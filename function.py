# def abc(**kwargs):
#     print(sum(kwargs.values()))
#     abc(a=4,b=5)

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

def mod(a,b):
    return(a%b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (add,sub,mul,div,mod): ").lower()

operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "mod": mod
}
if operator in operations:
    result = operations[operator](num1,num2)
print(f"{result}")



# if op == '+':
#     sum(num1,num2)
# elif op == '-':
#     sub(num1,num2)
# elif op == '*':
#     mul(num1,num2)
# elif op == '/':
#     div(num1,num2)
# elif op == '%':
#     mod(num1,num2)
