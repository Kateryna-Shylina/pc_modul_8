from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if len(users) == 0:
        return {}

    noboirthdays = True
    result = {}
    
    if date.today().weekday() == 0:
        current_day = date.today() + timedelta(days=-2)
    else:
        current_day = date.today() 
    end_day = current_day + timedelta(days=6)
    
    days = list()
    months = set()
    day = current_day
    while day <= end_day:
         days.append(day.day)
         months.add(day.month)
         day += timedelta(days=1)
    
    for user in users:   
        if user.get('birthday').day in days and user.get('birthday').month in months:        
            fullname = user.get('name').split(' ')
            name = fullname[0]

            birthday = datetime(current_day.year, user.get('birthday').month, user.get('birthday').day).date() if current_day.year != end_day.year and user.get('birthday').month == 12 else datetime(end_day.year, user.get('birthday').month, user.get('birthday').day).date()
            
            if birthday.weekday() in [0, 5, 6]:  
                if "Monday" in result:
                    result["Monday"].append(name)
                else:
                    result["Monday"] = [name]  
            elif birthday.weekday() == 1:
                if "Tuesday" in result:
                    result["Tuesday"].append(name)
                else:
                    result["Tuesday"] = [name]
            elif birthday.weekday() == 2:
                if "Wednesday" in result:
                    result["Wednesday"].append(name)
                else:
                    result["Wednesday"] = [name]
            elif birthday.weekday() == 3:
                if "Thursday" in result:
                    result["Thursday"].append(name)
                else:
                    result["Thursday"] = [name]
            else:
                if "Friday" in result:
                    result["Friday"].append(name)
                else:
                    result["Friday"] = [name]

            noboirthdays = False

    if noboirthdays:
        return {}
    else:
        return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 31).date()},
        {"name": "Jany Koumy", "birthday": datetime(1976, 1, 3).date()},
        {"name": "BJan BKoum", "birthday": datetime(1976, 12, 30).date()},
        {"name": "DonJan DonKoum", "birthday": datetime(1976, 1, 5).date()},
        {'name': 'John', 'birthday': datetime(2023, 12, 31).date()}, 
        {'name': 'Doe', 'birthday': datetime(2024, 1, 1).date()}, 
        {'name': 'Alice', 'birthday': datetime(2023, 12, 29).date()},
    ]
    
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")



    