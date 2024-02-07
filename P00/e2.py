from Seq0 import seq_read_fasta
FOLDER = "../sequences/"
FILENAME = "U5"

sequence = seq_read_fasta(FOLDER + FILENAME)
print(sequence[0:20])

