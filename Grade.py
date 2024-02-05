marks = float(input("Enter your marks: "))

if 80 <= marks <= 100:
    grade = "A+"
elif 75 <= marks < 80:
    grade = "A"
elif 70 <= marks < 75:
    grade = "A-"
elif 65 <= marks < 70:
    grade = "B+"
elif 60 <= marks < 65:
    grade = "B"
elif 55 <= marks < 60:
    grade = "B-"
elif 50 <= marks < 55:
    grade = "C+"
elif 45 <= marks < 50:
    grade = "C"
elif 40 <= marks < 45:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
