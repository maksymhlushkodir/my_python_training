import random

import matplotlib.pyplot as plt

cities = ["Київ", "Львів", "Одеса", "Харків"]
rainfall = {city : random.randint(0 , 100) for city in cities}

plt.bar(rainfall.keys(), rainfall.values(), color="teal")
plt.title("Рівень опадів по містах (мм)")
plt.ylabel("Опади")
plt.show()
