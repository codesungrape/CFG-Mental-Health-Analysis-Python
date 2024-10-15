import csv
import json
from pprint import pprint

#define file path
file_path = 'data/student_mental_health.csv'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = csv.DictReader(file)

pprint(data)