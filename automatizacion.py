import shutil

import pandas as pd

origen = r"C:\Users\harri\OneDrive\Documentos\base_de_datos_inventario.xlsx"
destino = r"C:\Users\harri\OneDrive\Escritorio\base_de_datos_inventario.xlsx"


df = pd.read_excel(origen)
print(df.head(10))

shutil.move(origen, destino)
print("Archivo movido con exito")
