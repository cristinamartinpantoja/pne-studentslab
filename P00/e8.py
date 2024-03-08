from Seq0 import most_frequent_base, seq_read_fasta

print("------| Exercise 8 |------")

genes = {'U5', 'ADA', 'FRAT1', 'FXN'}

for gene in genes:
    file_path = f"../sequences/{gene}"
    gene_most_frequent = most_frequent_base(file_path)
    gene_sequence = seq_read_fasta(file_path)

    most_frequent = most_frequent_base(gene_sequence)
    print(f"Gene {gene}: Most frequent Base: {most_frequent}")