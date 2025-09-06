# chat/views.py
from rest_framework import generics, permissions
from .models import ChatRoom, Message # Message'ı import et
from .serializers import ChatRoomSerializer, MessageSerializer # MessageSerializer'ı import et

class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    # Sadece giriş yapmış kullanıcıların oda oluşturabilmesini sağlar
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Yeni oda oluşturulurken sahibini o anki kullanıcı olarak ayarla
        serializer.save(owner=self.request.user)
        
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # URL'den gelen oda slug'ına göre mesajları filtrele
        room_slug = self.kwargs['room_slug']
        return Message.objects.filter(room__slug=room_slug).order_by('timestamp')