def mydecorator(a):
    def internalFunction(*args,**kwargs):
        print("Welcome to my page")
        a(*args,**kwargs)
        print("copyright ©️ urooj khan - 2025\n")
    return internalFunction
    
@mydecorator
def myfunc():
    print("I am Full stack Website Developer | Mobile Application Developer | Java Developer | Python Developer")
myfunc()

@mydecorator
def cgpa(b):
    print(f"My CGPA: {b}")
cgpa(3.78)