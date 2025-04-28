# Auto-generated script file
# by Google Colab

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('{file_name}')

# Tambahkan kolom
df['unit_price'] = df['sales_amount'] / df['quantity']
df['discount'] = 0
df['tax_amount'] = df['sales_amount'] * 0.1

def format_rupiah(x):
    return f"Rp{x:,.0f}".replace(",", ".")

df['sales_amount_rupiah'] = df['sales_amount'].apply(format_rupiah)
df['unit_price_rupiah'] = df['unit_price'].apply(format_rupiah)
df['tax_amount_rupiah'] = df['tax_amount'].apply(format_rupiah)

# Analisis
total_sales = df['sales_amount'].sum()
average_sales = df['sales_amount'].mean()
highest_sales = df['sales_amount'].max()

# Cetak hasil
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales:", highest_sales)

# Grafik
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sales_amount'], marker='o')
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Sales Amount (Rp)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()
