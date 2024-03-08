semester_fee = float(input("Enter your semester fee: "))
cgpa = float(input("Enter your CGPA: "))

if cgpa > 3.50:
    waiver_percent = 20
elif 3.00 <= cgpa <= 3.50:
    waiver_percent = 10
else:
    waiver_percent = 5

Waiver_Amount = (waiver_percent / 100) * semester_fee

print("Net waiver amount: ", Waiver_Amount)
