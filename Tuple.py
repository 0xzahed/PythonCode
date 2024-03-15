# eta ekti data type
# list e amra [] braket use krtam ar etay () er moddhe rakhte hoy ar eti changable na

newtuple = (1,2,3,4,6,5,7,8,88,99)
print(type(newtuple))
print(newtuple)
# index janar jonno but eti chng kora possible na
"""
newtuple[1] = 20 
print(newtuple)

"""

# negative index jodi -1 likhi taile last er data k print krbe

"""
print(newtuple[-1])
"""
# range of index first er jeta nibo sudhu oita include hobe but last er tar ager obdi kaj krbe
print(newtuple[2:4])

# change tuple item first  conver krte hbe list e 

x = list(newtuple)
print(type(list(newtuple))) #type janar jonno
x.append("hello")# append er maddhome item add hoy ekdom last e

# x[1] = "Good Bye" # for chnage variable

newtuple = tuple(x)

print(newtuple)