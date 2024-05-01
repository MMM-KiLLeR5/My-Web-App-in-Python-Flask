function openProfileModal() {
    document.getElementById('profile-modal').style.display = 'block';
}

function closeProfileModal() {
    document.getElementById('profile-modal').style.display = 'none';
}

const path = window.location.pathname;
const parts = path.split('/');
const username = parts[2];

const requestData = {
    username: username
};

const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
};

fetch('http://93.175.7.10:5000/user/data_of_users', options)
    .then(response => response.json())
    .then(data => {
        const profileModalContent = document.getElementById('profile-modal-content');
        profileModalContent.innerHTML = `
            <h2>Мой профиль</h2>
            <div class="profile-info">
                <p><strong>ГБ:</strong> ${data.user_gbs}</p>
                <p><strong>Минуты:</strong> ${data.user_minutes}</p>
                <p><strong>Баланс:</strong> ${data.balance}</p>
                <p><strong>Тариф:</strong></p>
                <ul class="tariff-info">
                    <li><strong>GB:</strong> ${data.gb}</li>
                    <li><strong>Минуты:</strong> ${data.minute}</li>
                    <li><strong>Цена за 1 GB:</strong> ${data.cost_one_gb}</li>
                    <li><strong>Цена за 1 минуту:</strong> ${data.cost_one_minute}</li>
                    <li><strong>Общий прайс:</strong> ${data.price}</li>
                </ul>
            </div>
            <button class="close-btn" onclick="closeProfileModal()">Закрыть</button>
        `;
    })
    .catch(error => console.error('Ошибка получения информации о пользователе:', error));
