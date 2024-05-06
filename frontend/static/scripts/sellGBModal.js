document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2];

    if (!username) {
        console.error('Username not found in URL path');
        return;
    }

    const sellGBModal = document.getElementById('sell-gb-modal');
    const sellGBButton = document.getElementById('sell-gb-button');
    const closeGBModalButton = document.getElementById('close-sell-gb-modal-button');

    sellGBButton.addEventListener('click', function () {
        sellGBModal.style.display = 'flex';
    });

    closeGBModalButton.addEventListener('click', function () {
        sellGBModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === sellGBModal) {
            sellGBModal.style.display = 'none';
        }
    });

    const sellGBForm = document.getElementById('sell-gb-form');

    sellGBForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const cost = document.getElementById('cost').value;
        const gb = document.getElementById('gb').value;

        console.log(cost);
        console.log(gb);
        fetch(`http://93.175.7.10:5000/market/sell_gb/${username}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                cost: cost,
                gb: gb
            })
        }).then(response => {
            if (!response.ok) {
                if (response.status === 405) {
                    throw new Error('Недостаточно гигабайт');
                }
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешно выставлено на продажу:', data);
            sellGBModal.style.display = 'none';
            alert('Успешно выставлено на продажу!');
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert(error.message);
        });
    });

    sellGBModal.style.display = 'none';
});
