#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('/Users/pamala/Documents/Project1/hospital_readmissions.csv')



# In[57]:


#Display headers in dataframe
df.head()
print(df.head(10))


# In[10]:


# Filter for readmitted patients
readmitted_data = df[df['readmitted'] == 'yes']

# Check for 'Diabetes' diagnosis whether primary, secondary or tertiary
diabetes_related_readmissions = readmitted_data[
    (readmitted_data['diag_1'].str.contains('Diabetes')) |
    (readmitted_data['diag_2'].str.contains('Diabetes')) |
    (readmitted_data['diag_3'].str.contains('Diabetes'))
]

# Print the count of diabetes-related readmissions
print(f"Number of diabetes-related readmissions: {diabetes_related_readmissions.shape[0]}")


# In[40]:


# Convert readmitted as a string
df['readmitted'] = df['readmitted'].astype(str).str.lower()

# Total number of admissions
total_admissions = df.shape[0]

# Counting readmissions
total_readmissions = df[df['readmitted'] == 'yes'].shape[0]

# Filtering for diabetes diagnoses in diag_1, diag_2, or diag_3 and determine total diabetes admissions
total_diabetes_admissions = df[(df['diag_1'].str.contains('Diabetes', na=False)) |
                               (df['diag_2'].str.contains('Diabetes', na=False)) |
                               (df['diag_3'].str.contains('Diabetes', na=False))].shape[0]

# Filter for readmissions with a diagnosis of diabetes
total_diabetes_readmissions = df[(df['readmitted'] == 'yes') &
                                 ((df['diag_1'].str.contains('Diabetes', na=False)) |
                                  (df['diag_2'].str.contains('Diabetes', na=False)) |
                                  (df['diag_3'].str.contains('Diabetes', na=False)))].shape[0]

# Display the results  (check work?)
print(f"Total Admissions: {total_admissions}")
print(f"Total Readmissions: {total_readmissions}")
print(f"Total Admissions with a Diagnosis of Diabetes: {total_diabetes_admissions}")
print(f"Total Readmissions with a Diagnosis of Diabetes: {total_diabetes_readmissions}")




# In[11]:


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


# In[12]:


#Identify admissions by diagnosis type
combined_diagnoses = pd.concat([df['diag_1'], df['diag_2'], df['diag_3']])
diagnosis_counts = combined_diagnoses.value_counts()
diagnosis_counts.plot(kind='bar')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.title('Distribution of Diagnoses')
plt.show()


# In[6]:


