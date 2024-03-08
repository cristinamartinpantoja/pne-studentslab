from Seq0 import seq_read_fasta
FOLDER = "../sequences/"

FILENAME = "U5"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene U5 ->" , len(sequence))

FILENAME = "ADA"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene ADA ->" ,len(sequence))

FILENAME = "FXN"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene FXN ->" ,len(sequence))

FILENAME = "FRAT1"
sequence = seq_read_fasta(FOLDER + FILENAME)
print("Gene FRAT1 ->" ,len(sequence))

"""
from Seq0 import seq_len, seq_read_fasta

genes = ["U5", "ADA", "FRAT1", "FXN"]

for gene in genes:
    file_path = f"../sequences/{gene}"
    gene_counts = seq_len(file_path)
    print(f"{gene}:" , gene_counts)
"""