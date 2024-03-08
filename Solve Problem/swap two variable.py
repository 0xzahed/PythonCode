x = int(input("Enter Number X: "))
y = int(input("Enter Number Y: "))

temp = x
print("Temp Is: ",temp)

x = y
print("X Is: ",x)
y=temp
print("Y Is: ",y)

# Swap Without Third Variable

x = int(input("Enter Number X: "))
y = int(input("Enter Number Y: "))

x,y = y,x
print("X Is: ",x)
print("Y Is: ",y)