import requests

r=requests.get('https://github.com/hyunseo6579/404_lab1/blob/main/lab1.py')
print(r.text)