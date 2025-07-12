import pandas as pd
import matplotlib.pyplot as plt

games = ['Minecraft', 'Stalker 2', 'Dota 2', 'Cs go', 'Kindom rush', 'Much']
estimates = [100, 90, -20, 78, 68, 54]

df = pd.DataFrame({
    'games' : games,
    'estimates' : estimates
})

df.plot.bar(x='games', y='estimates', color='violet')
plt.title('Rating of games')
plt.ylabel('points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()