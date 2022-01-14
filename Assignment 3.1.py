hrs = input("Enter Hours:")
h = float(hrs)
rate= input("Rate:")
r = float(rate)
if(h<40):
    pay=r*h
    print(pay)
else:
    pay=r*40+r*1.5*(h-40)
    print(pay)
    
