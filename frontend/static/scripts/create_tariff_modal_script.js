function openModal() {
    document.getElementById('modal').classList.add('show-modal');
}

function closeModal() {
    document.getElementById('modal').classList.remove('show-modal');
}

document.getElementById('create-tariff-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const formData = new FormData(this);
    const jsonData = {};

    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });

    fetch('http://93.175.7.10:5000/api/login/create_tariff', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось создать тариф');
        }
        closeModal();
        alert('Успешно!');
    })
    .catch(error => {
        console.error('Ошибка:', error);
        alert(error.message);
    });
});
