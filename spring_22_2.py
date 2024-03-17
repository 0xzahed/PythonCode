#1b
fee=int(input("Enter your semester fee:"))
result=float(input("Enter your CGPA (prev):"))
if result > 3.50:
   print( fee*(20/100))
elif result >= 3.00 and result <=3.50:
   print( fee*(10/100))
if result < 3.00:
   print( fee*(5/100))