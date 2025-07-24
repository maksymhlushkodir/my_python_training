import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'name' : ['maksym','massi','gatto','naoufal','daniel','pippo'],
        'vuoti' : [90, 100, 85, 90, 78, 70]}

df = pd.DataFrame(data)

df.plot.bar(x='name', y='vuoti', color='skyblue')
plt.title('scrutini')
plt.show()