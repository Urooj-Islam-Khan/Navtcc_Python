# ✅ LEVEL 1 – Crack the Login
#  Aapko admin user ka password guess karna hai.
#  Valid passwords passwords.txt file mein hote hain.
#  Aapko 3 chances milti hain.
#  Sahi password mil gaya → next level``
#  Galat → game over
# Concepts used:
# file handling, loop, if-else, try-except

# LEVEL 2 – Trace the Hidden Keyword
#  Aapko ek file clue.txt se keyword accesskey find karna hota hai.
#  User se direct poocha jata hai keyword kya hai.
#  Agar:
#  Input correct hai
#  AND 30 seconds ke andar diya gaya hai
# → next level
# warna → fail
# Concepts used:
# file reading, timing, conditional logic

# 🔐 LEVEL 3 – Decode the Cipher
#  File encrypted.txt mein ek encrypted message hota hai (e.g., Caesar cipher).
#  Aapko ise decrypt kar ke user se poocha jata hai correct message kya hai.
#  Agar sahi diya → next level
# Concepts used:
# string manipulation, list comprehension, encryption, decorator (logging)

# 💣 LEVEL 4 – Defuse the Bomb (Logic Puzzle)
#  Ek riddle diya jata hai:
#  “I speak without a mouth and hear without ears. What am I?”
#  Correct answer: echo
#  3 chances hoti hain.
#  Agar sahi answer → bomb.txt mein likha jata hai: “Bomb defused successfully!”
#  Galat → “Bomb exploded!”
# Concepts used:
# if-else, file writing, loop, input logic

# 🧱 LEVEL 5 – Final Firewall
#  Grid (matrix) mein ek weak point hidden hota hai e.g. (2,2)
#  User se grid coordinates liye jate hain.
#  Agar coordinates match karein → firewall breached → mission complete
# Concepts used:
# 2D list, tuple matching, input, try-except
    

import os
import time

os.chdir(r"E:\Python\HackingGame")

enc = ""


# level two function
def LevelTwo(keyword):
    a= ""
    with open("clue.txt","r") as f:
        a = f.read() 

    startTime = time.time()

    keywordAsk = keyword

    endTime = time.time()

    totalTime = endTime - startTime

    if keywordAsk == a and totalTime<=30:
        print("Correct and on time! Proceed to next level.")
        print("\nLevel Two Completed")
        @encrypter
        def LevelThree():
            print("\nLevel Three Complete")

        LevelThree()

    elif(totalTime>30):
        print("Timesup")
    elif(keywordAsk != a):
        print("❌ Incorrect\n Game Over!")

# level three decorator 
def encrypter(a):
    def internalEncrypter(*args,**kwargs):
        decryptText = { "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i", "h": "j", "i": "k", "j": "l", 
        "k": "m", "l": "n", "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v", 
        "u": "w", "v": "x", "w": "y", "x": "z", "y": "a", "z": "b"}
        with open("encrypted.txt", "r") as f:
            encLine = f.read().strip()
        print("\nLevel Three Starts\n")

        print(f"Encrypted Message: {encLine}")

        user_decrypt = input("Enter decrypted message: ").strip().lower()

        lists = []
        for i in encLine:
            if i in decryptText:
                lists.append(decryptText[i]) 
            else:
                lists.append(i)  
        decrypted_message = ''.join(lists).strip().lower()

        print("Decrypted code: ", decrypted_message)
        print("You entered         : ", user_decrypt)

        if user_decrypt == decrypted_message:
            a(*args, **kwargs)
            LevelFour()
        else:
            print("\nYou Lose\nGame Over")

    return internalEncrypter

# LevelFour 
def LevelFour():
    print("\nLevel Four Starts\nSolve the riddle")
    print("\"I speak without a mouth and hear without ears. What am I?\"")
    while i < 3:
        riddleAns = input("Enter the answer ").lower()
        if riddleAns == "echo":
            with open("bomb.txt","w") as f:
                f.write("\nBomb defused successfully")
            print("\nLevel Four Completed\n")
            levelFive()
            break
        else:
            print("\nBomb exploded!")
            break
    return LevelFour

# level five 
def levelFive():
    list2D = [
    [1,2,3,4],
    [4,6,7,8],
    [9,10,"w",12],
    [13,14,15,16]
    ]
    for row in list2D:
        print(row)
    weak_point = (2,2)
    print("Level Five Starts\n")
    try:
        wRow =  int(input("Enter indexed of row: "))
        wCol =  int(input("Enter indexed of column: "))
        userWP = (wRow,wCol)
        if weak_point == userWP:
            print("\nfirewall breached → mission complete")
        else:
            print("\nmission failed → Game Over")
    except ValueError:
        print("\nError: Please use only integers" )

pswd = ""
attempt = 3
i=0


# Program starts 
with open("password.txt","w") as f:
    f.write("Urooj124")
with open("password.txt","r") as f:
    pswd = f.read()
    
starts = input("Do you want to start HAckersGame\n Press \'Y\' for yes and \'N\' for No").lower()
if starts == "y":

    while (i<3):
        try:
            userpswd = input("Enter password ")
            if attempt<=3 and attempt>0:
                if pswd == userpswd:
                    print("\nLevel One Completed")
                    print("\nLevel Two Starts \n")
                    b = input("Enter keyword and Don't forget to use \'#\' in start ")
                    LevelTwo(b)
                    break
                elif pswd != userpswd:
                    attempt =attempt-1
                    print(f"You have {attempt} left")
                    print("Wrong password")
                if attempt==0:
                    print("\nGame Over 😭")
                    exit()
                i+=1
        except ValueError as e:
            print("Error: ", e)
else:
    print("Thank you for wasting our time\n Get Lost")
    exit()