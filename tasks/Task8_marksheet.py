print("Task 1")
name = input("Enter your name: ")
obtainedMarks = input("Enter your obtained Marks: ")
totalMarks = input("Enter total marks: ")

percentage = (float(obtainedMarks)/float(totalMarks)) *100
print(percentage)


print("Task 2")

sub1 = int(input("Enter  your sub 1 marks"))
sub2 = int(input("Enter  your sub 2 marks"))
sub3 = int(input("Enter  your sub 3 marks"))
sub4 = int(input("Enter  your sub 4 marks"))
sub5 = int(input("Enter  your sub 5 marks"))
sub6 = int(input("Enter  your sub 6 marks"))
sub7 = int(input("Enter  your sub 7 marks"))
sub8 = int(input("Enter  your sub 8 marks"))
obt=sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8

avg = obt/8
print(avg)