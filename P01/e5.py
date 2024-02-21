from Seq1 import Seq

def print_sequence(self, seq_number):
    print(f"Sequence {seq_number}: (Length: {self.seq_len()}) {self.strbases}")
    print(f"  A: {self.seq_count_base('A')},   C: {self.seq_count_base('C')},   T: {self.seq_count_base('T')},   G: {self.seq_count_base('G')}")



print("-----| Practice 1, Exercise 5 |------")

# Creating a null sequence
s1 = Seq()
print_sequence(s1, 0)

# Creating a valid sequence
s2 = Seq("ACTGA")
print_sequence(s2, 1)

# Creating an invalid sequence
s3 = Seq("Invalid sequence")
print_sequence(s3, 2)
