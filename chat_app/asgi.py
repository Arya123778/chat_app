"""
ASGI config for chat_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

# Fixed: Need to call django.setup() before importing other Django modules 
# This ensures Django is properly initialized before using get_user_model()
import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter  
from django.core.asgi import get_asgi_application  
import chat.routing  
# Fixed: Import our custom JWT middleware for WebSocket authentication 
from chat.middleware import JWTAuthMiddleware  

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    # Fixed: Use JWTAuthMiddleware instead of AuthMiddlewareStack for JWT token support in WebSockets 
    # Our middleware reads the token from query string (?token=xxx) and authenticates the user 
    'websocket':JWTAuthMiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
