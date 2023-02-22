import csv
    
def load_sequence_information(hamming_distances):
    with open("results.txt", "w") as f:
        for row in hamming_distances:
            row_values = list(row.values())
            f.write(f"{row_values[0]}\n")

            if row_values[3] is None:
                f.write(f"REVERSE:\n")
                f.write(f"{row_values[7]}\n")
                f.write(f"{row_values[8]}\n")
                f.write(f"{row_values[9]}\n")
                f.write(f"{row_values[10]}\n")
            else:
                f.write(f"FORWARD:\n")
                f.write(f"{row_values[3]}\n")
                f.write(f"{row_values[4]}\n")
                f.write(f"{row_values[5]}\n")
                f.write(f"{row_values[6]}\n")

            f.write("\n")
        
    with open("results.csv", "w+", newline="") as c:
        fieldnames = list(hamming_distances[0].keys())

        writer = csv.DictWriter(c, dialect="excel", fieldnames=fieldnames)

        writer.writeheader()
        for row in hamming_distances:
            writer.writerow(row)