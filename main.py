import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):  
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)