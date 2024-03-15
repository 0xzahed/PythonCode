def main():
    k = [1001,1002,1003,1004,1005]
    v= ["USA","Canada","China","Japan","UK"]
    dict1 = dictonary(k,v)
    for i in dict1:
        print(i,dict1[i],sep=" = ")

def dictonary(list1,list2):
    dctnry = dict()
    for i in range(len(list1)):
        dctnry[list1[i]] = list2[i]
    return dctnry
main()

def main():
    d = [181,178,187,182,192,189,202,201]
    print(d)
    
    tlist = reverselist(d)
    print(tlist)

    tlist = sortedlist(d)
    print(tlist)

def reverselist(list1):
    list1.reverse()
    return list1

def sortedlist(list2):
    list2.sort()
    return list2
main()


value  = [1,2,3,4,5,6,7,8,9]
value2 = [1,2,3]
for item in value:
    if item==5:
        continue
    print("break")
    for item2 in value2:
        print(item,item2)
fee = int(input("Enter semester fee: "))
result = float(input("Enter CGPA: "))

if result > 3.50:
    print("Net Waiver Amount:",round(fee*(20/100),2))
elif result >= 3.00 and result <=3.50:
    print("Net Waiver Amount:",round(fee*(10/100),2))
elif result < 3.00:
    print("Net Waiver Amount:",round(fee*(5/100),2))

list1 = []
count = 1
while count <= 100:
    if count%2==1:
        list1.append(count)
    count+=1
print(list1)

list1 = ["India","Thailand","Bhutan","China","Nepal","Myanmar"]
print(list1)
list1.remove("Myanmar")
for name in list1:
    print(name)


list1 = [1,2,3]
list2 = [2,4,5,2]
list3 = []

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            list3.append(item1)

print(list3)


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