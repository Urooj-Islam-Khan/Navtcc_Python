# Q1) Create a class called Calculator with a method add that takes two parameters and returns their sum. Create an object of the class and use the method.

def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

# Q2) "Create a program in Python that will have a function.
# The function will take a string as input, and it will count and print the occurrence of a specific word within that string. The program will use the count function."
# For Example:
# string="Programming"
# # input= m
# # output= 2

def count_word(letter,word = "Programming"):
    count = 0
    
    for i in word:
        if i == letter:
            count += 1
    return count
    
    
letter = input("Enter a letter to count: ")
print(count_word(letter))

# Q3) Given two tuples, ('apple', 'banana', 'cherry') and ('orange', 'grape'), concatenate them into a single tuple. Print the resulting tuple.

def concate(t1,t2):
    return t1 + t2

tpl1 = ('apple', 'banana', 'cherry')
tpl2 = ('orange', 'grape')
print(concate(tpl1,tpl2))

# Q4) Create a BMI Calculator with def function:
def BMI(weight,height):
    formula = weight/(height**2)
    return formula

hf = float(input("Enter height in feet: "))
hm = hf*0.3048
w = float(input("Enter weight in kg: "))
print("BMI:", BMI(w,hm))

if BMI(w,hm) < 18.5:
    print("Underweight")
elif BMI(w,hm) >= 18.5 and BMI(w,hm) < 24.9:
    print("Normal weight")
elif BMI(w,hm) >= 25:
    print("Overweight")