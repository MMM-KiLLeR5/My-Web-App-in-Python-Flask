document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2]; // Предполагается, что username находится во второй части пути

    const shareMINModal = document.getElementById('share-minutes-modal');
    const shareMINButton = document.getElementById('share-minutes-button');
    const closeMINModalButton = document.getElementById('close-minutes-modal-button');

    shareMINButton.addEventListener('click', function () {
        shareMINModal.style.display = 'flex';
    });

    closeMINModalButton.addEventListener('click', function () {
        shareMINModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === shareMINModal) {
            shareMINModal.style.display = 'none';
        }
    });

    const shareMINForm = document.getElementById('share-minutes-form');

    shareMINForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const phone_number = document.getElementById('phone_number_min').value;
        const value = document.getElementById('value_min').value;

        fetch(`http://93.175.7.10:5000/user/share_minute/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    phone_number,
                    value
                })
        }).then(response => {
            if (!response.ok) {
                if (response.status === 409) {
                    throw new Error('Пользователя с таким номером телефона не существует');
                } else if (response.status === 410) {
                    throw new Error('Не хватает средств для перевода');
                }
            }
        })
            .then(data => {
                console.log('Успешный перевод:', data);
                shareMINModal.style.display = 'none';
                alert('Перевод успешно завершен!');
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
            });
    });
});
