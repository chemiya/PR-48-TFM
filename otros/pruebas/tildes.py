import pandas as pd

# Crear un DataFrame de ejemplo con tildes
data = {'Nombre': ['Fran González', 'María López', 'Juan Pérez']}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV con codificación UTF-8
df.to_csv('archivo.csv', index=False, encoding='utf-8')

# Leer el archivo CSV para verificar que se guardaron correctamente
df_leido = pd.read_csv('archivo.csv')

# Mostrar el DataFrame leído
print(df_leido)
