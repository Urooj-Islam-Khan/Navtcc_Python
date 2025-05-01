from decorator import mydecorator

@mydecorator
def experience(a):
    print(f"I have {a} years of experience")

experience(3)
