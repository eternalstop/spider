import requests


proxy = {'http': '163.204.242.45:9999'}
r = requests.get(url="https://music.163.com/", proxies=proxy, timeout=1)
print(r.status_code)
