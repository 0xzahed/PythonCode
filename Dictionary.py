"""
# Dictionary
d = {}
Size = int(input("Enter The Size Of Element :"))
for i in range(Size):
    key = input("Enter The Name :")
    value = input("Enter The Value :")
    d[key] = value
print("Dictionary", d)"""

# Cretae Dictionary

Dictionary = {
    "Name" : "Abu Zahed",
    "Age"  : 23,
    "City" : "Bogura",
    "Country" : "Bangladesh"
}

print(Dictionary)


# Dictionary Length

print("Length :", len(Dictionary))

# Dictionary Constructior

NewDict = dict(Name="Zahed",Age=23,City="Bogura")
print(NewDict)


#Create User Input In Dictionary
"""
Dict = {}

Size = int(input("Enter Element Of Dictionary :"))
for i in range(Size):
    Key = input("Enter Key Of Dictionary :")
    Value = input("Enter Value Of Dictionary :")
    Dict[Key] = Value
print("Value Of This Dictionary :",Dict)"""

# Access Item
x = Dictionary["Name"]
print(x)

# Also Use Get Method

Y = Dictionary.get("Name")
print(Y)

#Get Keys

A = Dictionary.keys()
print(A)
B = Dictionary.values()
print(B)

# Key Exist Or Not

if "Name" in Dictionary:
    print("Yes")
else:
    print("Invalid!")

# Change Values
       
Dictionary["Age"]= 25

print("After Change-->",Dictionary)

# Update Keys And Values

Dictionary.update({"City":"Dhaka"})
print("After Update-->",Dictionary)

# Add Dictionary

Dictionary["Region"] = "Rajshahi"
print("After Adding New Value-->",Dictionary)

# Remove Using pop

Dictionary.pop("Name")
print(Dictionary)

Dictionary.popitem()
print("After Remove Item",Dictionary)

# Using Del keyword

del Dictionary["City"]
print(Dictionary)

Dictionary.clear()
print("After Remove All Value....",Dictionary)

# Loop

for N in Dictionary:
    print(Dictionary[N])

