import csv
    
def load_sequence_information(absolute_path, hamming_distances):
    path = absolute_path + "/db/"
    for segment_name in hamming_distances:
        segment = hamming_distances.get(segment_name) 
        for distance_rows_name in segment: 
            segment_path = path + segment_name + "/hamming_distance_results"
            with open(f"{segment_path}/{distance_rows_name}_results.csv", "w+", newline="") as c:
                distance_rows = segment.get(distance_rows_name)
                fieldnames = list(distance_rows[0].keys())

                writer = csv.DictWriter(c, dialect="excel", fieldnames=fieldnames)
                writer.writeheader()
                for row in distance_rows:
                        writer.writerow(row)