function openChangeTariffModal() {
    document.getElementById('change-tariff-modal').style.display = 'flex';
}

function closeChangeTariffModal() {
    document.getElementById('change-tariff-modal').style.display = 'none';
}

document.getElementById('change-tariff-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const formData = new FormData(this);
    const jsonData = {};

    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2];


    const tariffId = parseInt(jsonData['id']);

    fetch(`http://93.175.7.10:5000/user/change_tariff/${username}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({tariff_id: tariffId})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось изменить тариф');
        }
        closeChangeTariffModal();
        alert('Тариф успешно изменён!');
    })
    .catch(error => {
        console.error('Ошибка:', error);
        alert(error.message);
    });
});
