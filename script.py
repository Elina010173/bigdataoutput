import csv
import json

# Replace these paths with the paths to your CSV and JSON files
csv_file_path = 'input.csv'  # Path to the CSV file
json_file_path = 'output.json'  # Path to the JSON file to save the serialized data

data = []  # Create an empty list to store the serialized objects

# Open the CSV file and read its contents
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the CSV and serialize it as a dictionary
    for row in csv_reader:
        # Assuming each row in the CSV represents an object, you can further customize this serialization process
        # For example, you may want to convert specific fields to different data types or manipulate the data
        serialized_object = {
            'field1': row['Column1'],  # Replace 'Column1' with the actual column name
            'field2': row['Column2'],  # Replace 'Column2' with the actual column name
            # Add more fields as needed
        }
        
        data.append(serialized_object)

# Serialize the list of objects to JSON
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f'Serialization completed. Data saved to {json_file_path}')
