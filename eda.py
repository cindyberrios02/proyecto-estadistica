import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('datos_rendimiento.csv')

# Análisis exploratorio de datos
print(data.describe())

# Histograma de todas las variables
data.hist(bins=50, figsize=(20, 15))
plt.savefig('histograma_datos.png')
print("Histograma guardado como 'histograma_datos.png'")

# Correlación entre variables
corr_matrix = data.corr()
print(corr_matrix)

# Guardar la matriz de correlación como una imagen
plt.figure(figsize=(10, 8))
plt.matshow(corr_matrix, fignum=1)
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.colorbar()
plt.savefig('matriz_correlacion.png')
print("Matriz de correlación guardada como 'matriz_correlacion.png'")
