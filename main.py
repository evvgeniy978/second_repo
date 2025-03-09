import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):  # Оновлена перевірка quantity
        return []
   
    # Генерація унікального набору чисел
    numbers = random.sample(range(min, max + 1), quantity)
   
    # Повернення відсортованого списку
    return sorted(numbers)

def get_euromillions_numbers():
    # Генерація 5 випадкових унікальних чисел від 1 до 50 для основних чисел
    main_numbers = random.sample(range(1, 51), 5)  # 5 чисел від 1 до 50
    # Генерація 2 випадкових унікальних чисел від 1 до 12 для "зіркових" чисел
    star_numbers = random.sample(range(1, 13), 2)  # 2 числа від 1 до 12
   
    return sorted(main_numbers), sorted(star_numbers)

# Приклад виклику функцій
lottery_numbers = get_numbers_ticket(1, 49, 6)  # Залишаємо для порівняння або іншого використання
main_nums, star_nums = get_euromillions_numbers()

# Виведення результатів у форматі, схожому на лотерею "Євромільйон"
print("Ваші числа для Євромільйон:")
print(f"Основні числа (5 чисел від 1 до 50): {main_nums}")
print(f"Зіркові числа (2 числа від 1 до 12): {star_nums}")