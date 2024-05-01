document.addEventListener('DOMContentLoaded', function () {
    const userRegistrationForm = document.getElementById('userRegistrationForm');

    userRegistrationForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(userRegistrationForm)
        const jsonData = {};

        for (const [key, value] of formData.entries()) {
            jsonData[key] = value;
        }

        jsonData['tariff_id'] = parseInt(document.getElementById('tariff_id').value);
        console.log(jsonData)

        fetch('http://93.175.7.10:5000/user/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    // Проверяем статус ошибки
                    if (response.status === 409) {
                        throw new Error('Пользователь с таким номером паспорта уже зарегистрирован');
                    } else if (response.status === 410) {
                        throw new Error('Пользователь с таким номером телефона уже зарегистрирован');
                    } else if (response.status === 411) {
                        throw new Error('Пользователь с таким логином уже зарегистрирован');
                    } else {
                        throw new Error('Ошибка при регистрации');
                    }
                }
            })
            .then(data => {
                console.log('Успешная регистрация:', data);
                Notification.requestPermission().then(function (result) {
                    if (result === 'granted') {
                        new Notification('Регистрация успешно завершена');
                    }
                });
                setTimeout(() => {
                    window.location.href = "/user/login";
                }, 1000);
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
                window.location.href = "/user/register";
            });
    });
});

function goBack() {
    window.location.href = "/user/login"
}
