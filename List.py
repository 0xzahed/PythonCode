# list add korar somy obossoi [] ei braket use korte hbe
# etake c te array bola hoy
# type dekhar jonno print(type(li)) korte hoy
# and ei list thke jekono value chng kora jay 

# integer value
li = [1,2,3]

print(li)
li[1] = 20
print(li)

# string value

name = ["Zahed","Shakib", "Hamja", "Faysal"]
print(name)
print(type(name))

# change value
name[2] = "hello"
print(name)


# List Item Access

names = ["Zahed", "Shakib", "Hamja", "Faysal"]
print(names[2])

#change List iitem

names[3] = "Good Bye"

print(names)

# add List Item

names.append(10)
print(names)

# Insert

names.insert(4,"Hello world") # j index select korbo sei indexe eti add hobe and age jeta chilo seta pore pathay dibe
print(names)

# remove item from this list for spacific dlt index

newlist = ["Zahed","hamja", "Shakib", 212]
print(newlist)
"""
newlist.remove("Shakib")
print(newlist)

# pop() method poper modde kono index nnumber na dile direct last index dlt kore dey

#newlist.pop(2)
#newlist.pop(1)
print(newlist)
"""
# del keyword

del newlist[1]
print(newlist)

# clear method joto item thkbe sob remove hye jabe

newlist.clear()

print(newlist)

# user input

List = []

Size = int(input("Enter The Value :"))

for i in range(Size):
    List.append(input())
print(List)


