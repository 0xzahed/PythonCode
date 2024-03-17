#1c
n=1
odd_list=[]
while n<=100:
    if n%2!=0:
        odd_list.append(n)
    n+=1
print(odd_list)


odd=[item for item in range(1,101) if item % 2 !=0]
print(odd)

#2a
travel_country=["india","Thailand","Bhutan","China","Nepal","Myanmar"]
travel_country.remove("Myanmar")
for i in travel_country:
    print(i)