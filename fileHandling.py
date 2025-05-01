inp1 = int(input("Enter num 1: "))
inp2 = int(input("Enter num 2: "))
sum = inp1 + inp2
sum = str(sum)
a = open("user.txt","w")
b = a.write(f"The sum of {inp1} and {inp2} is {sum}")
a.close