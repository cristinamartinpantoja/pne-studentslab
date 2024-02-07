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