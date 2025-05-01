# Task 1: Square of Numbers
# Problem: Write a lambda function to calculate the square of a given number.
a = lambda x:x**2
print(a(5))
# Task 2: Add Two Numbers
# Problem: Write a lambda function to add two numbers.
b  = lambda x,y:x+y
print(b(2,3))

# Task 3: Sort List of Tuples
# Problem: You have a list of tuples where each tuple contains two values. Sort the list based on the second value using a lambda function.
lst = [(1, 4), (3, 1), (5, 3)]
# key is used to sort the list based on the second value of each tuple.
c = sorted(lst, key=lambda y: y[1])
print(c)

# Task 4: Filter Even Numbers
# Problem: Write a lambda function to filter out even numbers from a list using filter().
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x:x%2==0,numbers)
print(list(even))

# Task 5: Find Maximum Using Lambda
# Problem: Write a lambda function to find the maximum of two numbers.
num = lambda x,y:x if x>y else y
print(num(10,20))
