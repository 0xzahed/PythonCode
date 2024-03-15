d = {}
size = int(input("Enter Elemnt: "))

for i in range(size):
    Key = input()
    Dict={}
    Size = int(input("Enter Element: "))
    for j in range(Size):
        k = input("Enter Key: ")
        v = input("Enter Value: ")
        Dict[k] = v
        d[Key]= Dict
print(d)