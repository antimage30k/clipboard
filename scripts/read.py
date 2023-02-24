import json
import winreg
from urllib import request

res = request.urlopen("http://127.0.0.1:8080/ojj/bs/meter/task").read().decode("utf-8")

rsp = json.loads(res)
user_names = []
data = rsp['data']
for node in data:
    for model in node['user_models']:
        user_names.append(model['user_name'])

print(user_names)

a = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", 0, winreg.KEY_READ)
name, regsz = winreg.QueryValueEx(a, "ProductName")
print(name)
