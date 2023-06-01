import os
import json
import csv
from pathlib import Path

def main():
    path = "./db"

    with open("./results_configuration.json", "r") as json_file:
        json_config = dict(json.load(json_file))


    for segment in os.scandir(path):
        if (segment.is_dir()):
            hamming_distance_results_path = path + "/" + segment.name + "/hamming_distance_results"
            forward_dictionary = {}

            reverse_dictionary = {}

            for hamming_distance_results_csv in os.scandir(hamming_distance_results_path):

                subtypes = json_config.get(segment.name, [])
                for_dict = parse_csv(path, segment.name, subtypes, hamming_distance_results_csv.name, "Forward")
                rev_dict = parse_csv(path, segment.name, subtypes, hamming_distance_results_csv.name, "Reverse")

                forward_dictionary = combine_dictionarioes(forward_dictionary, for_dict)

                reverse_dictionary = combine_dictionarioes(reverse_dictionary, rev_dict)

                if len(for_dict) > 0:
                    print(hamming_distance_results_csv.name)
                    print(for_dict)
                    print(forward_dictionary)

                if len(rev_dict) > 0:
                    print(hamming_distance_results_csv.name)
                    print(rev_dict)
                    print(reverse_dictionary)

            write_csv(path, segment.name, "Forward", forward_dictionary)
            write_csv(path, segment.name, "Reverse", reverse_dictionary)

def combine_dictionarioes(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value

    return dict1

def parse_csv(path, segment, subtypes, csv_filename, direction):

    version_key = "forward_version" if direction == "Forward" else "reverse_version"

    dictionary = {}
    for subtype in subtypes:
        forward_version = subtypes.get(subtype).get(version_key) 
        if (subtype in csv_filename and forward_version in csv_filename and direction in csv_filename):
            with open(path + "/" + segment + "/hamming_distance_results/" + csv_filename, newline='') as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    hamming_distance = row[3]
                    if (hamming_distance == "hamming_distance"):
                        continue

                    if hamming_distance in dictionary:
                        dictionary[hamming_distance] += 1
                    else:
                        dictionary[hamming_distance] = 1

    return dictionary


def write_csv(path, segment, direction, dictionary):
    result_path = f"{path}/{segment}/hamming_culmination"
    Path(result_path).mkdir(parents=True, exist_ok=True)

    with open(f"{result_path}/{segment}_{direction}.csv", "w+") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["hamming_distance", "count"])
        for key, value in dictionary.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    main()
