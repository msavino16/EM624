# Author:  Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

# Exercise 05
# Pandas program

# This program will intake a file and convert it to pandas dataframes

# The program is written by loading in each dataset, then doing data manipulation and creating charts

#Import the required libraries
from matplotlib import pyplot as plt
import pandas as pd

print ("\n run by Michael Savino")
print ()

#Read the data file into a pandas data structure.
covid_df = pd.read_csv('covid_comorbidities_USsummary.csv')

#Remove records with "Age Group" equal to either 'Not stated' or 'All Ages'.
covid_df = covid_df[~covid_df['Age Group'].isin(['Not stated', 'All Ages'])]

#Remove records with "Condition" equal to COVID-19.
covid_df = covid_df[covid_df['Condition'] != 'COVID-19']

#Remove the columns "Condition Group", "ICD10_codes", "Number of Mentions".
covid_df = covid_df.drop(['Condition Group', 'ICD10_codes', 'Number of Mentions'], axis=1)

#Perform the exploratory analysis, after doing the proper recoding of the variables
age_group_mapping = {
    '0-24': 1, 
    '25-34': 2, 
    '35-44': 3, 
    '45-54': 4,
    '55-64': 5, 
    '65-74': 6, 
    '75-84': 7, 
    '85+': 8
}
covid_df['Age_Group_Numeric'] = covid_df['Age Group'].map(age_group_mapping)
covid_df['Condition_Numeric'] = pd.Categorical(covid_df['Condition']).codes

print("COVID-19 Deaths Distribution:")
print(covid_df['COVID-19 Deaths'].describe())
print()

print("Age Group Distribution:")
print(covid_df['Age Group'].describe())
print()

print("Condition Distribution:")
print(covid_df['Condition'].describe())

print()
numeric_cols = ['Age_Group_Numeric', 'Condition_Numeric', 'COVID-19 Deaths']
correlation_matrix = covid_df[numeric_cols].corr()
print("Correlation Matrix:")
print(correlation_matrix)

print()
print("Variable Values Distribution:")

print()
print("Age Group Distribution:")
age_dist = covid_df['Age Group'].value_counts()
print(age_dist)

print()
print("COVID-19 Deaths Distribution by Age Group:")
deaths_by_age = covid_df.groupby('Age Group')['COVID-19 Deaths'].sum().sort_values(ascending=False)
print(deaths_by_age)

print()
print("Missing Values:")
print(covid_df.isnull().sum())

#Bar Chart
plt.figure(figsize=(12, 8))
plt.subplot(221)
condition_deaths = covid_df.groupby('Condition')['COVID-19 Deaths'].sum().sort_values(ascending=False).head(5)
plt.bar(condition_deaths.index, condition_deaths.values)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.title('Top 5 Conditions by COVID-19 Deaths')


#Pie Chart
plt.subplot(222)
deaths_by_age_pie = covid_df.groupby('Age Group')['COVID-19 Deaths'].sum()
total_deaths = deaths_by_age_pie.sum()
percentages = []
for x in deaths_by_age_pie:
    percentage = (x/total_deaths)*100
    formatted_pct = f'{percentage:.1f}%'
    percentages.append(formatted_pct)
plt.pie(deaths_by_age_pie, labels=deaths_by_age_pie.index, autopct='%1.1f%%')
plt.title('Distribution of COVID-19 Deaths by Age Group')

plt.show()

#the comorbidity with the highest number of deaths for the population of less than 25 years of age
print()
print("Analysis for population under 25 years:")
under_25_data = covid_df[covid_df['Age Group'] == '0-24']
highest_comorbidity = under_25_data.nlargest(1, 'COVID-19 Deaths')
print()
print(f"Comorbidity with highest deaths for under 25: {highest_comorbidity['Condition'].iloc[0]}")
print(f"Number of deaths: {highest_comorbidity['COVID-19 Deaths'].iloc[0]}")

#the percentage of the total deaths this comorbidity represents for the total deaths in the same population
total_deaths_under_25 = under_25_data['COVID-19 Deaths'].sum()
percentage = (highest_comorbidity['COVID-19 Deaths'].iloc[0] / total_deaths_under_25) * 100
print(f"Percentage of total deaths under 25: {percentage:.1f}%")



print('\nThanks for using this tool!\n')
 