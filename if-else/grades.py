# give grades on the basis of marks
a=int(input("enter the marks: "))
if a>90:
    print("Grade: A")
    if a>80 and a<=90:
        print("Grade: B")
if a>=60 and a<=80:
  print("Grade: C")
  if a<60:
      print("Grade: D")
else:
          print("failed")

perc=float (input(" enter percentage"))
if perc>85:
    print("A")
elif perc>70 and perc<=85:
        print("B")
elif perc >60 and perc<=70:
            print("C")
elif perc >45 and perc <=60:
                print("D")
else:
                    print("E")