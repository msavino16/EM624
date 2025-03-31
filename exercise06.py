# Author:  Michael Savino

#"I pledge my honor that i have abided by the Stevens Honor System"

# Exercise 06
# Pandas program

# This program will intake a file and convert it to pandas dataframes

# The program is written by loading in each dataset, then doing data manipulation and creating charts

#Import the required libraries
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
from math import pi
from time import sleep

print("\n run by Michael Savino")
print()

faculty_df = pd.read_csv('SSE_Faculty.csv')

years = ['19-20', '20-21', '21-22', '22-23', '23-24']
programs = faculty_df['Program'].unique()

#Number of courses per each program per each Academic Year. This will be calculated using the
# "Load". For example, a Load value of "6" means the faculty taught 6 courses
print("Courses per program per Academic Year:")
for year in years:
    print()
    print(f"Academic Year {year}:")
    load_column = f'Load {year}'
    for program in programs:
        program_load = faculty_df[faculty_df['Program'] == program][load_column]
        total_courses = program_load.sum()
        print(f"{program}: {total_courses:.2f} courses")


#Average number of courses per faculty per Academic Year (from the "Load"). This per faculty, not
# per program. The "N/A" means the faculty did not teach that year.
print()
avg_courses_by_year = []
print("Average courses per faculty per Academic Year:")
for year in years:
    load_column = f'Load {year}'
    faculty = faculty_df[faculty_df[load_column] != 'N/A'][load_column]
    avg_courses = faculty.mean()
    print(f"{year}: {avg_courses:.2f} courses/faculty")
    avg_courses_by_year.append(avg_courses)

    


#Number of underloaded faculty per each Academic Year (An underloaded condition is when the
# Load for a given faculty that is less than the Target). This per faculty, not per program
print()
print("Number of underloaded faculty per Academic Year:")
for year in years:
    load_column = f'Load {year}'
    target_column = f'Target {year}'
    boolean_mask = (faculty_df[load_column] != 'N/A') & (faculty_df[target_column] != 'N/A')
    underloaded = faculty_df[boolean_mask][faculty_df[boolean_mask][load_column] < faculty_df[boolean_mask][target_column]]
    print(f"{year}: {len(underloaded)} faculty")


#Number of overloaded faculty per each Academic Year (Load that is more than the Target). This
# per faculty, not per program
print()
print("Number of overloaded faculty per Academic Year:")
overloaded_by_year = []
for year in years:
    load_column = f'Load {year}'
    target_column = f'Target {year}'
    boolean_mask = (faculty_df[load_column] != 'N/A') & (faculty_df[target_column] != 'N/A')
    overloaded = faculty_df[boolean_mask][faculty_df[boolean_mask][load_column] > faculty_df[boolean_mask][target_column]]
    print(f"{year}: {len(overloaded)} faculty")
    overloaded_by_year.append(len(overloaded))
    

#Average number of courses per faculty over the years. This is from the Load. Each faculty will have 1
# value (the average of courses taught in the years). The x-axis is the years, the y-axis the number of
# courses (from "Loads")    

p = figure(x_range=years, height=350, title='Average Courses per Faculty by Year',
           toolbar_location=None)
p.vbar(x=years, top=avg_courses_by_year, width=0.8)
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = 'Academic Year'
p.yaxis.axis_label = 'Number of Courses'





#Number of overloaded faculty over the years. Each year will have 1 value, that is the number of
# overloaded faculty. The x-axis is the years, the y-axis the number of loads (courses). 

p2 = figure(x_range=years, height=350, title='Number of Overloaded Faculty by Year',
           toolbar_location=None)
p2.line(x=years, y=overloaded_by_year, line_width=2)
p2.xgrid.grid_line_color = None
p2.y_range.start = 0
p2.xaxis.axis_label = 'Academic Year'
p2.yaxis.axis_label = 'Number of Overloaded Faculty'




