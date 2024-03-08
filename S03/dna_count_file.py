def count_bases_in_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Initialize counts for each base
            counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
            total_length = 0

            # Iterate through each line in the file
            for line in file:
                # Iterate through each character in the line
                for base in line.strip():
                    # Increment the count for the current base
                    counts[base] += 1
                    total_length += 1

        # Display the results
        print("Total length:", total_length)
        for base, count in counts.items():
            print(f"{base}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Main program
file_path = "dna.txt"  # Provide the correct path to the file
count_bases_in_file(file_path)
