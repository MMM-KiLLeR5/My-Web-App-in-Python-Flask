document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(loginForm);
        const jsonData = {};

        for (const [key, value] of formData.entries()) {
            jsonData[key] = value;
        }
        fetch('http://93.175.7.10:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Неправильный логин или пароль');
                }
                return response.json();
            })
            .then(data => {
                console.log('Успешный вход:', data);
                window.location.href = `/admin/${jsonData['username']}/dashboard?jwt=${data['access_token']}`;
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
                window.location.href = "/admin/login";
            });
    });
});

function goToMainPage() {
    window.location.href = "/";
}