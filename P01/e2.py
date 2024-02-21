from Seq1 import Seq
def print_sequence(self):
    print("Sequence: ", self)


print("-----| Practice 1, Exercise 2 |------")
# Creating a null sequence
s1 = Seq()
print_sequence(s1)

# Creating a valid sequence
s2 = Seq("TATAC")
print_sequence(s2)

#Creating an invalid sequence
#s3 = Seq("ACTTGHH")
#s3.print_sequence()