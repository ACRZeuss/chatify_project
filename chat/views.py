# chat/views.py
from rest_framework import generics, permissions
from .models import ChatRoom
from .serializers import ChatRoomSerializer

class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    # Sadece giriş yapmış kullanıcıların oda oluşturabilmesini sağlar
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Yeni oda oluşturulurken sahibini o anki kullanıcı olarak ayarla
        serializer.save(owner=self.request.user)