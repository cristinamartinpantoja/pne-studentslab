import http.client
import json
from http import HTTPStatus

server = 'rest.ensembl.org'
resource = '/info/ping'
params = '?content-type=application/json'
url = server + resource + params

print()
print(f"Server: {server}")
print(f"Url: {url}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", resource + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response receiced!: {response.status} {response.reason}")
if response.status == HTTPStatus.OK:
    data_str = response.read().decode("utf-8")
    data = json.loads(data_str)
    ping = data['ping']
    print(f"ping: {ping}")
    if ping == 1:
        print("PING OK! The database is running!")
    else:
        print("...")