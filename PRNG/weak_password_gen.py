import random
import time

seed = int(time.time())
random.seed(seed)

password = random.randint(100000, 999999)  # "рандомний" 6-значний пароль
print("Seed:", seed)
print("Generated password:", password)
import random
import time

seed = int(time.time())
random.seed(seed)

password = random.randint(100000, 999999)  # "рандомний" 6-значний пароль
print("Seed:", seed)
print("Generated password:", password)
