import matplotlib.pyplot as plt

absurdity = ['Crocodilo-bambardiro', 'Lililiralila', 'Tung-tung-tung-sagur', 'capucino asasino']
absurdity_numbers = [100, 100, 100, 100]

plt.bar(absurdity, absurdity_numbers, color='orange')
plt.title('absurdity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()