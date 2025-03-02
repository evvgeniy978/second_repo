
def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = [int(line.strip().split(",")[1]) for line in file if line.strip()]
        
        total = sum(salaries)
        average = total // len(salaries) if salaries else 0
        
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")