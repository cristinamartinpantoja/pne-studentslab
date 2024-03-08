#S03 e2. Count the number of bases in a DNA sequence

def count_bases(sequence):
    # Initialize counts for each base
    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

    # Iterate through each character in the sequence
    for base in sequence:
        # Increment the count for the current base
        counts[base] += 1

    # Calculate the total length of the sequence
    total_length = len(sequence)

    # Display the results
    print("Total length:", total_length)
    for base, count in counts.items():
        print(f"{base}: {count}")


# Main program
user_sequence = input("Introduce the sequence: ")
count_bases(user_sequence)




