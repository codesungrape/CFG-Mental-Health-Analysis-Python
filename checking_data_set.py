import csv
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt


#define file path
file_path = 'data/student_mental_health.csv'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = csv.DictReader(file)
    # Convert data to a list of dictionaries to print all rows
    data_list = list(data)  # This is indented because it's part of the `with` block
#pprint(data_list)


def get_age_21_data():
    age_21_data = []
    for participant in data_list:
        if participant['Age'] == '21':
            age_21_data.append(participant)

    pprint(age_21_data)

get_age_21_data()