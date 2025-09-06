# chat/urls.py (YENİ DOSYA)
from django.urls import path
from .views import ChatRoomListCreateView

urlpatterns = [
    path('', ChatRoomListCreateView.as_view(), name='room-list-create'),
]