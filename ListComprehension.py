num = [1,2,3,4,5]
#for i in num:
   # print(i*2)

double = [i * 2 for i in num]
print(double)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
   newlist.append(x)

print(newlist)

# Convert upper & lower Case

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.lower() for x in fruits] # x.upper

print(newlist)