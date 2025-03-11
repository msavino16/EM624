import pandas as pd


print ("\n run by Michael Savino")
print ()

classes_df = pd.read_csv('REG_CAP_Spring25_624.csv')


#a. calculate the percentage of courses online vs total (from the column "Delivery Mode").

online_count = len(classes_df[classes_df["Delivery Mode"] == "Online"])
total_count = len(classes_df)
online_percent = (online_count / total_count) * 100
inPerson_percent = 100-(online_count / total_count) * 100

print(f"Online courses: {online_percent:.2f}%")
print(f"In-person courses: {inPerson_percent:.2f}%")

"""
Online courses: 49.59%
In-person courses: 50.41%
"""

#b. calculate the number of students per each level of courses (from the column "Level"). Both "G" and "G-UG" are considered "graduate".

grad_students = int(classes_df[classes_df["Level"].isin(["G", "G-UG"])]["Enrollment Count"].sum())
undergrad_students = int(classes_df[classes_df["Level"] == "UG"]["Enrollment Count"].sum())
corp_students = int(classes_df[classes_df["Level"] == "CORP"]["Enrollment Count"].sum())

print("\nNumber of students per level:")
print("Graduate:", grad_students)
print("Undergraduate:", undergrad_students) 
print("CORP:", corp_students)

"""
Number of students per level:
Graduate: 1000
Undergraduate: 793
CORP: 265
"""

#c. calculate the percentage of graduate students vs total (from the column "Level"). Both "G" and "G-UG" are considered "graduate".
print()
percent_grad = float(grad_students)/float(grad_students+undergrad_students+corp_students)*100
print(f"{percent_grad:.2f}% of the students are Graduate students")

"""
48.59% of the students are Graduate students
"""


#d. using the column "Enrollment Count", print:

#1. the number of courses with less than 15 students
print()
less_then_15_students = classes_df[classes_df['Enrollment Count'] < 15].shape[0]
print(f"The number of classes with less than 15 students is {less_then_15_students}")
#2. the number of courses with more than 20 students but less or equal than 35
print()
more_than_20 = classes_df[classes_df['Enrollment Count'] > 20]
more_than_20_less_or_equal_35 = more_than_20[more_than_20['Enrollment Count'] <= 35].shape[0]
print(f"The number of classes with more than 20 students but less than or equal to 35 students is {more_than_20_less_or_equal_35}")
#3. the number of courses with more than 35 students
print()
more_than_35_students = classes_df[classes_df['Enrollment Count'] > 35].shape[0]
print(f"The number of classes with more than 35 students is {more_than_35_students}")
#4. the average number of students per course, not counting the courses with less than 5 students or blank as "Enrollment Count"
print()
filtered_df = classes_df[classes_df['Enrollment Count'] >= 5]
avg_students = filtered_df['Enrollment Count'].mean()
print(f"The average number of students per course, not counting the courses with less than 5 students or blank is {avg_students:.2f}")
#5. the 5 graduate courses with the highest number of students. In this case, consider as graduate courses only those with "G" in the column "Level".
print()
grad_courses = classes_df[classes_df['Level'] == 'G']
sorted_grad = grad_courses.sort_values('Enrollment Count', ascending=False)
top_5_grad = sorted_grad.head(5)
print("The 5 graduate courses with the highest enrollment are:")
for _, row in top_5_grad.iterrows():
    print(f"{row['Course']}: {int(row['Enrollment Count'])} students")
    
'''
The number of classes with less than 15 students is 44

The number of classes with more than 20 students but less than or equal to 35 students is 36

The number of classes with more than 35 students is 5

The average number of students per course, not counting the courses with less than 5 students or blank is 19.67

The 5 graduate courses with the highest enrollment are:
EM624-WS/SYS624-WS: 31 students
EM624-A/SYS624-A: 30 students
EM665-WS: 28 students
SYS611-WS: 27 students
EM605-A: 26 students
'''