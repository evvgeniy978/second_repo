def total_salary(file_path):
    total = 0
    count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ім'я та зарплату за комою
                name, salary = line.strip().split(', ')
                # Конвертуємо зарплату в число (int) і додаємо до загальної суми
                total += int(salary)
                count += 1
        
        # Обчислюємо середню зарплату
        average = total / count if count > 0 else 0
        
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено!")
        return 0, 0
    except ValueError:
        print("Помилка в форматі даних у файлі!")
        return 0, 0

# Шлях до файлу
file_path = "salary.txt"

# Виклик функції та виведення результатів
total, average = total_salary(file_path)
print(f"Зарплата сума заробленої плати: {total}, Середня зароблена плата: {average}")