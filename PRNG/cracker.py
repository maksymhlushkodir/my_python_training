import random
import time

def crack(target_password, approx_time):
    for possible_seed in range(approx_time - 10, approx_time + 10):
        random.seed(possible_seed)
        if random.randint(100000, 999999) == target_password:
            print("Found seed:", possible_seed)
            return possible_seed
    print("Seed not found.")
    return None

# Дані отримані від жертви :)
known_password = int(input("Enter the known password: "))
approx_time = int(input("Enter the approx generation time: "))  # наприклад: 1718123456

crack(known_password, approx_time)
