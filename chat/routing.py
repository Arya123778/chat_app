from django.urls import path
from . import consumers

websockets_urlpatterns=[
    path('ws/chat/', consumers.ChatConsumers.as_asgi()),
]