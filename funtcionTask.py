# Create a function called generate_marksheet that:

# Takes a student's name, roll number, and a dictionary of subjects with obtained marks.

# Calculates:

# Total obtained marks

# Percentage

# Grade (based on criteria below)

# Adds:

# Pass/Fail Status (if any subject is below 40, student fails)

# Class Position (assume marks of 3 more students are given for comparison)

# Remarks based on performance

# Returns a well-formatted marksheet as a string


# generate_marksheet(name, roll_number, subjects):

name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
eng = int(input("Enter English marks: "))
mad = int(input("Enter Mobile Application marks: "))
cg = int(input("Enter Calculus marks: "))
py = int(input("Enter Python marks: "))
cc = int(input("Enter Cloud Computing marks: "))
subjects = {}
subjects["English"] = eng
subjects["Mobile Application"] = mad
subjects["Calculus"] = cg
subjects["Python"] = py
subjects["Cloud Computing"] = cc




