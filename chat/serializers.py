# chat/serializers.py
from rest_framework import serializers
from .models import ChatRoom, Message # Message modelini import et

class ChatRoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'slug', 'owner']

# BU YENİ SERIALIZER'I EKLEYİN
class MessageSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    # Modeldeki 'content' property'sini kullanarak şifresi çözülmüş mesajı al
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'author_username', 'content', 'timestamp']