from e2 import genes
import http.client
import json
import termcolor
from Seq1 import Seq

name = input("Write the gene name: ")

if name in genes:
    code = genes[name]

    server = "rest.ensembl.org"
    resource = "/sequence/id/" + code
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
    print(name)
    termcolor.cprint("Description: ", color="green", end="")
    print(person["desc"])
    seq = person["seq"]

    s = Seq(seq)
    termcolor.cprint("Total length of the sequence: ", color="green", end="")
    print(s.seq_len())
    bases = {"A": 0, "G": 0, "T": 0, "C": 0}
    for i in bases.keys():
        termcolor.cprint(i + ": ", color="blue", end="")
        print(s.seq_count(i))
        count = s.seq_count(i).split(" ")
        bases[i] += int(count[0])

    termcolor.cprint("Most frequent base: ", color="green", end="")
    sort = sorted(bases.items(), key=lambda x: x[1], reverse=True)
    print(sort[0][0])

else:
    print("Try another gene. ")