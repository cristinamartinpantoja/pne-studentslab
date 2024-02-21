class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL Seq created")
            self.strbases = ""
            return

        valid_bases = set('ATCG')
        if set(strbases) <= valid_bases:
            print("New sequence created!")
            self.strbases = strbases
        else:
            print("INVALID sequence!")
            self.strbases = "ERROR"

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

    def read_fasta(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Concatenate all lines after the first one (ignoring the '>' line)
            fasta_sequence = ''.join(lines[1:])
            # Remove newline characters from the concatenated sequence
            fasta_sequence = fasta_sequence.replace('\n', '')
            self.strbases = fasta_sequence

    def print_sequence(self):
        print(f"Sequence : (Length: {len(self)}) {self.strbases}")
        bases_count = self.count()
        print(f"  Bases: {bases_count}")
        print(f"  Rev:   {self.reverse()}")
        print(f"  Comp:  {self.complement()}")


# Main program
if __name__ == "__main__":
    print("-----| Practice 1, Exercise 9 |------")

    # Creating a null sequence
    s = Seq()

    # Reading sequence from the "U5.txt" file
    s.read_fasta("U5")

    # Printing sequence information
    s.print_sequence()