# Calculate courses by program for 2023-24
load_2324 = 'Load 23-24'
programs = ['EM', 'SSW', 'SYS']
courses_by_program = {}

for program in programs:
    program_faculty = faculty_df[faculty_df['Program'] == program]
    program_load = program_faculty[program_faculty[load_2324] != 'N/A'][load_2324].sum()
    courses_by_program[program] = program_load


data = pd.Series(courses_by_program).reset_index(name='value').rename(columns={'index': 'program'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[3]

p3 = figure(height=350, title="Courses by Program (23-24)", toolbar_location=None,
           tools="hover", tooltips="@program: @value", x_range=(-0.5, 1.0))

p3.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='program', source=data)

p3.axis.axis_label = None
p3.axis.visible = False
p3.grid.grid_line_color = None

show(p)
sleep(1) #Added to make all charts render
show(p2)
sleep(1) #Added to make all charts render
show(p3)
print("--------------------------------------------------------")
#CHAT GPT CODE BELOW -----------------------------------------------------------------------------------


import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt

df = pd.read_csv('SSE_Faculty.csv')

import pandas as pd

# --- Step 2a: Number of Courses per Program per Academic Year ---

# Identify columns that represent course loads (they start with "Load ")
load_cols = [col for col in df.columns if col.startswith("Load ")]

# Reshape the DataFrame from wide to long format using the melt function.
# We keep 'ID' and 'Program' as identifier variables.
df_long = df.melt(id_vars=["ID", "Program"],
                  value_vars=load_cols,
                  var_name="Academic Year",
                  value_name="Load")

# Extract the academic year by removing the "Load " prefix.
df_long["Academic Year"] = df_long["Academic Year"].str.replace("Load ", "")

# Convert the 'Load' values to numeric, turning non-numeric entries (like "N/A") into NaN,
# then fill NaN with 0 (meaning no courses taught).
df_long["Load"] = pd.to_numeric(df_long["Load"], errors='coerce')
df_long["Load_filled"] = df_long["Load"].fillna(0)

# Group by 'Academic Year' and 'Program' and sum the 'Load_filled' values.
courses_per_program = (
    df_long.groupby(["Academic Year", "Program"])["Load_filled"]
           .sum()
           .reset_index(name="Total Courses")
)

print("Number of courses per program per Academic Year:")
print(courses_per_program)


# --- Reshape the DataFrame into Long Format for "Load" and "Target" ---

# Identify "Load" columns (e.g., "Load 19-20", "Load 20-21", etc.)
load_cols = [col for col in df.columns if col.startswith("Load ")]
df_long_load = df.melt(id_vars=["ID", "Program"],
                       value_vars=load_cols,
                       var_name="Academic Year",
                       value_name="Load")
# Remove the "Load " prefix to get the academic year
df_long_load["Academic Year"] = df_long_load["Academic Year"].str.replace("Load ", "")
# Convert to numeric, treating non-numeric (e.g., "N/A") as NaN and then fill with 0
df_long_load["Load"] = pd.to_numeric(df_long_load["Load"], errors='coerce')
df_long_load["Load_filled"] = df_long_load["Load"].fillna(0)

# Identify "Target" columns (e.g., "Target 19-20", "Target 20-21", etc.)
target_cols = [col for col in df.columns if col.startswith("Target ")]
df_long_target = df.melt(id_vars=["ID", "Program"],
                         value_vars=target_cols,
                         var_name="Academic Year",
                         value_name="Target")
# Remove the "Target " prefix to get the academic year
df_long_target["Academic Year"] = df_long_target["Academic Year"].str.replace("Target ", "")
# Convert to numeric, treating non-numeric as NaN
df_long_target["Target"] = pd.to_numeric(df_long_target["Target"], errors='coerce')

# Merge the two long DataFrames on ID, Program, and Academic Year
df_long = pd.merge(df_long_load, df_long_target, on=["ID", "Program", "Academic Year"])

# --- Step 2b: Average Number of Courses per Faculty per Academic Year ---
# Calculate the mean of the "Load_filled" for each Academic Year.
avg_courses_per_faculty = (
    df_long.groupby("Academic Year")["Load_filled"]
           .mean()
           .reset_index(name="Average Courses")
)
print("Average number of courses per faculty per Academic Year:")
print(avg_courses_per_faculty)
print("\n")

# --- Step 2c: Number of Underloaded Faculty per Academic Year ---
# Underloaded: where the faculty's Load_filled is less than the Target.
underloaded = df_long[df_long["Load_filled"] < df_long["Target"]]
underloaded_count = (
    underloaded.groupby("Academic Year")
               .size()
               .reset_index(name="Underloaded Count")
)
print("Number of underloaded faculty per Academic Year:")
print(underloaded_count)
print("\n")

# --- Step 2d: Number of Overloaded Faculty per Academic Year ---
# Overloaded: where the faculty's Load_filled is greater than the Target.
overloaded = df_long[df_long["Load_filled"] > df_long["Target"]]
overloaded_count = (
    overloaded.groupby("Academic Year")
              .size()
              .reset_index(name="Overloaded Count")
)
print("Number of overloaded faculty per Academic Year:")
print(overloaded_count)
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.transform import cumsum
from math import pi
import pandas as pd

# Use output_file for non-notebook environments
output_file("bokeh_plots.html")

# Example: Bar Plot (ensure your DataFrame 'avg_courses_per_faculty' exists)
source_avg = ColumnDataSource(avg_courses_per_faculty)
p1 = figure(x_range=avg_courses_per_faculty["Academic Year"].tolist(),
            title="Average Courses per Faculty Over the Years",
            x_axis_label="Academic Year",
            y_axis_label="Number of Courses",
            height=400)
p1.vbar(x="Academic Year", top="Average Courses", width=0.8, source=source_avg)

# Example: Line Plot (ensure 'overloaded_count' exists)
source_over = ColumnDataSource(overloaded_count)
p2 = figure(x_range=overloaded_count["Academic Year"].tolist(),
            title="Number of Overloaded Faculty Over the Years", 
            x_axis_label="Academic Year",
            y_axis_label="Number of Overloaded Faculty",
            height=400)
p2.line(x="Academic Year", y="Overloaded Count", source=source_over, line_width=2)
p2.scatter(x="Academic Year", y="Overloaded Count", source=source_over, size=8)

# Example: Pie Chart (ensure 'df_long' exists and is properly filtered)
df_2324 = df_long[df_long["Academic Year"] == "23-24"]
courses_2324 = (
    df_2324.groupby("Program")["Load_filled"]
           .sum()
           .reset_index(name="Total Courses")
)
courses_2324["angle"] = courses_2324["Total Courses"] / courses_2324["Total Courses"].sum() * 2 * pi
colors = {"EM": "#c9d9d3", "SSW": "#718dbf", "SYS": "#e84d60"}
courses_2324["color"] = courses_2324["Program"].map(colors)
source_pie = ColumnDataSource(courses_2324)
p3 = figure(height=400, title="Courses by Program in '23-'24",
            toolbar_location=None, tools="hover", tooltips="@Program: @Total Courses",
            x_range=(-1, 1))
p3.wedge(x=0, y=0, radius=0.8,
         start_angle=cumsum('angle', include_zero=True),
         end_angle=cumsum('angle'),
         line_color="white", fill_color='color',
         legend_field='Program', source=source_pie)
p3.axis.visible = False
p3.grid.grid_line_color = None

# Show all plots (they will all be embedded in the same HTML file)
show(p1)
sleep(1) #Added to make all charts render
show(p2)
sleep(1) #Added to make all charts render
show(p3)

#CHAT GPT CODE END -----------------------------------------------------------------------------------
print('\nThanks for using this tool!\n')
 