from Seq1 import Seq
def print_sequence(self):
    print(f"Sequence : (Length: {self.seq_len()}) {self.strbases}")
    bases_count = self.seq_count()
    print(f"  Bases: {bases_count}")
    print(f"  Rev:   {self.seq_reverse()}")
    print(f"  Comp:  {self.seq_complement()}")


print("-----| Practice 1, Exercise 9 |------")

# Creating a null sequence
s = Seq()

# Reading sequence from the "U5.txt" file
s.seq_read_fasta("U5")

# Printing sequence information
print_sequence(s)