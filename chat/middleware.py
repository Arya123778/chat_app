from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser

# Import AccessToken and database_sync_to_async at module level (they work fine here)
from rest_framework_simplejwt.tokens import AccessToken
from channels.db import database_sync_to_async  
from channels.middleware import BaseMiddleware

# Fixed: Don't call get_user_model() at module level - use inside async function instead.
# Changed from: from django.contrib.auth import get_user_model (with User = get_user_model())
# To avoid "get_user_model() must be called inside an async function or after Django setup"

@database_sync_to_async  
def get_user_from_token(token_key):
    # Import user model inside the async function to avoid issues before Django setup is complete
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
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
