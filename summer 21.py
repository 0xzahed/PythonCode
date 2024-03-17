List1=["Shikha","Haua","Muzam","01971700130"]
sum=0
Vow=0
for i in List1:
    sum+=len(i)
    for j in i:
        if j.lower() in ("a","e","i","o","u"):
            Vow+=1

print("Number of Charecter:",sum)
print("Num of vowel:",Vow)

List=[]
for i in range(20,61):
    if i%2==0 or i%5==0:
        if i%2==0:
            i+=5
        if i%5==0:
            i+=2
        List.append(i)

print(List)