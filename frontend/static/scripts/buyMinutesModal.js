document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2];

    const buyMinutesModal = document.getElementById('buy-minutes-modal');
    const buyMinutesButton = document.getElementById('buy-minutes-button');
    const closeMinutesModalButton = document.getElementById('close-buy-minutes-modal-button');

    buyMinutesButton.addEventListener('click', function () {
        buyMinutesModal.style.display = 'flex';
    });

    closeMinutesModalButton.addEventListener('click', function () {
        buyMinutesModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === buyMinutesModal) {
            buyMinutesModal.style.display = 'none';
        }
    });

    const buyMinutesForm = document.getElementById('buy-minutes-form');

    buyMinutesForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const minutesAmount = document.getElementById('minutes-amount').value;
        fetch(`http://93.175.7.10:5000/user/buy_minute/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({value: minutesAmount})
        }).then(response => {
            if (!response.ok) {
                throw new Error('Неправильно введено количество гигабайт');
            }
            return response.json();
        })
            .then(data => {
                console.log('Успешная покупка:', data);
                buyMinutesModal.style.display = 'none';
                alert('Успешная покупка!');
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
            });
    });
    buyMinutesModal.style.display = 'none';
})
;
