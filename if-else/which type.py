# check whther the input is either integer, alphabate or special character
letter=input("enter the letter")
if letter=="":
    print("alphabate")
elif letter==int:
    print("integer")
elif letter!="" or letter!=int:
    print("special character")