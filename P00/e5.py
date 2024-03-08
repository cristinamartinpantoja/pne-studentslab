from Seq0 import seq_count

genes = ['U5', 'ADA', 'FRAT1', 'FXN']

print("-----| Exercise 5 |------")

for gene in genes:
    file_path = f"../sequences/{gene}"
    gene_counts = seq_count(file_path)

    print(f"Gene {gene}: {gene_counts}")