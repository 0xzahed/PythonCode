def insert_Payment(Dic):
    for key,value in Dic.items():
        if value["plan"]=="basic":
            value["payment"]="$9.99"
        elif value["plan"]=="standard":
            value["payment"]="$15.99"
        elif value["plan"]=="premium":
            value["payment"]="$19.99"
    return Dic

def print_Payment(Dic):
    for key,value in Dic.items():
        print(f"Name:{value["name"]}  Have to pay:{value["payment"]}\n")

nasted_dic={}
count=1
while True:
    name=str(input("Enter name:"))
    name.lower()
    if name=="done":
        break
    plan=str(input("Enter plan:"))
    plan.lower()
    nasted_dic[count]={"name":name,"plan":plan}
    count+=1
print(nasted_dic)
final_dic=insert_Payment(nasted_dic)
print_Payment(final_dic)