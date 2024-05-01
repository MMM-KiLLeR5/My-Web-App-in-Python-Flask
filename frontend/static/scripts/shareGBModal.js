document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2]; // Предполагается, что username находится во второй части пути

    const shareGBModal = document.getElementById('share-gb-modal');
    const shareGBButton = document.getElementById('share-gb-button');
    const closeGBModalButton = document.getElementById('close-gb-modal-button');

    shareGBButton.addEventListener('click', function () {
        shareGBModal.style.display = 'flex';
    });

    closeGBModalButton.addEventListener('click', function () {
        shareGBModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === shareGBModal) {
            shareGBModal.style.display = 'none';
        }
    });

    const shareGBForm = document.getElementById('share-gb-form');

    shareGBForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const phone_number = document.getElementById('phone_number').value;
        const value = document.getElementById('value').value;

        fetch(`http://93.175.7.10:5000/user/share_gb/${username}`, {
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
                console.log('Успешный перевод:');
                shareGBModal.style.display = 'none';
                alert('Перевод успешно завершен!');
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
            });
    });
});
