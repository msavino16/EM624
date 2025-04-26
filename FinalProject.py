#Author: Michael Savino

#"I pledge my honor that I have abided by the Stevens Honor System"

#Final Project
#Suicide Data Analysis Program

#This program will analyze 2012-2014 suicide data with visuals and statistics

#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print()
print("Suicide Data Analysis")
print()
#load the data
suicide_stats = pd.read_csv('full_data.csv')

#remove all non-suicide cases and police column
suicide_stats = suicide_stats[suicide_stats['intent'] == 'Suicide']
suicide_stats = suicide_stats.drop('police', axis=1)

#basic data statistics
print("Descriptive Statistics:")
print(suicide_stats.describe())
print()
print("Total number of records:", len(suicide_stats))

#cases per year
print()
print("Cases per year:")
yearly_stats = suicide_stats.groupby('year').size()
for year, count in yearly_stats.items():
    print(f"{year}: {count} cases ({(count/len(suicide_stats)*100):.2f}%)")

#ages graph
plt.figure(figsize=(12, 6))
sns.histplot(data=suicide_stats, x='age', bins=30, kde=True)
plt.title('Age distribution of suicide cases')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#race graph
plt.figure(figsize=(12, 6))
race_counts = suicide_stats['race'].value_counts()
sns.barplot(x=race_counts.values, y=race_counts.index)
plt.title('Race distribution of suicide cases')
plt.xlabel('Number of cases')
plt.ylabel('Race')
plt.show()

#month graph
plt.figure(figsize=(12, 6))
monthly_counts = suicide_stats.groupby('month').size()
plt.plot(monthly_counts.index, monthly_counts.values)
plt.title('Monthly distribution of suicide cases')
plt.xlabel('Month')
plt.ylabel('Number of cases')
plt.xticks(range(1, 13))
plt.show()

#location graph
plt.figure(figsize=(12, 6))
place_counts = suicide_stats['place'].value_counts()
sns.barplot(x=place_counts.values, y=place_counts.index)
plt.title('Location distribution of suicide cases')
plt.xlabel('Number of cases')
plt.ylabel('Location')
plt.show()

#gender graph
plt.figure(figsize=(12, 6))
gender_counts = suicide_stats['sex'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender distribution of suicide cases')
plt.show()

#education graph
plt.figure(figsize=(12, 6))
education_counts = suicide_stats['education'].value_counts()
sns.barplot(x=education_counts.values, y=education_counts.index)
plt.title('Education distribution of suicide cases')
plt.xlabel('Number of cases')
plt.ylabel('Education Level')
plt.show()

#sort all ages into groups for age gender analysis
suicide_stats['age_group'] = pd.cut(suicide_stats['age'], bins=[0, 18, 25, 35, 45, 55, 65, 75, 100], labels=['Under 18', '18-25', '26-35', '36-45', '46-55', '56-65', '66-75', 'Over 75'])
age_gender = pd.crosstab(suicide_stats['age_group'], suicide_stats['sex'])
age_gender_pct = age_gender.div(age_gender.sum(axis=1), axis=0) * 100

#create age geder graph
plt.figure(figsize=(12, 6))
sns.heatmap(age_gender_pct, annot=True, fmt='.1f', cmap='YlOrRd')
plt.title('Gender distribution within age groups')
plt.xlabel('Gender')
plt.ylabel('Age Group')
plt.show()
