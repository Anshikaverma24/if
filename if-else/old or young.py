# check who is oldest out of three people
age1=int(input("enter the number"))
age2=int(input("enter the number"))
age3=int(input("enter the number"))
if age1 > age2 and age1 > age3:
    print("Person 1 is oldest")
elif age2 > age1 and age2 > age3:
    print("Person 2 is oldest")
elif age3 > age1 and age3 > age2:
    print("Person 3 is oldest")