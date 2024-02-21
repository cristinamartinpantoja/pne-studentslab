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

    def count(self):
        if self.strbases == "" or self.strbases == "ERROR":
            return {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for base in self.strbases:
            if base in base_counts:
                base_counts[base] += 1
        return base_counts

    def reverse(self):
        if self.strbases == "" or self.strbases == "ERROR":
            return "ERROR"
        return self.strbases[::-1]

    def complement(self):
        if self.strbases == "" or self.strbases == "ERROR":
            return "ERROR"

        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_seq = ''.join([complement_dict[base] for base in self.strbases])
        return comp_seq

    def print_sequence(self, seq_number):
        print(f"Sequence {seq_number}: (Length: {len(self)}) {self.strbases}")
        bases_count = self.count()
        print(f"  Bases: {bases_count}")
        print(f"  Rev:   {self.reverse()}")
        print(f"  Comp:  {self.complement()}")



print("-----| Practice 1, Exercise 8 |------")

# Creating a null sequence
s1 = Seq()
s1.print_sequence(0)

# Creating a valid sequence
s2 = Seq("ACTGA")
s2.print_sequence(1)

# Creating an invalid sequence
s3 = Seq("Invalid sequence")
s3.print_sequence(2)