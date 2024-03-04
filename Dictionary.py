N = {1,2,3,7} | {2,3,7}

print(N)


# Dictionary

d = {}
Size = int(input("Enter The Size Of Element :"))

for i in range(Size):
    key = input("Enter The Name :")
    value = input("Enter The Value :")
    d[key] = value
print("Dictionary", d)