import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd

#===<!dati!>===
data_shop = {'Продукт': ['Чіпси', 'Шоколад', 'Печиво'], 'Продажі': [150, 200, 75]}
df = pd.DataFrame(data_shop)

df.plot.bar(x='Продукт', y='Продажі', color='violet')
plt.title("shop_data")
plt.show()

pdf = FPDF
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Продажі за тиждень:", ln=True)
pdf.cell(200, 10, txt=df.to_string(), ln=True)
pdf.output(("sales_report.pdf"))