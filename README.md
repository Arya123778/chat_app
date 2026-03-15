# chat_app
A real-time chat-app built using Django, Django Channels, Websockets and JWT Authentication.

Features:-
1. JWT Authentication (Register, Login, Logout)
2. Real time messaging using websockets
3. Create and Join chat app
4. Sees who join and left the room
5. Chat history
6. Token refresh and blacklisting
7. User profiles with avtar and bio
8. Accessible online via ngrok tunneling

Tech Stack:-
1. Backend:- Django6.0.3
2. Real Time :- Django channels + websockets
3. Auth:- SimpleJWT
4. Message broker:- Redis
5. ASGI server:- Daphne
6. Database:- SQLite
7. Tunneling:- ngrok

Setup and Installation:-
#Prerequisites
Python 3.13+
Redis (running on port 6379)
ngrok (for public access)

1.Clone the respository:-
git clone <your-repo-url>
cd chat_app

2. Create and active virtual environment:-
python -m venv venv
venv\Scripts\activate        # Windows

3.Install dependencies:-
pip install django djangorestframework django-channels daphne
pip install channels-redis djangorestframework-simplejwt
pip install redis

4. Apply migrations:-
python manage.py migrate

5. Create superuser:-
python manage.py createsuperuser

Running the App:-
Every time you want to use the chat app, run these in order:
1. Terminal 1: Start Daphne(Django server)
venv\Scripts\activate
daphne -p 8000 chat_app.asgi:application
2. Terminal 2: Verify Redis is running
netstat -ano | findstr :6379
3. Terminal 3: Start ngrok (for public access)
.\ngrok.exe http 8000

Accessing the App:-
Locally:- http://127.0.0.1:8000
Online:- https://your-ngrok-url.ngrok-free.app

How to Chat with a Friend
1.Start Daphne, Redis, and ngrok (see above)
2. Open https://your-ngrok-url.ngrok-free.app in your browser
3. Login or Register
4. Create a room called general
5. Share the ngrok link with your friend
6. Friend opens the link → clicks Register → joins general room
7. Start chatting in real time! 




