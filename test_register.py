import urllib.request
import urllib.parse
import json

data = json.dumps({
    'username': 'arya',
    'email': 'arya@gmail.com',
    'password': 'arya1234567890',
    'password2': 'arya1234567890'
}).encode('utf-8')

req = urllib.request.Request(
    'http://127.0.0.1:8000/api/accounts/register/',
    data=data,
    headers={'Content-Type': 'application/json'}
)

try:
    response = urllib.request.urlopen(req)
    print("Status:", response.status)
    print("Response:", response.read().decode())
except urllib.error.HTTPError as e:
    print("Status:", e.code)
    print("Error:", e.read().decode())
