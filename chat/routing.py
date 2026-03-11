from django.urls import re_path
from . import consumers

# Updated regex to support room names with letters, numbers, hyphens, and underscores
websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>[\w-]+)/$', consumers.ChatConsumer.as_asgi()),
]
