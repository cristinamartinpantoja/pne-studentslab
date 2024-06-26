#otra forma de hacer la Seq0 aparte de la que ya tengo
from pathlib import Path
def seq_ping():
    print("OK")
def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    seq = Path(filename).read_text()[first_line:]
    seq = seq.replace("\n", "")
    return seq
def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count
def seq_count(seq):
    dic = {"A": 0, "C": 0, "T": 0, "G": 0}
    for i in seq:
        if i in dic:
            dic[i] +=1
    return dic
def seq_reverse(seq, n=0):
    return seq[::-1]
def seq_complement(seq):
    complement = ""
    for i in seq:
        if i == "A":
            complement += "T"
        elif i == "T":
            complement += "A"
        elif i == "C":
            complement += "G"
        elif i == "G":
            complement += "C"
    return complement

def seq_check(seq):
    seq = seq.upper()
    bases = ["A", "T", "C", "G"]

    for i in seq:
        if i not in bases:
            return "Not valid"