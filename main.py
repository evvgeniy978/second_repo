import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if not (1 <= min < max <= 1000) or not (min <= quantity <= max):
        return []  
    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("your lottery numbers:", lottery_numbers)