Date_of_birth = int(input("Date of Birth: "))
The_year_now = int(input("The_year_now: "))
if (The_year_now-Date_of_birth)>=18:
    print("You can vote in the elections")
else:
    print("You can not vote in the election")

# --------------------------------------------------------
#פתרון בלי לבקש את השניה עכשיו 
# import datetime
# Date_of_birth = int(input("Date of Birth: "))
# if (datetime.datetime.today().year-Date_of_birth)>=18:
#     print("You can vote in the elections")
# else:
#     print("You can not vote in the election")