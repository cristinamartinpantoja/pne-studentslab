from Seq0 import seq_count_bases

genes = ['U5', 'ADA', 'FRAT1', 'FXN']
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 5 |------")

for gene in genes:
    print(f"\nGene {gene}:")
    for base in bases:
        file_path = f"../sequences/{gene}"
        base_count = seq_count_bases(file_path, bases)
        print(f"  {base}: {base_count[base]}")