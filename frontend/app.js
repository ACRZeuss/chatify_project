// frontend/app.js

document.addEventListener('DOMContentLoaded', () => {
    // --- DARK MODE KODU BAŞLANGIÇ ---
    const darkModeToggle = document.querySelector('#dark-mode-toggle');
    const body = document.body;

    // Sayfa yüklendiğinde kayıtlı temayı uygula
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
    }

    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        // Seçimi localStorage'a kaydet
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
    });
    // --- DARK MODE KODU BİTİŞ ---


    // --- ELEMENT SEÇİMLERİ ---
    const loginContainer = document.querySelector('#login-container');
    const roomContainer = document.querySelector('#room-container');
    const chatContainer = document.querySelector('#chat-container');
    const loginForm = document.querySelector('#login-form');
    const roomList = document.querySelector('#room-list');
    const createRoomForm = document.querySelector('#create-room-form');
    const chatLog = document.querySelector('#chat-log');
    const chatForm = document.querySelector('#chat-form');
    const messageInput = document.querySelector('#chat-message-input');
    const roomNameHeader = document.querySelector('#chat-room-name');
    const backToRoomsButton = document.querySelector('#back-to-rooms');
    const logoutButton = document.querySelector('#logout-button');

    let chatSocket = null;

    // --- YARDIMCI FONKSİYONLAR ---
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const apiRequest = async (url, method = 'GET', body = null) => {
        const headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        };
        const config = { method, headers, credentials: 'include' };
        if (body) {
            config.body = JSON.stringify(body);
        }
        const response = await fetch(url, config);
        if (!response.ok) {
            throw new Error(`API isteği başarısız: ${response.statusText}`);
        }
        return response.status === 204 ? null : response.json();
    };

    // --- ANA UYGULAMA MANTIĞI ---

    const showView = (view) => {
        loginContainer.classList.add('hidden');
        roomContainer.classList.add('hidden');
        chatContainer.classList.add('hidden');
        view.classList.remove('hidden');
    };

    const loadRooms = async () => {
        try {
            const rooms = await apiRequest('http://127.0.0.1:8000/api/rooms/');
            roomList.innerHTML = ''; // Listeyi temizle
            if (rooms.length === 0) {
                roomList.innerHTML = '<p>Henüz hiç sohbet odası yok. İlk odayı sen oluştur!</p>';
            } else {
                rooms.forEach(room => {
                    const roomElement = document.createElement('button');
                    roomElement.className = 'room-btn';
                    roomElement.textContent = room.name;
                    roomElement.dataset.slug = room.slug;
                    roomList.appendChild(roomElement);
                });
            }
        } catch (error) {
            console.error('Odalar yüklenemedi:', error);
            roomList.innerHTML = '<p>Odalar yüklenirken bir hata oluştu.</p>';
        }
    };

    const enterChatRoom = (slug, name) => {
        showView(chatContainer);
        roomNameHeader.textContent = `Sohbet Odası: ${name}`;

        if (chatSocket) chatSocket.close();

        chatSocket = new WebSocket(`ws://127.0.0.1:8000/ws/chat/${slug}/`);

        chatSocket.onopen = () => console.log('WebSocket bağlantısı kuruldu.');
        chatSocket.onclose = () => console.error('WebSocket bağlantısı kapandı.');
        
        chatSocket.onmessage = (e) => {
            const data = JSON.parse(e.data);
            chatLog.innerHTML += `<div><b>${data.username}:</b> ${data.message}</div>`;
            chatLog.scrollTop = chatLog.scrollHeight;
        };
    };

    // --- OLAY DİNLEYİCİLERİ ---

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = e.target.elements.username.value;
        const password = e.target.elements.password.value;
        try {
            await apiRequest('http://127.0.0.1:8000/api/auth/login/', 'POST', { username, password });
            showView(roomContainer);
            await loadRooms();
        } catch (error) {
            alert('Kullanıcı adı veya şifre hatalı!');
        }
    });

    createRoomForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const roomNameInput = e.target.elements['new-room-name'];
        const name = roomNameInput.value.trim();
        if (name) {
            try {
                await apiRequest('http://127.0.0.1:8000/api/rooms/', 'POST', { name });
                roomNameInput.value = '';
                await loadRooms(); // Listeyi yenile
            } catch (error) {
                alert('Oda oluşturulamadı. Bu isimde bir oda zaten olabilir.');
            }
        }
    });

    roomList.addEventListener('click', (e) => {
        if (e.target && e.target.classList.contains('room-btn')) {
            const { slug } = e.target.dataset;
            const name = e.target.textContent;
            enterChatRoom(slug, name);
        }
    });

    chatForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (message && chatSocket && chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({ message }));
            messageInput.value = '';
        }
    });

    backToRoomsButton.addEventListener('click', () => {
        if (chatSocket) chatSocket.close();
        chatLog.innerHTML = '';
        showView(roomContainer);
        loadRooms();
    });

    logoutButton.addEventListener('click', () => {
        window.location.reload();
    });
    
    showView(loginContainer);
});