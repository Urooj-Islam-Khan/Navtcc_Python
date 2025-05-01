print("---------Student Marks------------")


students = []

i = 1
while i <= 3:
    print(f"\nEnter details for Student {i}:")
    name = input("Enter the Student Name: ")
    roll = int(input("Enter the Roll Number: "))
    e = int(input("Enter English marks: "))
    m = int(input("Enter Math marks: "))
    u = int(input("Enter Urdu marks: "))
    c = int(input("Enter Computer marks: "))
    p = int(input("Enter Physics marks: "))

    total = e + m + u + c + p
    percentage = (total / 500) * 100

    if percentage >= 80:
        grade = "A1"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\n------------ RESULT CARD ---------")
    print("STUDENT Name  :", name)
    print("ROLL NUMBER   :", roll)
    print("TOTAL MARKS   :", total)
    print("GRADE         :", grade)
    print("---------End----------")

   
    students.append([name, total])

    i += 1


i = 0
while i < len(students):
    next_student = i + 1
    while next_student < len(students):
        if students[next_student][1] > students[i][1]:
            temp = students[i]
            students[i] = students[next_student]
            students[next_student] = temp
        next_student = next_student + 1
    i += 1


print("\n----- STUDENT POSITIONS -----")
position = 1
for s in students:
    
    if position == 1:
        trophy = " 🏆🎊"
        alp = "st"
    elif position == 2:
        trophy = " 🎉🎊"
        alp = "nd"
    elif position == 3:
        trophy = " 😭😂"
        alp = "rd"
    

    print(f"{position}{alp} Position => Name: {s[0]}{trophy}    || Total Marks: {s[1]}")
    position += 1