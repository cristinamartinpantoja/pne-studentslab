import http.client
import json
import termcolor

server = "rest.ensembl.org"
resource = "/sequence/id/ENSG00000207552"
params = "?content-type=application/json"
url = server + resource + params

print()
print(f"Server {server}")
print(f"URL {url}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", resource + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
data_str = response.read().decode("utf-8")

person = json.loads(data_str)

termcolor.cprint("Gene: ", color="green", end="")
print("MIR633")
termcolor.cprint("Description: ", color="green", end="")
print(person["desc"])
termcolor.cprint("Bases: ", color="green", end="")
print(person["seq"])