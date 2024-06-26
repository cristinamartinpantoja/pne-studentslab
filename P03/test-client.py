from Client0 import Client

PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

ip = "127.0.0.1"
port = 8080
c = Client(ip, port)
print(f"Connection to SERVER at {ip}, PORT: {port}")

print("* Testing PING...")
print(f"{c.talk('PING')}\n")

print("* Testing GET...")
print(f"GET 0: {c.talk('GET 0')}\nGET 1: {c.talk('GET 1')}\nGET 2: {c.talk('GET 2')}\nGET 3: {c.talk('GET 3')}\nGET 4: {c.talk('GET 4')}\n")

print("* Testing INFO...")
print(f"{c.talk('INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA')}\n")

print("* Testing COMP...")
print(f"COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA\n{c.talk('COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA')}\n")

print("* Testing REV...")
print(f"REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA\n{c.talk('REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA')}\n")

print(f"* Testing GENE...\nGENE U5\n{c.talk('GENE U5')}\n\nGENE ADA\n{c.talk('GENE ADA')}\n\nGENE FRAT1\n{c.talk('GENE FRAT1')}\n\nGENE FXN\n{c.talk('GENE FXN')}\n\nGENE RNU6_269P\n{c.talk('GENE RNU6_269P')}")