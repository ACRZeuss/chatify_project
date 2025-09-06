# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_room(self, room_slug):
        try:
            return ChatRoom.objects.get(slug=room_slug)
        except ChatRoom.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, room, content):
        Message.objects.create(room=room, author=self.scope['user'], content=content)

    async def connect(self):
        self.room_slug = self.scope['url_route']['kwargs']['room_slug']
        self.room_group_name = f'chat_{self.room_slug}'

        room = await self.get_room(self.room_slug)
        if room is None or not self.scope['user'].is_authenticated:
            await self.close()
            return

        self.room = room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        if not self.scope['user'].is_authenticated:
            return

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username

        await self.save_message(self.room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat_message', 'message': message, 'username': username}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))