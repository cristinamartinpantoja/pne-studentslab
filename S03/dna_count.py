#S03 e2. Count the number of bases in a DNA sequence

valid_bases = {"A", "T", "G", "C"}
base_count = {"A":0, "G": 0, "C":0, "T":0}

sequence = input("Enter a valid sequence")
length_seq = len(sequence)
for base in sequence:
    if base in sequence:
        valid_bases[base] += 1
    if base not in sequence:
        print("invalid sequence")

print(length_seq)





