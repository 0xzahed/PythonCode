def Element_Number(user_number):
    d = {}
    # size = int(input("Enter Elemnt: "))
    for i in range(user_number):
        Number = input("Nasted :")
        Dict={}
        Size = int(input("Enter Element: "))
        for j in range(Size):
            Name = input("Enter Name: ")
            Plan = input("Enter Value: ")
            Dict[Name] = Plan
            d[Number]= Dict
    print(d)
user_number=int(input("Enter Number :"))
Element_Number(user_number)
    