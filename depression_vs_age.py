import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint

file_path = "data/student_mental_health.csv"
data = pd.read_csv(file_path)

age_vs_depression = data.groupby(['Age', 'Do you have Depression?']).size().unstack()

age_vs_depression.plot(kind="bar", figsize=(8,6), stacked=True, color=['#BEC0E4', '#FF9999'])

plt.title('Students ages and depression')
plt.xlabel('Age of Students')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.legend(title="Depression Status", labels=["No Depression", 'Depression'])

plt.tight_layout()
plt.show()


age_vs_depression = data.groupby(['Age', 'Do you have Depression?']).size().unstack()

age_vs_depression.plot(kind="bar", figsize=(8,6), stacked=True, color=['#BEC0E4', '#FF9999'])

plt.title('Students ages and depression')
plt.xlabel('Age of Students')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.legend(title="Depression Status", labels=["No Depression", 'Depression'])

plt.tight_layout()
plt.show()