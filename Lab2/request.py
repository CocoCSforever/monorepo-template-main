import requests

# r = requests.get('https://api.github.com/events')

# print(r.text)

r = requests.post('https://httpbin.org/post', data={'data': '222'})