# Exercise 1:
# Create a list called fruits with the following items: "apple", "banana", "cherry", "date". Print out the second and fourth elements using indexing.

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[1], fruits[3])

# Exercise 2:
# Given a list numbers = [10, 20, 30, 40, 50], print out the last element of the list using negative indexing.
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])

# Exercise 3:
# Create a list called colors with the following items: "red", "green", "blue", "yellow". Replace the third color with "purple" using indexing.

colors = ["red", "green", "blue", "yellow"]
colors[2] = "purple"
print(colors)
# Exercise 4:
# Write a program that takes a list of numbers as input and outputs the sum of all the numbers in the list.

numbers = []
sum = 0  
sumnum = []
for i in range(1, 6):
    num = int(input("Enter a number: "))
    numbers.append(num)
    sum += num
sumnum.append(sum) 
print("The given list:", numbers)
print("The sum of the numbers is:", sumnum)

# Exercise 5:
# Given a list words = ["apple", "banana", "cherry", "date"], print out the last three elements using slicing.
words = ["apple", "banana", "cherry", "date"]
print(words[-3:])

# Exercise 6:
# Write a program that takes a list of words as input and outputs the list in reverse order.

words = []
reversed_words = []
for i in range(1, 6):
    word = input("Enter a word: ")
    words.append(word)
    reversed_words.append(word[::-1])

print("The given list:", words)
print("The reversed list:", reversed_words)

# Exercise 7:
# Given a list numbers = [5, 10, 15, 20, 25], replace the second and fourth numbers with their squares using indexing.
numbers = [5, 10, 15, 20, 25]
numbers[1] = numbers[1] ** 2
numbers[3] = numbers[3] ** 2
print(numbers)

# Exercise 8:
# Create a list of numbers from 1 to 10. Using slicing, print out every second number in the list.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst[1:10:2])

# Exercise 9:
# Write a program that checks if a given list of words contains the word "python". If it does, print "Found", otherwise print "Not Found"

lists = ["java", "python", "c++", "javascript", "html", "css", "php", "ruby", "swift", "kotlin", "go", "rust", "typescript", "sql","dart"]
word = "python"
if word in lists:
    print("Found")
else:
    print("Not Found")


for i in range(len(lists)):
    if lists[i] == word:
        print("Found")
        break
else:
    print("Not Found")