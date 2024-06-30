# recopilacion_datos.py

import pandas as pd

# Cargar datos desde el archivo CSV existente
df = pd.read_csv('datos_recopilados.csv')

# Verificar que los datos se han cargado correctamente
print(df.head())

# Guardar los datos en un nuevo archivo CSV para confirmación
df.to_csv('datos_rendimiento.csv', index=False)
print("Datos cargados desde 'datos_recopilados.csv' y guardados en 'datos_rendimiento.csv'")
