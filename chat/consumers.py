import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user=self.scope['user']
        
        if not user.is_authenticated:
            await self.close()
            return
        
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name=f'chat_{self.room_name}'
        
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'user_join',
                'user':user.username,
            }
        )
    async def disconnect(self,close_code):
        user=self.scope['user']
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'user_left',
                'user':user.username,
            }
        )
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive(self, text_data):
        """called when message is received form websocket"""
        data=json.loads(text_data)
        message=data.get('message','').strip()
        
        if not message:
            return
        user=self.scope['user']
        
        await self.save_message(user,self.room_name,message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'sender':user.username,
                'sender_id':user.id,
            }
        )
        
    async def chat_message(self, event):
        """send chat message to websocket"""
        await self.send(text_data=json.dumps({
            'type':'message',
            'message':event['message'],
            'sender':event['sender'],
            'sender_id':event['sender_id'],
        }))
    
    async def user_join(self,event):
        """Notify room when someone joins"""
        await self.send(text_data=json.dumps({
            'type':'user_join',
            'user':event['user'],
        }))
    
    async def user_leave(self,event):
        """Notify room when someone leaves"""
        await self.send(text_data=json.dumps({
            'type':'user_leave',
            'user':event['user'],
        }))
    
    @database_sync_to_async
    def save_message(self,user,room_name, content):
        room, _=Room.objects.get_or_create(name=room_name)
        return Message.objects.create(room=room,sender=user,content=content)