#distribution of age for general admission
age_counts = df['age'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Age Distribution')
plt.axis('equal')
plt.show()


# In[58]:


#distribution of age based on readmission
filtered_df = df[df['readmitted'] == 'yes']
age_counts = filtered_df['age'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=140)
plt.show()


# In[28]:


# Counting the occurrences of 'yes' and 'no' in the 'glucose_test' column
glucose_test_counts = df['glucose_test'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(glucose_test_counts, labels=glucose_test_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Glucose Monitoring Responses')
plt.show()



# In[20]:


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


# In[52]:


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

diabetic_patients = df[df['diabetes_med'] == 'yes'].copy()  
diabetic_patients.loc[:, 'outpatient_visit_category'] = pd.cut(diabetic_patients['n_outpatient'], bins=bins, labels=labels)



# In[31]:


# Counting the occurrences of 'yes' and 'no' in the 'A1ctest' column
A1C_counts = df['A1Ctest'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(A1C_counts, labels=A1C_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of A1C Results')
plt.show()


# In[60]:


# Increase the overall figure size
plt.figure(figsize=(20, 20))  # Width, height in inches

# Filter the DataFrame for relevant columns
data_subset = df[['n_medications', 'diag_1', 'diag_2', 'diag_3']]


# Plotting the first scatter plot in a more spacious configuration
plt.subplot(2, 2, 1)  # Changed grid to 2x2 and updated subplot positions
sns.scatterplot(data=data_subset, x='n_medications', y='diag_1')
plt.title('n_medications vs. diag_1')

# Plotting the second scatter plot
plt.subplot(2, 2, 2)
sns.scatterplot(data=data_subset, x='n_medications', y='diag_2')
plt.title('n_medications vs. diag_2')

plt.tight_layout()  # Adjust layout to make sure there is no overlap
plt.show()




# In[43]:


# Counting admissions based on primary, secondary, and tertiary diagnoses
primary_diagnoses = df['diag_1'].value_counts()
secondary_diagnoses = df['diag_2'].value_counts()
tertiary_diagnoses = df['diag_3'].value_counts()

# Visualize the top 10 primary diagnoses
plt.figure(figsize=(10, 6))
sns.barplot(x=primary_diagnoses.head(10).index, y=primary_diagnoses.head(10).values)
plt.title('Top 10 Primary Diagnoses for Patient Admissions')
plt.xlabel('Diagnosis Codes')
plt.ylabel('Number of Admissions')
plt.xticks(rotation=45)
plt.show()

# Similarly for secondary diagnoses
plt.figure(figsize=(10, 6))
sns.barplot(x=secondary_diagnoses.head(10).index, y=secondary_diagnoses.head(10).values)
plt.title('Top 10 Secondary Diagnoses for Patient Admissions')
plt.xlabel('Diagnosis Codes')
plt.ylabel('Number of Admissions')
plt.xticks(rotation=45)
plt.show()

# And tertiary diagnoses
plt.figure(figsize=(10, 6))
sns.barplot(x=tertiary_diagnoses.head(10).index, y=tertiary_diagnoses.head(10).values)
plt.title('Top 10 Tertiary Diagnoses for Patient Admissions')
plt.xlabel('Diagnosis Codes')
plt.ylabel('Number of Admissions')
plt.xticks(rotation=45)
plt.show()


# In[49]:


# Filter for readmitted cases
readmitted_df = df[df['readmitted'] == 'yes']# Identify diabetes diagnoses as primary, secondary, or tertiary
# Assuming 'Diabetes' is the keyword or diagnosis code for diabetes
primary_diabetes_readmissions = readmitted_df['diag_1'].str.contains('Diabetes', na=False).sum()
secondary_diabetes_readmissions = readmitted_df['diag_2'].str.contains('Diabetes', na=False).sum()
tertiary_diabetes_readmissions = readmitted_df['diag_3'].str.contains('Diabetes', na=False).sum()

# Visualizing the diabetes readmissions by diagnosis position
diagnosis_positions = ['Primary', 'Secondary', 'Tertiary']
readmission_counts = [primary_diabetes_readmissions, secondary_diabetes_readmissions, tertiary_diabetes_readmissions]

plt.figure(figsize=(8, 5))
sns.barplot(x=diagnosis_positions, y=readmission_counts)
plt.title('Readmissions for Diabetes by Diagnosis Position')
plt.xlabel('Diagnosis Position')
plt.ylabel('Number of Readmissions')
plt.show()

# Print the number of readmissions for each diagnosis position
print("Number of readmissions with diabetes as a primary diagnosis:", primary_diabetes_readmissions)
print("Number of readmissions with diabetes as a secondary diagnosis:", secondary_diabetes_readmissions)
print("Number of readmissions with diabetes as a tertiary diagnosis:", tertiary_diabetes_readmissions)


# In[50]:


# Identify non-diabetes diagnoses as primary, secondary, or tertiary
primary_non_diabetes_readmissions = readmitted_df[~readmitted_df['diag_1'].str.contains('Diabetes', na=False)].shape[0]
secondary_non_diabetes_readmissions = readmitted_df[~readmitted_df['diag_2'].str.contains('Diabetes', na=False)].shape[0]
tertiary_non_diabetes_readmissions = readmitted_df[~readmitted_df['diag_3'].str.contains('Diabetes', na=False)].shape[0]

# Print the number of readmissions for each non-diabetes diagnosis position
print("Number of readmissions without diabetes as a primary diagnosis:", primary_non_diabetes_readmissions)
print("Number of readmissions without diabetes as a secondary diagnosis:", secondary_non_diabetes_readmissions)
print("Number of readmissions without diabetes as a tertiary diagnosis:", tertiary_non_diabetes_readmissions)

# Visualizing the non-diabetes readmissions by diagnosis position
diagnosis_positions = ['Primary', 'Secondary', 'Tertiary']
readmission_counts = [primary_non_diabetes_readmissions, secondary_non_diabetes_readmissions, tertiary_non_diabetes_readmissions]

plt.figure(figsize=(8, 5))
sns.barplot(x=diagnosis_positions, y=readmission_counts)
plt.title('Readmissions without Diabetes by Diagnosis Position')
plt.xlabel('Diagnosis Position')
plt.ylabel('Number of Readmissions')
plt.show()


# In[51]:


# Filter for readmitted cases
readmitted_df = df[df['readmitted'] == 'yes']

# Identifying readmissions where diabetes is mentioned in any of the three diagnosis positions
diabetes_readmissions = readmitted_df[
    readmitted_df['diag_1'].str.contains('Diabetes', na=False) |
    readmitted_df['diag_2'].str.contains('Diabetes', na=False) |
    readmitted_df['diag_3'].str.contains('Diabetes', na=False)
]

# Calculate the total number of readmissions
total_readmissions = readmitted_df.shape[0]

# Calculate the number of diabetes-related readmissions
diabetes_related_readmissions = diabetes_readmissions.shape[0]

# Calculate the likelihood (percentage) of readmissions where diabetes is a factor
likelihood_diabetes_readmission = (diabetes_related_readmissions / total_readmissions) * 100

# Print the results
print(f"Total number of readmissions: {total_readmissions}")
print(f"Number of diabetes-related readmissions: {diabetes_related_readmissions}")
print(f"Likelihood of diabetes being a factor in readmissions: {likelihood_diabetes_readmission:.2f}%")


# In[55]:


# Filter for patients with a diabetes diagnosis
diabetes_cases = df[
    df['diag_1'].str.contains('Diabetes', na=False) |
    df['diag_2'].str.contains('Diabetes', na=False) |
    df['diag_3'].str.contains('Diabetes', na=False)
]

# Further filter for those who were readmitted
diabetes_readmitted = diabetes_cases[diabetes_cases['readmitted'] == 'yes']

# Summarize the total number of inpatient visits before the current admission for these patients
total_inpatient_visits = diabetes_readmitted['n_inpatient'].sum()

# Average number of inpatient visits
average_inpatient_visits = diabetes_readmitted['n_inpatient'].mean()

# Print the results
print(f"Total inpatient visits before admission for readmitted diabetes patients: {total_inpatient_visits}")
print(f"Average inpatient visits before admission for readmitted diabetes patients: {average_inpatient_visits:.2f}")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(diabetes_readmitted['n_inpatient'], bins=20, kde=True)
plt.title('Distribution of Inpatient Visits for Readmitted Diabetes Patients')
plt.xlabel('Number of Inpatient Visits')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




