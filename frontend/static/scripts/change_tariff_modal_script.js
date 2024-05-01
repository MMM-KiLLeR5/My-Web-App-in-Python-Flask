function openChangeTariffModal() {
    document.getElementById('change-tariff-modal').classList.add('show-modal');
}

function closeChangeTariffModal() {
    document.getElementById('change-tariff-modal').classList.remove('show-modal');
}

document.getElementById('change-tariff-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const formData = new FormData(this);
    const jsonData = {};

    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });
    const tariffId = parseInt(jsonData['id']);
    delete jsonData['id'];
    console.log(tariffId);
    fetch(`http://93.175.7.10:5000/api/edit_tariff/${tariffId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
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
