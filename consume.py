from urllib import response
import requests

res=requests.get('http://127.0.0.1:8000/drinks/')

print(res.json())