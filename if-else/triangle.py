# print three types of triangles 
angle1=int(input("enter the angle1-"))
angle2=int(input("enter the angle2-"))
angle3=int(input("enter the angle3-"))
if angle1==angle2==angle3:
 print("equilateral triangle")
elif angle1==angle2!=angle3 and angle1!=angle2==angle3 and angle1!=angle3==angle2:
 print("isoceles triangle")
if angle1!=angle2!=angle3:
 print("scalene triangle")