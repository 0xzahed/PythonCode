days_of_week = ["Saturday", "Sunday", "Tuesday", "Thursday", "Friday"]

def check_day(day):
    if day == "Friday":
        return "Today is holiday"
    else:
        return "Working day"

def add_missing_days(days_list):
    days_list.insert(1, "Monday")  
    days_list.insert(3, "Wednesday")  

add_missing_days(days_of_week)

print(check_day("Saturday"))  
print(check_day("Friday"))    
