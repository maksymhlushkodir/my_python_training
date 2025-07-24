import matplotlib.pyplot as plt

my_love = ["Cat", "Pizza", "Code", "Anime", "Music"]
estimates = [80, 65, 87, 100, 95]

plt.pie(estimates, labels=my_love, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("love")
plt.show()