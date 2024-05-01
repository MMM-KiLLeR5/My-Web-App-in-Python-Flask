document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2];

    if (!username) {
        console.error('Username not found in URL path');
        return;
    }

    const buyGBModal = document.getElementById('buy-gb-modal');
    const buyGBButton = document.getElementById('buy-gb-button');
    const closeGBModalButton = document.getElementById('close-buy-gb-modal-button');

    buyGBButton.addEventListener('click', function () {
        buyGBModal.style.display = 'flex';
    });

    closeGBModalButton.addEventListener('click', function () {
        buyGBModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === buyGBModal) {
            buyGBModal.style.display = 'none';
        }
    });

    const buyGBForm = document.getElementById('buy-gb-form');

    buyGBForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const gbAmount = document.getElementById('gb-amount').value;

        console.log(gbAmount);
        fetch(`http://93.175.7.10:5000/user/buy_gb/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: gbAmount })
        }).then(response => {
            if (!response.ok) {
                throw new Error('Неправильно введено количество гигабайт');
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешная покупка:', data);
            buyGBModal.style.display = 'none';
            alert('Успешная покупка!');
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert(error.message);
        });
    });

    buyGBModal.style.display = 'none';
});
