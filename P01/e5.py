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

    def __len__(self):
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def print_sequence(self, seq_number):
        print(f"Sequence {seq_number}: (Length: {len(self)}) {self.strbases}")
        print(f"  A: {self.count_base('A')},   C: {self.count_base('C')},   T: {self.count_base('T')},   G: {self.count_base('G')}")



print("-----| Practice 1, Exercise 5 |------")

# Creating a null sequence
s1 = Seq()
s1.print_sequence(0)

# Creating a valid sequence
s2 = Seq("ACTGA")
s2.print_sequence(1)

# Creating an invalid sequence
s3 = Seq("Invalid sequence")
s3.print_sequence(2)
