import requests

r=requests.get('https://raw.githubusercontent.com/hyunseo6579/404_lab1/master/lab1.py')
print(r.text)