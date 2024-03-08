from Seq0 import seq_reverse, seq_read_fasta

print("------| Exercise 6 |------")

genes = ['U5', 'ADA', 'FRAT1', 'FXN']

for gene in genes:
    file_path = f"../sequences/{gene}"
    gene_counts = seq_reverse(file_path)
    gene_sequence = seq_read_fasta(file_path)
    print(f"Gene {gene}:")

    # Create a fragment of the first 20 bases
    fragment = gene_sequence[:20]
    print(f"Fragment: {fragment}")

    # Calculate and print the reverse of the fragment
    fragment_reverse = seq_reverse(fragment)
    print(f"Reverse:", fragment_reverse)
    print("\n")