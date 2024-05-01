function openTariffList() {
    var modal = document.getElementById('tariff-list-modal');
    modal.style.display = 'block';

    document.getElementById('tariff-list').innerHTML = '';
    fetch('http://93.175.7.10:5000/api/list_tariff')
        .then(response => {
            if (!response.ok) {
                throw new Error('Не удалось получить список тарифов');
            }
            return response.json();
        })
        .then(data => {
        var html = '';
        data.forEach(function(tariff) {
        html += '<tr>';
        html += '<td>' + tariff.id + '</td>';
        html += '<td>' + tariff.gb + '</td>';
        html += '<td>' + tariff.minute + '</td>';
        html += '<td>' + tariff.cost_one_gb + '</td>';
        html += '<td>' + tariff.cost_one_minute + '</td>';
        html += '<td>' + tariff.price + '</td>';
        html += '</tr>';
        });
        document.getElementById('tariff-list').innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка загрузки списка тарифов:', error);
            alert('Произошла ошибка при загрузке списка тарифов');
        });
}

function closeTariffListModal() {
    var modal = document.getElementById('tariff-list-modal');
    modal.style.display = 'none';
}
