from P02.Client0 import Client
from P01.Seq1 import Seq

def get_gene_fragments(gene_sequence, fragment_size=10):

    gene_fragments = [str(gene_sequence[i:i + fragment_size]) for i in range(0, len(gene_sequence), fragment_size)]
    return gene_fragments

def send_fragments_to_server(gene_name, fragments):

    # Create a Client object
    c = Client(IP="192.168.1.45", PORT=8080)

    print("-----| Practice 2, Exercise 5 |------")
    print(c)

    # Print the NULL Seq information
    null_seq = Seq()  # Assuming you have a default constructor for Seq
    print(null_seq)

    # Print the original gene sequence
    original_gene_seq = Seq("FRAT1.txt") # Replace with actual gene sequence
    print(f"Gene {gene_name}: {original_gene_seq}")

    # Send each gene fragment to the server using the talk() method
    for i, fragment in enumerate(fragments, start=1):
        print(f"Fragment {i}: {fragment}")
        response = c.talk(fragment)
        print(f"Response from the server: {response}")


# Assuming you have a Seq class for gene sequences and gene data
# Replace the original_gene_sequence with the actual FRAT1 gene sequence.
original_gene_sequence = original_gene_seq

# Extract fragments of 10 bases each
gene_fragments = get_gene_fragments(original_gene_sequence, fragment_size=10)

# Send the fragments to the server
send_fragments_to_server("FRAT1", gene_fragments)