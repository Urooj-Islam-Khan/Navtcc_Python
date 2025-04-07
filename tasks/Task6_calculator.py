num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
op = input("enter character")

if op=="+":
    print(num1,"+",num2,"=",num1 + num2)
elif op =="-":
    print(num1,"-",num2,"=",num1-num2)
elif op=="*":
    print(num1,"*",num2,"=",num1*num2)
elif op=="/":
    print(num1,"/5",num2,"=",num1/num2)
else:
    print("wrong operator")