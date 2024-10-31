#Importamos la libreria de Pandas, que es fundamental para análisis de datos 
import pandas as pd 
# Define la ruta del archivo CSV que contiene los datos 
# Si el archivo está en el mismo directorio basta con poner el nombre del archivo 
path = "Sesion_2/Online_Retail.csv"
dragon_data = pd.read_csv(path, encoding='latin1')
print(type(dragon_data))
print(dragon_data.head())





