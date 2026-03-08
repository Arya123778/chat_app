from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

User=get_user_model()

@database_sync_to_async
def get_user_from_token(token_key):
    try:
        token=AccessToken(token_key)
        user_id=token['user_id']
        return User.objects.get(id=user_id)
    except Exception:
        return AnonymousUser()

class JWTAuthMiddleware(BaseMiddleware):
    """Reads JWT token from WebSockets query string"""
    async def __call__(self,scope,receive, send):
        query_prams=parse_qs(scope['query_string'].decode())
        token=query_prams.get('token',[None])[0]
        scope['user']=await get_user_from_token(token) if token else AnonymousUser()
        return await super().__call__(scope,receive,send)