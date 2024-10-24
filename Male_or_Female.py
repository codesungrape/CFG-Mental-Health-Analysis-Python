import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint

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

#Create a pandas DataFrame with the counts
gender_data = pd.DataFrame({
    'Gender': ['Male', 'Female'],
    'Count': [male, female]
})

# Print the DataFrame to check the structure (optional)
print(gender_data)

# Create a barplot using seaborn
plt.figure(figsize=(6, 4))  # Optional: Set figure size
sns.barplot(x='Gender', y='Count', hue='Gender', data=gender_data, palette='Set2', legend=False)

# Add labels and title
plt.title('Count of Total Male vs Total Female Participants')
plt.xlabel('Gender')
plt.ylabel('Number of Participants')

# Display the plot
plt.show()




# Finding total depressed and gender difference count


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

depressed_participants = is_depressed()

#how many depressed participants are male vs female
def gender_difference_depressed(depressed_participants):
    depressed_participant_data = depressed_participants[-1] #get the depresses_participant list
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
    return {
        'male_count': male,
        'female_count': female,
        'male_participants': male_participants,
        'female_participants': female_participants
    }
depressed_gender_data = gender_difference_depressed(depressed_participants)
depressed_male_data = depressed_gender_data['male_participants']
depressed_female_data = depressed_gender_data['female_participants']

# Create a DataFrame for depressed participants
depressed_gender_data_df = pd.DataFrame({
    'Gender': ['Male', 'Female'],
    'Count': [depressed_gender_data['male_count'], depressed_gender_data['female_count']]
})

# Create a barplot for depressed participants
plt.figure(figsize=(6, 4))
sns.barplot(x='Gender', y='Count', hue="Gender", data=depressed_gender_data_df, palette='Set2')

# Add labels and title
plt.title('Count of Depressed Male vs Female Participants')
plt.xlabel('Gender')
plt.ylabel('Number of Depressed Participants')
plt.show() # Display the plot
