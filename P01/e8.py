from Seq1 import Seq

def print_sequence(self, seq_number):
    print(f"Sequence {seq_number}: (Length: {self.seq_len()}) {self.strbases}")
    bases_count = self.seq_count()
    print(f"  Bases: {bases_count}")
    print(f"  Rev:   {self.seq_reverse()}")
    print(f"  Comp:  {self.seq_complement()}")



print("-----| Practice 1, Exercise 8 |------")

# Creating a null sequence
s1 = Seq()
print_sequence(s1, 0)

# Creating a valid sequence
s2 = Seq("ACTGA")
print_sequence(s2, 1)

# Creating an invalid sequence
s3 = Seq("Invalid sequence")
print_sequence(s3, 2)