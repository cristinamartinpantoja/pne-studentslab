from pathlib import Path
class Seq:
    def __init__(self, seq):
        self.seq = seq

    def seq_len(self):
        return len(self.seq)

    def seq_count(self, b):
        base = self.seq.count(b)
        percentage = (base/len(self.seq) * 100)
        return str(base) + " (" + str(percentage) + "%)"

    def seq_complement(self):
        dict_of_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        my_seq = ""
        for i in self.seq:
            if i in dict_of_bases:
                my_seq += dict_of_bases[i]
        return my_seq

    def seq_reverse(self):
        seq1 = self.seq[::-1]
        reverse_seq = seq1[:self.seq_len()]
        return reverse_seq

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        lines = file_contents.split("\n")[1:]
        seq = "".join(lines)
        self.seq = seq
        return self.seq