# Chatify: Gerçek Zamanlı Sohbet Uygulaması

`Chatify`, Python (Django & Channels) backend ve Vanilla JavaScript frontend kullanılarak geliştirilmiş, web tabanlı, modern ve gerçek zamanlı bir sohbet uygulamasıdır. Kullanıcıların dinamik olarak sohbet odaları oluşturmasına ve anlık olarak mesajlaşmasına olanak tanır.

---

## ✨ Özellikler

- **Kullanıcı Kimlik Doğrulama:** Güvenli giriş sistemi.
- **Dinamik Oda Yönetimi:** Kullanıcılar arayüz üzerinden kendi sohbet odalarını oluşturabilir.
- **Gerçek Zamanlı Mesajlaşma:** WebSocket teknolojisi sayesinde odalarda anlık ve gecikmesiz iletişim.
- **Veritabanı Entegrasyonu:** Gönderilen tüm mesajlar kalıcı olarak veritabanına kaydedilir.
- **Modern Arayüz:** Aydınlık ve Karanlık mod (Light/Dark Mode) desteği.
- **Kullanıcı Tercihleri:** Tema seçimi, tarayıcının yerel deposunda (`localStorage`) saklanarak kalıcı hale getirilir.
- **RESTful API:** Oda listeleme ve oluşturma işlemleri için standartlara uygun API endpoint'leri.

---

## 🛠️ Teknoloji Yığını

### Backend
- **Python 3.x**
- **Django:** Ana web çatısı.
- **Django Channels:** WebSocket ve diğer asenkron protokoller için entegrasyon katmanı.
- **Daphne:** `Channels` için ASGI sunucusu.
- **Django Rest Framework:** Temiz ve güçlü API'ler oluşturmak için.
- **Redis:** `Channels` için mesajlaşma katmanı (message broker).

### Frontend
- **HTML5**
- **CSS3:** Tema desteği için CSS Değişkenleri (Variables) ile birlikte.
- **Vanilla JavaScript (ES6+):** Herhangi bir framework olmadan, modern JavaScript özellikleri (Fetch API, DOM Manipulation) kullanılarak yazılmıştır.

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
- **Python 3.8+**
- **Redis:** [Redis'in resmi sitesinden](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/) veya işletim sisteminizin paket yöneticisiyle kurun. (Örn: `sudo apt install redis-server` veya `brew install redis`).

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
    pip install django daphne channels channels-redis djangorestframework django-cors-headers
    ```
    *(**İpucu:** Gelecekte kolaylık olması için `pip freeze > requirements.txt` komutuyla bir gereksinimler dosyası oluşturabilirsiniz.)*

4.  **Redis Sunucusunu Başlatın:**
    Yeni bir terminal açın ve `redis-server` komutunu çalıştırın. Bu terminalin arka planda çalışır durumda kalması gerekir.

5.  **Veritabanını Hazırlayın:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Admin Kullanıcısı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```
    Komut sizden bir kullanıcı adı, e-posta ve şifre isteyecektir.

7.  **Backend Sunucusunu Başlatın:**
    ```bash
    python manage.py runserver
    ```
    Sunucu artık `http://127.0.0.1:8000` adresinde çalışıyor.

8.  **Frontend'i Başlatın:**
    - **Yeni bir terminal** açın.
    - Sanal ortamı bu terminalde de aktif edin.
    - `frontend` klasörünün içine girin: `cd frontend`
    - Python'un dahili web sunucusu ile frontend'i çalıştırın:
        ```bash
        python -m http.server 5500
        ```
    - Şimdi tarayıcınızdan `http://127.0.0.1:5500` adresine gidin.

Artık uygulamayı kullanmaya hazırsınız!

---

## 📝 API Endpoints

- `POST /api/auth/login/`: Kullanıcı girişi yapmak ve session başlatmak için.
- `GET, POST /api/rooms/`: Tüm mevcut sohbet odalarını listeler veya yeni bir tane oluşturur.

---

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.