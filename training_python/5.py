import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------------------------------------------------------------------

names = ["Анна", "Богдан", "Катя", "Дмитро", "Олена"]
grades = [85, 92, 78, 60, 95]
study_hours = [10, 12, 8, 5, 15]

#----------------------------------------------------------------------

names = np.array(names)
grades = np.array(grades)
study_hours = np.array(study_hours)

#----------------------------------------------------------------------

df = pd.DataFrame({
    'names' : names,
    'grades' : grades,
    'study_hours' : study_hours
})

print("-------------data-------------")
print(df)

print("\n---Студенти з оцінкою > 80---")
print(df[df['grades'] > 80])

print("\n---Студенти з годинами < 10---")
print(df[df['study_hours'] < 10])

# Графік: імена по X, оцінки по Y
df.plot(
    x='names',
    y='grades',
    kind='bar',
    legend=False,
    color='violet'
)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()