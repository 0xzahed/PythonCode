List1=["Shikha","Haua","Muzam","01971700130"]
# sum = 0
Vow = 0
# for i in List1:
#     sum+=len(i)
# print(sum)
for j in List1:
    for i in j:
        if i.lower() in ("a","e","i","o","u"):
            Vow+=len(i)
print(Vow)
      