# take attendance total from user out of 300, if if higher than 75% print"allowed" else print"not allowed"
student=int(input("enter the total attendance"))       #out of 300
percent_attendence=student/300*100
if percent_attendence<=75:
 print("not allowed")
else :
 print("allowed")
print(percent_attendence)