import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):  
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
def get_euromillions_numbers():
    main_numbers = random.sample(range(1, 51), 5)  
    star_numbers = random.sample(range(1, 13), 2)  
   
    return sorted(main_numbers), sorted(star_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)  
main_nums, star_nums = get_euromillions_numbers()

print("Ваші числа для Євромільйон:")
print(f"Основні числа (5 чисел від 1 до 50): {main_nums}")
print(f"Зіркові числа (2 числа від 1 до 12): {star_nums}")