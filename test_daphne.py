import urllib.request
import json

# Test server is running
try:
    response = urllib.request.urlopen('http://127.0.0.1:8000/')
    print('Server Status:', response.status)
except Exception as e:
    print('Server Error:', e)

# Test registration endpoint
data = json.dumps({'username': 'testuser2', 'email': 'test2@example.com', 'password': 'TestPass123!', 'password2': 'TestPass123!'}).encode()
req = urllib.request.Request('http://127.0.0.1:8000/api/accounts/register/', data=data, method='POST')
req.add_header('Content-Type', 'application/json')
try:
    response = urllib.request.urlopen(req)
    print('Register Status:', response.status)
except Exception as e:
    print('Register Error:', e)

print('\n✅ Daphne server test completed!')
