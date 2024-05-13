#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load the data
df = pd.read_csv('/Users/pamala/Documents/Project1/hospital_readmissions.csv')



# In[6]:


df.head()


# In[7]:


# Filter for readmitted patients
readmitted_data = df[df['readmitted'] == 'yes']

# Check for 'Diabetes' diagnosis in any of the three diagnostic columns
diabetes_related_readmissions = readmitted_data[
    (readmitted_data['diag_1'].str.contains('Diabetes')) |
    (readmitted_data['diag_2'].str.contains('Diabetes')) |
    (readmitted_data['diag_3'].str.contains('Diabetes'))
]

# Print the count of diabetes-related readmissions
print(f"Number of diabetes-related readmissions: {diabetes_related_readmissions.shape[0]}")


# In[8]:


import matplotlib.pyplot as plt
# Assuming you have a DataFrame named df containing the data
# df = pd.read_csv("your_data.csv")
# Grouping the data by age and calculating the average time_in_hospital for each age group
avg_time_in_hospital_by_age = df.groupby('age')['time_in_hospital'].mean()
# Plotting a bar chart
plt.figure(figsize=(12, 6))
avg_time_in_hospital_by_age.plot(kind='bar', color='skyblue')
plt.title('Average Time in Hospital by Age')
plt.xlabel('Age')
plt.ylabel('Average Time in Hospital')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[10]:


import matplotlib.pyplot as plt

# Assuming df is your previously loaded DataFrame
combined_diagnoses = pd.concat([df['diag_1'], df['diag_2'], df['diag_3']])
diagnosis_counts = combined_diagnoses.value_counts()
diagnosis_counts.plot(kind='bar')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.title('Distribution of Diagnoses')
plt.show()


# In[16]:


age_counts = hospital_admissions_df['age'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Age Distribution')
plt.axis('equal')
plt.show()


# In[19]:


filtered_df = hospital_admissions_df[hospital_admissions_df['readmitted'] == 'yes']
age_counts = filtered_df['age'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct=‘%1.1f%%’, startangle=140)
plt.title(‘Pie Chart of Age Distribution’)
plt.axis(‘equal’)
plt.show()


# In[22]:


import matplotlib.pyplot as plt

# Counting the occurrences of 'yes' and 'no' in the 'glucose_test' column
glucose_test_counts = df['glucose_test'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(glucose_test_counts, labels=glucose_test_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Glucose Monitoring Responses')
plt.show()



# In[23]:


# Filter the DataFrame for patients with diabetes who were readmitted
diabetes_readmitted_outpatient = df[
    (df['diabetes_med'] == 'yes') &  # Patients on diabetic medication
    (df['readmitted'] == 'yes') &    # Patients who were readmitted
    (df['n_outpatient'] > 0)         # Patients with outpatient visits in the year preceding their hospital stay
]

# Count the patients meeting the criteria
patient_count = diabetes_readmitted_outpatient.shape[0]

# Display the results
print(f"Number of patients diagnosed with diabetes who were readmitted and had outpatient visits in the year preceding their admission: {patient_count}")


# In[27]:


import matplotlib.pyplot as plt
import pandas as pd

# Filter the DataFrame for patients with diabetes medication
diabetic_patients = df[df['diabetes_med'] == 'yes']

# Define bins for the number of outpatient visits
bins = [-1, 0, 3, 6, float('inf')]
labels = ['0 visits', '1-3 visits', '4-6 visits', '7+ visits']

# Categorize the number of outpatient visits
diabetic_patients['outpatient_visit_category'] = pd.cut(diabetic_patients['n_outpatient'], bins=bins, labels=labels)

# Calculate readmission rates by category
readmission_rates = diabetic_patients.groupby('outpatient_visit_category')['readmitted'].value_counts(normalize=True).unstack().fillna(0)

# Plotting the results
fig, ax = plt.subplots(figsize=(10, 6))
readmission_rates.plot(kind='bar', stacked=True, ax=ax)
ax.set_ylabel('Proportion of Patients')
ax.set_title('Readmission Rates by Outpatient Visit Categories')
ax.legend(title='Readmitted')
plt.show()


# In[28]:


import matplotlib.pyplot as plt

# Counting the occurrences of 'yes' and 'no' in the 'A1ctest' column
A1C_counts = df['A1Ctest'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(A1C_counts, labels=A1C_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of A1C Results')
plt.show()


# In[ ]:




