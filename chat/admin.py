from django.contrib import admin
from .models import Room,Message
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['name','created_by','created_at']
    filter_horizontal=['members']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['sender','room','content','timestamp','is_read']
    list_filter=['room','is_read']