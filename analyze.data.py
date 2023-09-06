import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

transformed_sales_df = pd.read_csv("transformed_sales_data.csv")
transformed_marketing_df = pd.read_csv("transformed_marketing_data.csv")

sales_stats = transformed_sales_df.describe()
marketing_stats = transformed_marketing_df.describe()



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Grafico de barras ROI promedio por mes
sns.barplot(x="month", y="ROI", data=transformed_marketing_df, ax=ax1)
ax1.set_xlabel("Mes")
ax1.set_ylabel("ROI Promedio")
ax1.set_title("ROI Promedio por Mes")
ax1.tick_params(axis='x', rotation=45)

# Grafico de barras agrupadas de ingresos por mes y producto
sns.barplot(x="month", y="revenue", hue="product", data=transformed_sales_df, ax=ax2)
ax2.set_xlabel("Mes")
ax2.set_ylabel("Ingresos")
ax2.set_title("Ingresos por Mes y Producto")
ax2.tick_params(axis='x', rotation=45)
ax2.legend(title="Producto")

# Ajustar el espaciado entre subtramas
plt.tight_layout()

# Mostrar ambos gráficos en simultáneo
plt.show()



