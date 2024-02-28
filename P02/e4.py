from Client0 import Client
from P01.Seq1 import Seq

def send_gene_to_server(gene_name, gene_sequence):

    # Create a Client object
    c = Client(IP="192.168.1.45", PORT=8080)

    # Print the message before sending the gene
    print(f"Sending the {gene_name} Gene to the server...")

    # Send the gene sequence to the server using the talk() method
    response = c.talk(str(gene_sequence))

    # Print the response from the server
    print(f"Response from the server: {response}")


# Assuming you have a Seq class for gene sequences and gene data
# Replace the gene_sequence_U5, gene_sequence_FRAT1, and gene_sequence_ADA
# with the actual gene sequences obtained from the Seq class.
gene_sequence_U5 = Seq("U5_Gene_Sequence")
gene_sequence_FRAT1 = Seq("FRAT1_Gene_Sequence")
gene_sequence_ADA = Seq("ADA_Gene_Sequence")

# Send each gene to the server
send_gene_to_server("U5", gene_sequence_U5)
send_gene_to_server("FRAT1", gene_sequence_FRAT1)
send_gene_to_server("ADA", gene_sequence_ADA)