# chat/admin.py
from django.contrib import admin
from .models import ChatRoom, Message # Modellerimizi buradan import ediyoruz

# Modellerimizi admin paneline kaydediyoruz
admin.site.register(ChatRoom)
admin.site.register(Message)