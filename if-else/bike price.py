# take the price from user if
#     PRICE              TAX
#    >100000             15%
#    >50000              10%
#    <=50000             5%        
price=int(input("enter bike main price-"))
if price>100000:
    print("TAX, 15%")
elif price>50000 or price<=100000:
    print("TAX, 10%")   
elif price<=50000:
    price("TAX, 5%")