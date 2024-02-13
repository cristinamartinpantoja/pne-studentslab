from pathlib import Path

def seq_read_fasta(filename):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return body
def seq_len(filename):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    return len(body)

def seq_count_base(filename, base):
    first_line = Path(filename).read_text().find("\n")
    body = Path(filename).read_text()[first_line:]
    body = body.replace("\n", "")
    base = len(body)
    return base

def seq_count(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}
    for base in bases:
        count = seq_count_base(seq, base)
        bases.update({base:count})
    return bases
def seq_reverse(seq, n=0):
    seq = seq[::-1]
    return seq[:n]
def seq_complement(seq):
    dict_of_bases = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in seq:
        if i in dict_of_bases:
            print(dict_of_bases[i], end = "")

def seq_check(seq):
    seq = seq.upper()
    bases = ["A", "T", "C", "G"]

    for i in seq:
        if i not in bases:
            return "Not valid"
