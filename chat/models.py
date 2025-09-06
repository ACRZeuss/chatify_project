# chat/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from cryptography.fernet import Fernet

# Şifreleme için Fernet nesnesini ayar dosyasındaki anahtarla oluştur
fernet = Fernet(settings.ENCRYPTION_KEY)

class ChatRoom(models.Model):
    # ... (Bu modelde değişiklik yok) ...
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self._meta.get_field('name').default:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Mesaj içeriğini şifreli tutacağımız için TextField kullanmaya devam edebiliriz.
    encrypted_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def content(self):
        # Mesaj içeriği istendiğinde, şifreli veriyi çözüp geri döndür
        try:
            return fernet.decrypt(self.encrypted_content.encode()).decode()
        except Exception:
            return "Mesaj çözülemedi"

    def save(self, *args, **kwargs):
        # Normal 'content' alanını kullanmayacağımız için override etmiyoruz
        # Şifreleme işlemini consumer'da yapacağız.
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author.username}: [şifreli mesaj]'