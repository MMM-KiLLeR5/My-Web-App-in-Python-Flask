document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2];

    if (!username) {
        console.error('Username not found in URL path');
        return;
    }

    const sellMinuteModal = document.getElementById('sell-minute-modal');
    const sellMinuteButton = document.getElementById('sell-minute-button');
    const closeMinuteModalButton = document.getElementById('close-sell-minute-modal-button');

    sellMinuteButton.addEventListener('click', function () {
        sellMinuteModal.style.display = 'flex';
    });

    closeMinuteModalButton.addEventListener('click', function () {
        sellMinuteModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === sellMinuteModal) {
            sellMinuteModal.style.display = 'none';
        }
    });

    const sellMinuteForm = document.getElementById('sell-minute-form');

    sellMinuteForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const cost = document.getElementById('cost_min').value;
        const min = document.getElementById('min').value;

        console.log(cost);
        console.log(min);
        fetch(`http://93.175.7.10:5000/market/sell_min/${username}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                cost: cost,
                min: min
            })
        }).then(response => {
            if (!response.ok) {
                if (response.status === 405)
                throw new Error('Недостаточно минут');
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешно выставлено на продажу:', data);
            sellMinuteModal.style.display = 'none';
            alert('Успешно выставлено на продажу!');
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert(error.message);
        });
    });

    sellMinuteModal.style.display = 'none';
});
