from Client import Client

class SeqClient:
    def __init__(self, host, port):
        self.client = Client(host, port)

    def test_ping(self):
        print("* Testing PING...")
        response = self.client.talk("PING")
        print(response)

    def test_get(self, num):
        print(f"* Testing GET {num}...")
        response = self.client.talk(f"GET {num}")
        print(response)

    def test_info(self, sequence):
        print(f"* Testing INFO...")
        response = self.client.talk(f"INFO {sequence}")
        print(response)

    def test_comp(self, sequence):
        print(f"* Testing COMP...")
        response = self.client.talk(f"COMP {sequence}")
        print(response)

    def test_rev(self, sequence):
        print(f"* Testing REV...")
        response = self.client.talk(f"REV {sequence}")
        print(response)

    def test_gene(self, gene_name):
        print(f"* Testing GENE...")
        response = self.client.talk(f"GENE {gene_name}")
        print(response)

if __name__ == "__main__":
    client = SeqClient('127.0.0.1', 8080)

    print("-----| Practice 3, Exercise 7 |------")
    client.test_ping()
    client.test_get(0)

    sequence = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
    client.test_info(sequence)
    client.test_comp(sequence)
    client.test_rev(sequence)

    genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
    for gene in genes:
        client.test_gene(gene)