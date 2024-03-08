from Seq0 import seq_complement, seq_read_fasta

print("------| Exercise 7 |------")

genes = ['U5', 'ADA', 'FRAT1', 'FXN']

for gene in genes:
    file_path = f"../sequences/{gene}"
    gene_complement = seq_complement(file_path)
    gene_sequence = seq_read_fasta(file_path)
    print(f"Gene {gene}:")

    # Create a fragment of the first 20 bases
    fragment = gene_sequence[:20]
    print(f"Frag: {fragment}")

    # Calculate and print the complement of the fragment
    fragment_complement = seq_complement(fragment)
    print("Comp:", fragment_complement)
    print("\n")