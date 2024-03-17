def Mid_Alart(L):
        L.lower()
        if L=="september":
            print("Mid-term month.\n")
        else :
            print("Study hard for the next examination.\n")

List=["february","March","April","May","June","August","September","October","November"]
List.insert(0,"January")
List.insert(6,"July")
List.insert(11,"December")
print(List)
M=str(input("Enter a month from given List:"))
Mid_Alart(M)