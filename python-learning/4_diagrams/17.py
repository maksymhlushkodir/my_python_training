# КОМЕНТИ!!!!!!
import matplotlib.pyplot as plt

language = ['python', 'java', 'C#']
hours_week = [7, 14, 21]

plt.pie(hours_week, labels=language, shadow=True, autopct="%1.1f%%", startangle=90)
plt.title('hours_week')
plt.show()