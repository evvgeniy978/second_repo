from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        arbitrary_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        return (arbitrary_date - today_date).days
    except ValueError:
        return None  

print(get_days_from_today("2022-02-03")) 