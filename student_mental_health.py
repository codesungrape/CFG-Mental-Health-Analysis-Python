import csv
from pprint import pprint
from collections import Counter

#define file path
file_path = 'data/student_mental_health.csv'

# Function to read CSV data
def read_data():
    data = []
    with open(file_path, 'r') as file:
        spreadsheet = csv.DictReader(file)
        for row in spreadsheet:
            data.append(row)
    return data

#save data to spreadsheet_data variable
spreadsheet_data = read_data()

# In this section, there are functions to find general information from ALL data

#function to return max and min age of chosen participant
def find_max_min_age(spreadsheet_data):
    ages = []

    for participant in spreadsheet_data:
        age_str = participant.get("Age", "").strip() ## Get the "Age" field, handle missing or empty values

        # Check if the age field is not empty before converting to integer
        if age_str.isdigit(): # Check if it's a valid number
            ages.append(int(age_str))
    if ages:
        max_age = max(ages)
        min_age = min(ages)
        print(f"The oldest age of participants is {max_age} and the youngest age of participants is {min_age}")
        return [max_age, min_age, ages, len(ages)]
    else:
        print("No valid age data available.")
        return None

# Call the function with spreadsheet_data passed in/use destructuring to save returned values into variables
[max_age, min_age, ages, ages_length] = find_max_min_age(spreadsheet_data)
#print(ages)


#function to find complete data of one participant
def participant_data(spreadsheet_data):
    # Get participant number from the user
    chosen_participant_number = int(input("Which participant do you want to check (must be integer between 1-101 (inclusive))? "))
    if 1 <= chosen_participant_number <= 101:
        chosen_participant = spreadsheet_data[chosen_participant_number - 1]
        pprint(chosen_participant)
    else:
        print("Please enter a number between 1 and 101.")

participant_data(spreadsheet_data)


#Function to check how many participants identify as male vs identify as female
def male_or_female():
    male = 0
    female = 0

    for participant in spreadsheet_data:
        gender = participant.get("Choose your gender", "").strip()
        if gender == 'Male':
            male+= 1
        elif gender == 'Female':
            female += 1

    total_participants = male + female
    print(f"There are {male} male participants and {female} female participants. This is out of {total_participants} participants")
    return [male, female] #using destructuring to save values to variables

[male, female] = male_or_female() #using destructuring to save values to variables
# print(male)
# print(female)

def what_year():
    male_year = []
    total_male_data = []
    female_year = []
    total_female_data = []

    for participant in spreadsheet_data:
        gender_str = participant.get("Choose your gender", "").strip().title()
        gender_year = participant.get("Your current year of Study").strip().title()
        if gender_str == "Male":
            male_year.append(gender_year)
            total_male_data.append(participant)
        elif gender_str == "Female":
            female_year.append(gender_year)
            total_female_data.append(participant)
    # Count how many males and females are in what year
    count_male_year = Counter(male_year)
    count_female_year = Counter(female_year)

    print(f"There are {len(spreadsheet_data)} participants of whom {len(total_male_data)} are Male and they are in the following years {count_male_year}")
    print(f"There are {len(spreadsheet_data)} participants of whom {len(total_female_data)} are Female and they are in the following years {count_female_year}")
    return [male_year, total_male_data, female_year, total_female_data]

#call what_year() function to see print statements
what_year()




# From this sections onwards, I have more specific data, or split original data into subsets


#function to find total number of participants who said they felt depressed, separate participants who feel depressed from those that dont and save into a smaller spreadsheet data variable
def is_depressed():
    ans_yes = 0
    ans_no = 0
    depressed_participants = []

    for participant in spreadsheet_data:
        answer_str1 = participant.get("Do you have Depression?", "").strip()
        if answer_str1 == 'Yes':
            ans_yes += 1
            depressed_participants.append(participant)
        elif answer_str1 == 'No':
            ans_no += 1

    percentage_depressed = round((ans_yes/len(spreadsheet_data)) * 100, 2)
    print(f"Total of participants who answered 'Yes' to feeling depressed is {ans_yes} and 'No' to feeling depressed is {ans_no}. This is a {percentage_depressed}% of participants who indentify as being depressed.")
    return [ans_yes, ans_no, depressed_participants]

result = is_depressed()
#pprint(result)


#how many depressed participants are male vs female
def gender_difference_depressed(result):
    depressed_participant_data = result[-1] #get the depresses_participant list
    male = 0
    female = 0
    male_participants = []
    female_participants = []

    for participant in depressed_participant_data:
        gender = participant.get("Choose your gender", "").strip()
        if gender == 'Male':
            male += 1
            male_participants.append(participant)
        elif gender == 'Female':
            female += 1
            female_participants.append(participant)
    print(f"There are {male} male participant who identified as depressed and {female} female participants")
    return [male, female, male_participants, female_participants]  # using destructuring to save values to variables

depressed_gender_data = gender_difference_depressed(result)
depressed_male_data = depressed_gender_data[2]
depressed_female_data = depressed_gender_data[-1]
#pprint(depressed_male_data)



# explore depressed male data
def depressed_male_data_values(depressed_male_data, depressed_female_data):

    study_year_male = []
    study_year_female = []

    for participant in depressed_male_data:
        year = participant.get("Your current year of Study", "").strip().title()
        study_year_male.append(year)
    for participant in depressed_female_data:
        year = participant.get("Your current year of Study", "").strip().title()
        study_year_female.append(year)

    # Extrapolate how many are in each year
    count_male_year = Counter(study_year_male)
    count_female_year = Counter(study_year_female)


    print(f"There are {len(study_year_male)} and they are in {count_male_year}")
    print(f"There are {len(study_year_female)} and they are in {count_female_year}")



    return [study_year_male, study_year_female]


[male_year_data, female_year_data] = depressed_male_data_values(depressed_male_data, depressed_female_data)




