# #2b
#
# List1=[1,2,3]
# List2=[2,4,5]
# common=[]
# for i in List1:
#     for j in List2:
#         if i==j:
#             common.append(i)
#
# if len(common)==0:
#     print("No common elements\n")
# else:
#     print(common)



#2c
n=int(input("Enter total element number:"))
List=[]
for i in range(n):
    a=int(input())
    List.append(a)

if n>2:
    List.pop(0)
    List.pop(-1)
    print(List)
else:
    print("Not Possible\n")