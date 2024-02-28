from Client0 import Client
from P01.Seq1 import Seq
GENES = ["U5", "FRAT1", "ADA"]
GENES_DIR = "../sequences/"
PRACTICE = 2
EXERCISE = 4

IP = "212.128.255.103" # your IP address
PORT = 8081

def get_file_path(gene):
    return GENES_DIR + gene

def req_response_from_server(client, msg):
    print("To Server: {}".format(msg), sep="")
    response = client.talk(msg)
    print(f"From Server:{response}")

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Create a client object
c = Client(IP, PORT)

for g in GENES:
    s = Seq()
    s.seq_read_fasta(get_file_path(g))
    m = "Sending " + g + " Gene to the server..."
    req_response_from_server(c, m)
    m = str(s)
    req_response_from_server(c, m)