from Seq1 import Seq


def print_sequence(self):
    print("Sequence: ", "Length:", len(self.strbases), self.strbases)

print("-----| Practice 1, Exercise 4 |------")

# Creating a null sequence
s1 = Seq()
print_sequence(s1)

# Creating a valid sequence
s2 = Seq("ACTGA")
print_sequence(s2)

# Creating an invalid sequence
s3 = Seq("ACTTGHH")
print_sequence(s3)