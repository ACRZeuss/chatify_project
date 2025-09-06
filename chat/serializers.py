# chat/serializers.py (YENİ DOSYA)
from rest_framework import serializers
from .models import ChatRoom

class ChatRoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'slug', 'owner']