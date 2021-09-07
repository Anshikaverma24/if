#  print "navgurukul" if the number is divisible by 3 and 7, if divisible by 3 print "nav" and print "gurukul" if divisible by 7
i=1
while i<=100:
    if i%3==0 and i%7==0:
     print("navgurukul")
    elif i%3==0:
     print("nav")
    elif i%7==0:
     print("gurukul")
    else:
     print(i)
    i+=1