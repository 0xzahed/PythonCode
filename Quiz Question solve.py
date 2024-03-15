List = ["February","March","April","May","June","July","August","September","october","November","December"]


def check_day(day):
    if day == "September":
        return "Mid-Term Month"
    else:
        return "Study Hard For The Next Examination"

def add_missing_days(List):
    days_list.insert(0, "january")  
    days_list.insert(6, "July")  

add_missing_days(List)

print(check_day("September"))  
print(check_day("Friday")) 