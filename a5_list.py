#************************** CS421: Assignment 5 **************
#
#  There are four sections in this assignment. Each section is worth 5 points.
#  Sections 1 and 2 count towards Assignment 5.
# Sections 3 and 4 count towards Assignment 6.
#  Skeleton code is already given. 
#  You only need to add your code between BEGIN and END lines in each section.
#
# Do NOT hardcode the output; You need to write python code so that it works whether
# you have 10 students in the list OR 1000 students in the list.
#
#  Use pythontutor.com to implement each section.
#  Save the complete implementation to a file called "a5_lists.py" and submit the file to Google Classroom
#
# How to save the code from PythonTutor to a file?
#           Select the entire code (Ctrl + A)
#           Copy the entire code (Ctrl + C)
#           Open notepad or any other editor you use to write text files.
#           Paste the entire code (Ctrl + V)
#           Save the code to a file (Ctrl +S)
# ************************************************************


#----------------------------------------------------------------------------
# A.5.1 --> Assume that some students registered twice for the same class.
# You need to write a program to remove the duplicate registrations from a list
#----------------------------------------------------------------------------

# define students list
students = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie", "peter"]
print("All students --> ", students)



#=========================================
# BEGIN -- your code
student_1 = []
for x in students:
    if x not in student_1:student_1.append(x)
# ---- pseudo code 
# I used the for loop to pick a name from the students list. I stated that if x is not in the empty list student_1, to inset the name into student_1. If the name was in student_1 it would choose the next name.
# -------------------------------------------------------------------------------------------------------------
# start with an temporary empty list called "student_temp"
# we need to visit each and every element in "students" list.
# so, start with a for loop on the "students"
# for each element in the list
#         check whether the element is in the student_temp
#         if the element is not in the student_temp, add it there
#         if the element is there in the student_temp, it implies it is a duplicate. So, don't add
# 
# once the for loop ends, we will have "student_temp" which contains only the unique students
# 
# assign our orignal variable "students" to "student_temp"
# we are now done; students list now contains only the unique students.

# END -- your code
#=========================================

# print students list. This should NOT contain any duplicates
print("Unique students --> ", students)


#----------------------------------------------------------------------------
#A.5.2 --> Assume that some students registered both html and python classes
# Find out the list of students who registered for both the classes.
#----------------------------------------------------------------------------


html = [ "barb", "dan", "ellie", "abe", "chris"]    
python = ["henry", "chris", "dan", "ellie", "frank", "gavin"] 

#=========================================
# BEGIN -- your code
dupe_list = []
for y in html:
    if y in python:dupe_list.append(y)
# pseudo-code
# I created an empty list called dupe_list. I used for loop to choose a name from html. If the name was in python i would add it to dupe_list.

# Start a for loop on html list
# Then for each element X in html list
#           check whether the element x in python list
#           If it is there, we know that it is a duplicate registration.
#           So, add the element x to dupe_list list
# 
# Once the for loop is done, 
# our dupe_list now contains all the duplicate names.

# END -- your code
#=========================================

print("html students --> ", html)
print("python students --> ", python)
print("duplicates --> ", dupe_list)