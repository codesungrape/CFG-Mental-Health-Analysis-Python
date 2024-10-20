import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
plt.title('Count of Male vs Female Participants')
plt.xlabel('Gender')
plt.ylabel('Number of Participants')

# Display the plot
plt.show()