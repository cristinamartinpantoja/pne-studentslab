from Seq1 import Seq

SEQUENCES = "../sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Practice 1, Exercise 10 |------")
for g in GENES:
    file = SEQUENCES + g
    s = Seq()
    s.seq_read_fasta(file)
    print("Gene", g, ": Most frequent Base:", s.most_frequent_base(), sep='')