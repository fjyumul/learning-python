import requests

url = 'https://www.httpbin.org/get?name=Joseph&id=123'
payload = {
    "name":"Joseph", 
    "id":"123"
    }

response = requests.get(url, payload)

response.url
response.body
response.request.body
response.status_code
response.text
response.content.json()