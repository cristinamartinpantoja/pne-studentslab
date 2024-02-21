from Seq1 import Seq

def seq_info(seq):
    print("Sequence: ", seq)
    print("Length: ", seq.seq_len())

# Creating an object with the sequence "ACTGA"
sequence_object = Seq("ACTGA")

# Printing length and sequence information
print("-----| Practice 1, Exercise 1 |------")
seq_info(sequence_object)