from pathlib import Path

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

    def seq_read_fasta(self, filename):
        first_line = Path(filename).read_text().find("\n")
        body = Path(filename).read_text()[first_line:]
        body = body.replace("\n", "")
        self.strbases = body
        return body
    def __str__(self):
        return self.strbases
    def seq_len(self):
        return len(self.strbases)

    def seq_count_base(self, base):
        return self.strbases.count(base)

    def seq_count(self):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for base in bases.keys():
            count = self.seq_count_base(base)
            bases.update({base:count})
        return bases

    def reverse(self):
        if self.strbases == None:
            return "NULL"
        else:
            for i in self.strbases:
                if i == "A" or i == "C" or i == "T" or i == "G":
                    seq_n = self.strbases[:len(self.strbases)]
                    return seq_n[::-1]
                else:
                    return "ERROR"

    def seq_complement(self):
        complement = ""
        if self.strbases == None:
            return "NULL"
        else:
            for base in self.strbases:
                if base == "A":
                    complement += "T"
                elif base == "G":
                    complement += "C"
                elif base == "C":
                    complement += "G"
                elif base == "T":
                    complement += "A"
                else:
                    return "ERROR"
        return complement

    def seq_check(self):
        seq = self.strbases.upper()
        bases = ["A", "T", "C", "G"]

        for i in seq:
            if i not in bases:
                return "Not valid"

    def most_frequent_base(self):
        seq = self.strbases
        bases_count = {'A': 0, 'G': 0, 'C': 0, 'T': 0}

        for base in seq:
            if base in bases_count:
                bases_count[base] += 1

        most_common = max(bases_count, key=bases_count.get)

        return most_common