List1 = ["Zahed","Hamja","Shakib"]
List2 = ["Google","Microsoft","Amazon"]

print(list (zip(List1,List2))) # zip fuinction diye duita list combine kore ek sthe kora jay eti tuple type print kore

user_name = ["healthMin", "reliefkin", "FoodMin", "admin"]
password = ["123health", "456 relief", "789food", "imadmin:123"]

# Convert username and password into pairs
credentials = dict(zip(user_name, password))
print(credentials)