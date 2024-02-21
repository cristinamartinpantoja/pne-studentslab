from Seq1 import Seq

def print_sequence(seq, seq_number):
    print(f"Sequence {seq_number}: (Length: {seq.seq_len()}) {seq}")
    bases_count = seq.seq_count()
    print(f"  Bases: {bases_count}")


print("-----| Practice 1, Exercise 6 |------")

# Creating a null sequence
s1 = Seq()
print_sequence(s1, 0)

# Creating a valid sequence
s2 = Seq("ACTGA")
print_sequence(s2,1)

# Creating an invalid sequence
s3 = Seq("Invalid sequence")
print_sequence(s3, 2)
