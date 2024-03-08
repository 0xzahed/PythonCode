# 1, a

sum = 0
n = int(input("Case:"))

for i in range(n):
    x,y = input("enter 2 integer:").split()
    x = int(x); y = int(y)
    for j in range(x,(x+(y*2))):
        if j%2 != 0:
            sum = sum +j
    print(sum)