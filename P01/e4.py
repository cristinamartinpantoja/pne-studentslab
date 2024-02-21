class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = ""

            return

        valid_bases = set('ATCG')
        if set(strbases) <= valid_bases:
            print("New sequence created!")
            self.strbases = strbases
        else:
            print("INVALID sequence!")
            self.strbases = ""

    def print_sequence(self):
        print("Sequence: ", "Length:", len(self.strbases), self.strbases)

print("-----| Practice 1, Exercise 4 |------")

# Creating a null sequence
s1 = Seq()
s1.print_sequence()

# Creating a valid sequence
s2 = Seq("ACTGA")
s2.print_sequence()

# Creating an invalid sequence
s3 = Seq("ACTTGHH")
s3.print_sequence()