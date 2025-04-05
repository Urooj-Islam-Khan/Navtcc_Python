# take date of birth from user and calculate age also tell them their zodiac sign with little description of that

# **Date of Birth and Zodiac Sign**
import datetime

# User se date of birth lena
dob = input("Enter your date of birth (YYYY-MM-DD): ")

# Date ko proper format mein convert karna
dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date() 
#ye date jo string me save hota hai usko date me convert karne ke liye use krte hain or .date() se date ko extract karte hainura date or time return krta hai

current_date = datetime.date.today() # Aaj ki date lena

age = current_date.year - dob.year # Age calculate karna

if current_date.month < dob.month or current_date.day < dob.day:
    age -=1
    print("Your age is:", age)
else:
    print("Your age is:", age)

month = dob.month
day = dob.day
zodiac_sign = ""
description = ""

if month == 3 and day >=21 or month == 4 and day<=19:
    zodiac_sign = "Aries"
    description = "Aries is the first sign of the zodiac, symbolizing new beginnings and courage."
elif month == 4 and day >=20 or month == 5 and day<=20:
    zodiac_sign="Taurus"
    description = "Taurus is known for its practicality, reliability, and love for beauty."
elif month == 5 and day >=21 or month == 6 and day<=21:
    zodiac_sign="Gemini"
    description = "Gemini is characterized by duality, communication, and adaptability."
elif month == 6 and day >=22 or month == 7 and day<=22:
    zodiac_sign="Cancer"
    description = "Cancer is nurturing, emotional, and deeply intuitive."
elif month == 7 and day >=23 or month == 8 and day<=22:
    zodiac_sign="Leo"
    description = "Leo is known for its confidence, creativity, and leadership qualities."
elif month == 8 and day >=23 or month == 9 and day<=22:
    zodiac_sign="Virgo"
    description = "Virgo is practical, analytical, and detail-oriented."
elif month == 9 and day >=23 or month == 10 and day<=23:
    zodiac_sign="Libra"
    description = "Libra is associated with balance, harmony, and relationships."
elif month == 10 and day >=24 or month == 11 and day<=21:
    zodiac_sign="Scorpio"
    description = "Scorpio is intense, passionate, and mysterious."
elif month == 11 and day >=22 or month == 12 and day<=21:
    zodiac_sign="Sagittarius"
    description = "Sagittarius is adventurous, optimistic, and loves freedom."
elif month == 12 and day >=22 or month == 1 and day<=19:
    zodiac_sign="Capricorn"
    description = "Capricorn is disciplined, responsible, and has a strong sense of duty."
elif month == 1 and day >=20 or month == 2 and day<=18:
    zodiac_sign="Aquarius"
    description = "Aquarius is innovative, independent, and values humanitarianism."
elif month == 2 and day >=19 or month == 3 and day<=20:
    zodiac_sign="Pisces"
    description = "Pisces is compassionate, artistic, and deeply emotional."
else:
    zodiac_sign="Unknown"
    description="No description available."