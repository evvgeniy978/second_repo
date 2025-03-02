def get_cats_info(file_path):
    cats_info = []  # Список для зберігання інформації про котів
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві пробіли та розбиваємо рядок за комою
                id, name, age = line.strip().split(',')
                # Створюємо словник для кожного кота
                cat = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                # Додаємо словник до списку
                cats_info.append(cat)
        
        return cats_info
    
    except FileNotFoundError:
        print("Файл не знайдено!")
        return []
    except ValueError:
        print("Помилка в форматі даних у файлі!")
        return []

# Шлях до файлу
file_path = "cats_file.txt"

# Виклик функції та виведення результатів
cats = get_cats_info(file_path)
print(cats)