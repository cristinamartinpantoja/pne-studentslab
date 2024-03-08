from pathlib import Path

def seq_ping():
    print("Testing the seq_ping function")
    print("OK!")
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

def seq_count_bases(file_path, bases):
    try:
        with open(file_path, 'r') as file:
            gene_sequence = file.read()
            base_counts = {base: gene_sequence.count(base) for base in 'ACTG'}
            return base_counts
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def seq_count(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}
    for base in bases:
        count = seq_count_bases(seq, bases)
        bases.update({base:count})
    return bases

def seq_reverse(sequence):
    return sequence[::-1]

def seq_complement(seq):
    dict_of_bases = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in seq:
        if i in dict_of_bases:
            print(dict_of_bases[i], end = "")


def most_frequent_base(sequence):
    base_counts = {}
    for base in sequence:
        base_counts[base] = base_counts.get(base, 0) + 1

    most_frequent_base = max(base_counts, key=base_counts.get)
    return most_frequent_base

def seq_check(seq):
    seq = seq.upper()
    bases = ["A", "T", "C", "G"]

    for i in seq:
        if i not in bases:
            return "Not valid"