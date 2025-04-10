a =  int(input("Enter a number: "))
# if a%3==0:
#     print("Ding")
# elif a%5==0:
#     print("Dong")
# if a%3==0 and a%5==0:
#     print("Ding Dong")
# else:
#     print("Dong Ding")

if a%3==0 and a%5==0:
    print("Ding Dong")
elif a%3 ==0 and a%5!=0:
    print("Ding")
elif a%5 ==0 and a%3!=0:
    print("Dong")
else:
    print("Dong Ding")