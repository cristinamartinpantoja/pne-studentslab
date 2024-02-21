from Seq1 import seq_len

class SequenceObject:
    def __init__(self, sequence):
        self.sequence = "ACTGA"

    def seq_info(self):
        print("Sequence: ", self.sequence)
        print("Length: ", len(self.sequence))

# Creating an object with the sequence "ACTGA"
sequence_object = SequenceObject("ACTGA")

# Printing length and sequence information
print("-----| Practice 1, Exercise 1 |------")
sequence_object.seq_info()