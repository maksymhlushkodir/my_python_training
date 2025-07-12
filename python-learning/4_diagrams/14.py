import matplotlib.pyplot as plt

anime = ["RE:ZERO", "Jojo", "GTO", "SAO", "Baki", "Dr.Stone", "Dead-Note", "Frieren"]
estimates = [101, 98, 75, 25, 69, 80, 101, 87]

plt.bar(anime, estimates, color='red')
plt.title("Anime")
plt.ylabel("points")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()