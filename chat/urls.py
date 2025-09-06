# chat/urls.py (YENİ DOSYA)
from django.urls import path
from .views import ChatRoomListCreateView, MessageListView # MessageListView'i import et

urlpatterns = [
    path('', ChatRoomListCreateView.as_view(), name='room-list-create'),
    path('<slug:room_slug>/messages/', MessageListView.as_view(), name='message-list'),
]