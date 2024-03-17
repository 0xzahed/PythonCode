# Dict = {}
# Size = int(input("outer: "))
# for i in range(Size):
#     Dict2={}
#     Key = input("Outer Key: ")
#     S = int(input("Inner Range: "))
#     for j in range(S):
#         K = input("Inner Key: ")
#         V = input("Inner Value: ")
#         Dict2[K] = V
#     Dict[Key] = Dict2
# print(Dict)

def insert_payment(Dict):
    for Key, value in Dict.items():
        if plan == "basic":
            value["Payment"]= "9.99$"
        elif plan == "standard":
            value["Payment"]= "15.99$"
        elif plan == "premium":
            value["Payment"]= "19.99$"
    return Dict

def Finalpayment(Dict):
    for key, value in Dict.items():
        print(f"Name:{name} have to pay {value["Payment"]}")

Dictionary = {}
count = 1

while True:
    name = str(input('Enter Name: '))
    name.lower()
    if name == "done":
        break
    plan = str(input("Enter Plan: "))
    plan.lower()
    Dictionary[count] = {"name": name, "plan": plan}
    count += 1

print(Dictionary)
finalpay = insert_payment(Dictionary)
Finalpayment(finalpay)


