import csv
import json
import os

def csv_to_json(path):
    result = {"adjectives": [], "verbs": [], "adverbs": [], "nouns": []}
    for folder in ["adjectives", "adverbs", "nouns", "verbs"]:
        items = os.listdir(f"{path}/{folder}/csv/")
        print(f"{folder}: ITEMS: {len(items)}")
        for file in os.listdir(f"{path}/{folder}/csv/"):
            pathfile = f"{path}/{folder}/csv/{file}"
            print(f"{folder} --> {pathfile}")
            
            with open(pathfile, 'r') as csv_file:
                # Read CSV data
                csv_data = csv.DictReader(csv_file, delimiter=';')
                # Convert CSV data to JSON
                print(csv_data)
                result[folder] += csv_data
    
    print(result)
    json_data = json.dumps(result, indent=4)
    
    # Write JSON data to a file
    with open("test_french_english.json", 'w') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    # CSV file path
    native = "french"
    to_learn = "english"

    # Convert CSV to JSON
    csv_to_json(f"{native}_{to_learn}")