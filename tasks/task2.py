# Q1) Write a program in which you have to ask S1, S2, S3 and show the output in this way: [(S1|S2)|S3]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
print("[(",S1,"|",S2,")|",S3,"]")

# Q2) Write a program in which you have to ask S1, S2, S3 and show the output in this way: [(S1,S2|S2/S1)||S3||]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
print("[(",S1,S2,"|",S2,"/",S1,")||",S3,"||]")

# Q3) Write a program in which you have to ask S1, S2, S3, S4 and show the output in this way: [[S1]/\[S2]/\[S3]/\[S4]]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
print("[[",S1,"]/\\[",S2,"]/\\[",S3,"]/\\[",S4,"]]")

# Q4) Write a program in which you have to ask S1, S2, S3, S4 and show the output in this way: |S1|-->S2<--|S3|-->S4
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
print("|",S1,"|-->",S2,"<--|",S3,"|-->",S4)

# Q5) Write a program in which you have to ask S1, S2, S3, S4 and show the output in this way: |S1|/-\|->S2<-|/-\|S3|/-\|->S4
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
print("|",S1,"|/-\\|->",S2,"<-|/-\\|",S3,"|/-\\|->",S4)

# Q6) Write a program in which you have to ask S1, S2, S3, S4, S5 and show the output in this way: S1|?|S5-~>S3$#>_[S2|(S4]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
S5 = input("Enter number 5: ")
print(S1,"|?|",S5,"-~>",S3,"$#>_[",S2,"|(",S4,"]")

# Q7) Write a program in which you have to ask S1, S2, S3, S4, S5 and show the output in this way: S1S2S3S4S5S2S3S1S4S1S2S4S5
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
S5 = input("Enter number 5: ")
print(S1+S2+S3+S4+S5+S2+S3+S1+S4+S1+S2+S4+S5)

# Q8) Write a program in which you have to ask S1, S2, S3, S4, S5 and show the output in this way: [S1/|\(|S2|(|S3|)/|\S4|)||S5]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
S4 = input("Enter number 4: ")
S5 = input("Enter number 5: ")
print("[",S1,"/|\\(|",S2,"|(|",S3,"|)/|\\",S4,"|)||",S5,"]")

# Q9) Write a program in which you have to ask S1, S2, S3 and show the output in this way: (|S1-><-S2|]<>><<>[[[S3]]]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
print("(|",S1,"-><-",S2,"|]<>><<>[[[",S3,"]]]")

# Q10) Write a program in which you have to ask S1, S2, S3 and show the output in this way: (((S1S3||/-?||S2,S1||?-\/||S3S2]]]
S1 = input("Enter number 1: ")
S2 = input("Enter number 2: ")
S3 = input("Enter number 3: ")
print("(((",S1+S3,"||/-?||",S2+","+S1,"||?-\\/||",S3+S2,"]]]")