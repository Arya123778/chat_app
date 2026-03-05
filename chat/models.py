from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model

class Room(models.Model):
    name=models.CharField(max_length=100, unique=True)
    description=models.TextField(blank=True, null=True)
    created_by=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_rooms")
    members=models.ManyToManyField(User, related_name="rooms", blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        self.name

class Message(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
    
    class Meta:
        ordering=['timestamp']
    
    def __str__(self):
        return f'{self.sender.username} -> {self.room.name} : {self.content[:50]}'