import random
import matplotlib.pyplot as plt

dice_rolls = [random.randint(1 ,6) for i in range(10)]
print("Киди кубика:", dice_rolls)

plt.hist(dice_rolls, bins=6, edgecolor="black", color="violet")
plt.title("Частота випадання чисел на кубику")
plt.xlabel("Число")
plt.ylabel("Кількість")
plt.show()