a=2;
b=3;
n=4;
k=5;

print("1. Addition and Subtraction")
eq1 = (a + b) % n
eq2 = ((a % n) + (b % n)) % n
print(  eq1,"=",eq2 )

eq1 = (a - b) % n
eq2 = ((a % n) - (b % n)) % n
print(eq1, "=", eq2)

print("2. Multiplication")
eq1 = a * b % n
eq2 = ((a % n) * (b % n)) % n
print(eq1, "=", eq2)

print("3. Exponential")
eq1= (a**k) % n 
eq2= ((a % n)**k)%n
print(eq1, "=", eq2)
