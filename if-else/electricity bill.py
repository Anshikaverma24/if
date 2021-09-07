# calculate electricity  bill
units=int(input("enter the units"))
if units<=100:
    print(" no charges")
elif units>100 or units>=200:
    bill=units*5
    print(bill)
elif units<200 or units<=400:
    bill=units*10
    print(bill)