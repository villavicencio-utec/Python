import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("documento.csv")

print(type(df))

#muestra las primeras filas
print(df.head())

# Acceso por posición de filas
print(df[1:2])

# Acceso por columnas
print(df[["fecha","estado", "minsa","total"]])


#Filtrado
filter = df['total'] > 598.0
df_enuso = df.where(filter)
df_enuso = df_enuso.dropna()
print(df_enuso)

# Agrupar datos en base a los valores de una columna
minsa = df.groupby('estado')["ffaa_pnp"]
#print(minsa.describe())
print(minsa.mean())

# # Agrupar datos y filtrar columna
# minsa = df.groupby('estado')['minsa']
# print(minsa.describe())


minsa_resume = df.groupby('estado')['minsa'].sum()
minsa_resume.plot(kind='bar')
plt.title('Plot de barras.')
plt.savefig('imagenGuardad.png')
plt.show()
