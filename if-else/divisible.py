# take userinput,check whther its is divisble by 5 or 11
num=int(input("enter the number"))
if num%11==0:
    print("divisible by 11")
elif num%5==0:
 print("divisible by 5")
else:
 print("not divisible")