user=[]
Pass=[]
admin={"Iamadmin":"123"}
print("resistation List:")
while True:
    name=str(input("Enter User name:"))
    if name=="done":
        break
    pas = str(input("Enter password:"))
    user.append(name)
    Pass.append(pas)
User={}
for i in range(len(user)):
    User[user[i]]=Pass[i]

print("Login Page:")

while True:
    U=str(input("Enter User name:"))
    P = str(input("Enter password:"))
    if U in User and User[U]==P:
        print("Login successfully.")
        break
    elif U in admin and admin[U] == P:
        print("Login successfully.")
        break
    else:
        print("Worng Password.Please try again")