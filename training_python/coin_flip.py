import random
import matplotlib.pyplot as plt

# Підкидаємо монетку 100 разів і зберігаємо результати
results = [random.choice(["Орел", "Решка"]) for _ in range(100)]

# Рахуємо кількість "Орел" і "Решка"
count_orel = results.count("Орел")
count_reshka = results.count("Решка")

# Виводимо результати
print("Орел:", count_orel, "разів")
print("Решка:", count_reshka, "разів")

# Будуємо гістограму
plt.hist(results, bins=2, edgecolor="black", color="skyblue")
plt.title("Частота випадання")
plt.xlabel("Результат підкидання")
plt.ylabel("Кількість")
plt.xticks([0.25, 0.75], ["Орел", "Решка"])  # Підписи під стовпцями
plt.show()