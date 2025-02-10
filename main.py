from datetime import datetime
def get_days_from_today(date: str) -> int:
    try:
        arbitrary_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        days_difference = (arbitrary_date - today_date).days
        return days_difference
        
    except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
print(get_days_from_today("2022-02-03")) 