# Chatify: Gerçek Zamanlı Sohbet Uygulaması

`Chatify`, Python (Django & Channels) backend ve Vanilla JavaScript frontend kullanılarak geliştirilmiş, web tabanlı, modern ve gerçek zamanlı bir sohbet uygulamasıdır. Kullanıcıların dinamik olarak sohbet odaları oluşturmasına, geçmiş mesajları görüntülemesine ve anlık olarak mesajlaşmasına olanak tanır. Tüm mesajlar, veritabanında uçtan uca şifrelenmiş olarak saklanır.

---

## ✨ Özellikler

-   **Kullanıcı Kimlik Doğrulama:** Güvenli giriş sistemi.
-   **Dinamik Oda Yönetimi:** Kullanıcılar arayüz üzerinden kendi sohbet odalarını oluşturabilir.
-   **Gerçek Zamanlı Mesajlaşma:** WebSocket teknolojisi sayesinde odalarda anlık ve gecikmesiz iletişim.
-   **Kalıcı Mesaj Geçmişi:** Odalara girildiğinde önceki sohbetler yüklenir.
-   **Güçlü Şifreleme:** Veritabanına kaydedilen tüm mesaj içerikleri `cryptography` kütüphanesi kullanılarak şifrelenir.
-   **Modern Arayüz:** Aydınlık ve Karanlık mod (Light/Dark Mode) desteği.
-   **Kullanıcı Tercihleri:** Tema seçimi, tarayıcının yerel deposunda (`localStorage`) saklanarak kalıcı hale getirilir.
-   **RESTful API:** Oda ve mesaj listeleme/oluşturma işlemleri için standartlara uygun API endpoint'leri.

---

## 🛠️ Teknoloji Yığını

### Backend
-   **Python 3.x**
-   **Django:** Ana web çatısı.
-   **Django Channels:** WebSocket ve diğer asenkron protokoller için entegrasyon katmanı.
-   **Daphne:** `Channels` için ASGI sunucusu.
-   **Django Rest Framework:** Temiz ve güçlü API'ler oluşturmak için.
-   **Redis:** `Channels` için mesajlaşma katmanı (message broker).
-   **Cryptography:** Mesaj içeriklerinin güvenliği için.

### Frontend
-   **HTML5**
-   **CSS3:** Tema desteği için CSS Değişkenleri (Variables) ile birlikte.
-   **Vanilla JavaScript (ES6+):** Herhangi bir framework olmadan, modern JavaScript özellikleri (Fetch API, DOM Manipulation) kullanılarak yazılmıştır.

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
-   **Python 3.8+**
-   **Redis:** [Redis'in resmi sitesinden](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/) veya işletim sisteminizin paket yöneticisiyle kurun. (Örn: `sudo apt install redis-server` veya `brew install redis`).

### Adım Adım Kurulum

1.  **Projeyi Klonlayın (veya indirin):**
    ```bash
    git clone https://github.com/ACRZeuss/chatify_project.git
    cd chatify_project
    ```

2.  **Sanal Ortamı (Virtual Environment) Oluşturun ve Aktif Edin:**
    ```bash
    python -m venv venv
    # Windows için:
    venv\Scripts\activate
    # macOS/Linux için:
    source venv/bin/activate
    ```

3.  **Gerekli Python Kütüphanelerini Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Şifreleme Anahtarı Oluşturun ve Ayarlayın:**
    -   `python manage.py shell` komutunu çalıştırın.
    -   `from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())` komutunu çalıştırın ve çıkan anahtarı kopyalayın.
    -   `.env` dosyasına `ENCRYPTION_KEY = 'your-generated-key-here'` satırını ekleyin.

5.  **Redis Sunucusunu Başlatın:**
    Yeni bir terminal açın ve `redis-server` komutunu çalıştırın. Bu terminalin arka planda çalışır durumda kalması gerekir.

6.  **Veritabanını Hazırlayın:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Admin Kullanıcısı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Backend Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```
    Sunucu artık `http://120.0.1:8000` adresinde çalışıyor.

9.  **Frontend'i Başlatın:**
    -   **Yeni bir terminal** açın.
    -   `frontend` klasörünün içine girin: `cd frontend`
    -   Python'un dahili web sunucusu ile frontend'i çalıştırın:
        ```bash
        python -m http.server 5500
        ```
    -   Şimdi tarayıcınızdan `http://127.0.0.1:5500` adresine gidin.

Artık uygulamayı kullanmaya hazırsınız!

---

## 📝 API Endpoints

-   `POST /api/auth/login/`: Kullanıcı girişi yapmak ve session başlatmak için.
-   `GET, POST /api/rooms/`: Tüm mevcut sohbet odalarını listeler veya yeni bir tane oluşturur.
-   `GET /api/rooms/<slug>/messages/`: Belirtilen odaya ait mesaj geçmişini listeler.

---

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.