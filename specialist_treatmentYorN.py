import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "data/student_mental_health.csv"
data = pd.read_csv(file_path)

# Specify the questions of interest
questions = [
    'Did you seek any specialist for a treatment?',
    'Do you have Anxiety?',
    'Do you have Depression?',
    'Do you have Panic attack?'
]

# Count the responses for each question
response_counts = {}
for question in questions:
    response_counts[question] = data[question].value_counts()

# Convert the counts into a DataFrame for easier plotting and transpose the DataFrame to have questions as rows and responses as columns
response_df = pd.DataFrame(response_counts).fillna(0)  # Replace NaNs with 0
response_df = response_df.T

# Plot the data and titles
response_df.plot(kind='bar', figsize=(10, 6), color=['#BEC0E4', '#FF9999'], stacked=True)

plt.title('Participants Responses to Mental Health Questions')
plt.xlabel('Questions')
plt.ylabel('Number of Responses')
plt.xticks(rotation=45)
plt.legend(title="Responses", labels=["No", "Yes"])


plt.tight_layout() # Adjustments to layout
plt.show()
