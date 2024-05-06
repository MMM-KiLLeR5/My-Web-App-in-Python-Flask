function openExchangeMinList() {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2]; // Предполагается, что username находится во второй части пути
    var modal = document.getElementById('exchange-min-modal');
    modal.style.display = 'block';

    document.getElementById('exchange-min-list').innerHTML = '';
    fetch('http://93.175.7.10:5000/market/min_table')
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
                html += '<td>' + offer.min + '</td>';
                html += '<td>' + offer.cost + '</td>';
                html += '<td><button class="buy-button" onclick="buyMinOffer(\'' + username + '\', ' + iter + ')">Купить</button></td>';
                html += '</tr>';
                iter++;
            });
            document.getElementById('exchange-min-list').innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка загрузки списка тарифов:', error);
            alert('Произошла ошибка при загрузке списка тарифов');
        });
}

function closeExchangeMinListModal() {
    var modal = document.getElementById('exchange-min-modal');
    modal.style.display = 'none';
}
function buyMinOffer(username, offerId) {
    fetch(`http://93.175.7.10:5000/market/buy_min/${username}&${offerId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => {
        if (!response.ok) {
            if (response.status === 405) {
                throw new Error(`Недостаточно средств на балансе`);
            }
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
