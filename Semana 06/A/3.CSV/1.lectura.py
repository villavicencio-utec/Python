import pandas as pd
import matplotlib.pyplot as plt

# lee el archivo CSV
df = pd.read_csv("documento.csv")
print(type(df))

# muestra las primeras filas
print(df.head())
#
# Acceso por posición de filas
print(df[:])
#
# # Acceso por columnas
print(df[["fecha", "estado", "minsa"]])

# #Filtrado
filter = df['estado'] == "disponible"
df_enuso = df.where(filter).dropna()
print(df_enuso)

# Agrupar datos en base a los valores de una columna
grouped_data = df.groupby('estado')
#
# Obtener estadisticas basicas
print(grouped_data.describe())
# Otras funciones:  count(), sum(), mean(), std(), min(), max()
print(grouped_data.max())

#
#
# # Agrupar datos y filtrar columna
minsa = df.groupby('estado')['minsa']
print(minsa.describe())
#
# #graficos
#
minsa_resume = df.groupby('estado')['minsa'].sum()
print(minsa_resume)
minsa_resume.plot(kind='bar')
plt.title('Plot de barras.')
plt.savefig('plot_image.png')
plt.show()
#minsa_resume.plot(kind='bar')
