from Seq0 import seq_read_fasta
FOLDER = "../sequences/"

FILENAME = "FRAT1"
sequence = seq_read_fasta(FOLDER + FILENAME)

counta = 0
countc = 0
countt = 0
countg = 0

for i in sequence:
    if i == "A":
        counta += 1
    if i == "C":
        countc += 1
    if i == "T":
        countt += 1
    if i == "G":
        countg += 1

print("Gene FRAT1:")
print("A:", counta)
print("C:", countc)
print("T:", countt)
print("G:", countg)

FILENAME = "U5"
sequence = seq_read_fasta(FOLDER + FILENAME)

counta = 0
countc = 0
countt = 0
countg = 0

for i in sequence:
    if i == "A":
        counta += 1
    if i == "C":
        countc += 1
    if i == "T":
        countt += 1
    if i == "G":
        countg += 1

print("Gene U5:")
print("A:", counta)
print("C:", countc)
print("T:", countt)
print("G:", countg)

print("Así con todos")