alphaToNum ={"a" : 1,"b" : 2,"c" : 3,"d" : 4,"e" : 5,"f" : 6,"g" : 7,"h" : 8,"i" : 9,"j" : 10,"k" : 11,"l" : 12,"m" : 13,"n" : 14,"o" : 15,"p" : 16,"q" : 17,"r" : 18,"s" : 19,"t" : 20,"u" : 21,"v" : 22,"w" : 23,"x" : 24,"y" : 25,"z" : 26}

userinput = input("Enter you name: ")
password = []
num = 0
sumOfTwo = 0
for i in userinput:
    num = alphaToNum[i]
    if num > 9:
        sumOfTwo = sum(int(j) for j in str(num))
        password.append(sumOfTwo)
    
    else:
        password.append(num)

print(password)

#39661
