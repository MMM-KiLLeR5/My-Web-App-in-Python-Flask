document.addEventListener('DOMContentLoaded', function () {
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2]; // Предполагается, что username находится во второй части пути

    const rechargeBalanceModal = document.getElementById('recharge-balance-modal');
    const rechargeBalanceButton = document.getElementById('recharge-balance-button');
    const closeRechargeBalanceButton = document.getElementById('close-recharge-balance-button');

    rechargeBalanceButton.addEventListener('click', function () {
        rechargeBalanceModal.style.display = 'flex';
    });

    closeRechargeBalanceButton.addEventListener('click', function () {
        rechargeBalanceModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === rechargeBalanceModal) {
            rechargeBalanceModal.style.display = 'none';
        }
    });

    const rechargeBalanceForm = document.getElementById('recharge-balance-form');

    rechargeBalanceForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const value = document.getElementById('value_recharge').value;

        console.log('Amount to Recharge:', value);

        fetch(`http://93.175.7.10:5000/user/deposit/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'value': value})
        }).then(response => {
            if (!response.ok) {
                throw new Error('Недостаточно средств');
            }
            return response.json();
        })
            .then(data => {
                console.log('Успешное пополнение:', data);
                alert('Успешное пополнение');
                rechargeBalanceModal.style.display = 'none';
            })
            .catch(error => {
                console.error('Ошибка:', error);
                alert(error.message);
            });
    });
});
