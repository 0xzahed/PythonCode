# set unchangable and sob gula data type dewa jabe
# ar same variable dewa jabena kaj suhdu unique variable kore

#set = {1,True,"String","String"}
"""
Set = set()
Size = int(input("Enter The Elemnt : "))
for i in range(Size):
    Value = input("Enter Value : ")
    Set.add(Value)
print(Set)"""

# Create Set

NewSet = {"Hi", "Hello", "Let's Go", "Good Bye","Hello"}
print(NewSet)

print(len(NewSet))
print(type(NewSet))

# Create Constructor

N = set(("Name","Age","District"))
print(N)

# Access Item In Set

if "Hello" in NewSet:
    print("Hello")
else:
    print("Invalid!!")

# Add Item
    
NewSet.add("Welcome")
print(NewSet)

# Update Set

MySet = {"Banana","Apple","Burger"}

NewSet.update(MySet)
print(NewSet)

# Remove Set Item

NewSet.remove("Banana")
print(NewSet)

NewSet.discard("Apple")
print(NewSet)

NewSet.pop()
print(NewSet)

NewSet.clear()
print(NewSet)

