# chat/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Bu satır 'ws/chat/herhangi-bir-oda-slug/' formatındaki tüm yolları yakalar
    re_path(r'^ws/chat/(?P<room_slug>[\w-]+)/$', consumers.ChatConsumer.as_asgi()),
]