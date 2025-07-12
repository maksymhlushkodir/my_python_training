import pandas as pd
import matplotlib.pyplot as plt

data = {'Ім\'я': ['Анна', 'Богдан', 'Катя'], 'Оцінка': [85, 92, 78]}
df = pd.DataFrame(data)

df.plot.bar(x='Ім\'я', y='Оцінка', color='violet')
plt.title('Оцінки студентів')
plt.show()