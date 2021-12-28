from requests import get, post
from json import dumps
host = 'localhost'
port = 5003

url = f"http://{host}:{port}/"

post_headers = {
    'Content-Type': 'application/json'
}

try:
    send_data = {'name': 'yossi', 'age': 205}
    get_data = get(url=url)
    post_data = post(url=url+'echo', data=dumps(send_data),
                     headers=post_headers)
except ConnectionError:
    print("error with connection")
print(get_data.json())
print(post_data.json())
