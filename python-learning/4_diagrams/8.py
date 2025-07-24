import pandas as pd
import matplotlib.pyplot as plt

films_ratings = { 'films' : ['Форсаж 9', 'Дюна', 'Оппенгеймер', 'Барбі', 'Титанік'],
          'ratings' : [6.5, 8.0, 8.5, 7.3, 9.2]}

df = pd.DataFrame(films_ratings)

df.plot.bar(x='films', y='ratings', color='violet')
plt.title('films/ratings')
plt.show()