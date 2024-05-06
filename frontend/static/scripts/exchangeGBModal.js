function openExchangeGBList() {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2]; // Предполагается, что username находится во второй части пути
    var modal = document.getElementById('exchange-gb-modal');
    modal.style.display = 'block';

    document.getElementById('exchange-gb-list').innerHTML = '';
    fetch('http://93.175.7.10:5000/market/gb_table')
        .then(response => {
            if (!response.ok) {
                throw new Error('Не удалось получить список тарифов');
            }
            return response.json();
        })
        .then(data => {
            var html = '';
            var iter = 1;
            data.forEach(function(offer) {
                html += '<tr>';
                html += '<td>' + iter + '</td>';
                html += '<td>' + offer.gb + '</td>';
                html += '<td>' + offer.cost + '</td>';
                html += '<td><button class="buy-button" onclick="buyGBOffer(\'' + username + '\', ' + iter + ')">Купить</button></td>';
                html += '</tr>';
                iter++;
            });
            document.getElementById('exchange-gb-list').innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка загрузки списка тарифов:', error);
            alert('Произошла ошибка при загрузке списка тарифов');
        });
}

function closeExchangeGBListModal() {
    var modal = document.getElementById('exchange-gb-modal');
    modal.style.display = 'none';
}
function buyGBOffer(username, offerId) {
    fetch(`http://93.175.7.10:5000/market/buy_gb/${username}&${offerId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => {
        if (response.status === 405) {
            throw new Error(`Недостаточно средств на балансе`);
        }
        alert('Успешная покупка!');
        location.reload();
        return response.json();
    })
    .catch(error => {
        console.error('Ошибка при выполнении запроса:', error);
        alert(error.message);
    });
}


