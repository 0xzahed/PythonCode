x = int(input("Enter number of element:"))
list1 = []
for _ in range(x):
    list1.append(int(input()))

if x>=2:
    list1.remove(list1[0])
    list1.remove(list1[-1])
    print(list1)
else:
    print("Not Possible")