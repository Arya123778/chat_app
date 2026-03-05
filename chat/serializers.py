from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Room, Message

User=get_user_model

class UserSummarySerializer(serializers.ModelSerializer):
    """Small user info to show inside messages"""
    class Meta:
        model=User
        fields=['id','username','avatar','is_online']

class MessageSerializer(serializers.ModelSerializer):
    sender=UserSummarySerializer(read_only=True)
    class Meta:
        model=Message
        fields=['id','room','sender','content','timestamp','is_read']
        read_only_fields=['id','sender','timestamp']
        
class RoomSerializer(serializers.ModelSerializer):
    members=UserSummarySerializer(many=True, read_only=True)
    created_by=UserSummarySerializer(read_only=True)
    last_message=serializers.SerializerMethodField()
    member_count=serializers.SerializerMethodField()
    
    class Meta:
        model=Room
        fields=['id','name','description','created_by','members','member_count','last_message','created_at']
        
    def get_last_message(self,obj):
        """Return the most recent message in the room"""
        last=obj.messages.last()
        if last:
            return{
                'content':last.content,
                'sender':last.sender.username,
                'timestamp':last.timestamp
            } 
            return None
    def get_member_count(self, obj):
        return obj.members.count()
        