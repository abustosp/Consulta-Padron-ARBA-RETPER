import pandas as pd
import numpy as np
from time import time
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename


Excel = "Base-Clientes.xlsx"
Txt = askopenfilename(title="Seleccione el archivo de texto con el padrón de percepciones y retenciones", filetypes=[("Archivos de texto", "*.txt") , ("CSV" , "*.CSV") , ("Todos los archivos", "*.*")])
Titulos_Padron = ["Tipo" , "Fecha de Publicación" , "Desde" , "Hasta" , "CUIT" , "Tipo-Contr-Insc" , "Marca-Alta-Baja-Sujeto" , "Marca-cbio-AIícuota" , "Alícuota-Retención" , "Nro-Grupo-Percepción" , "Nro-Grupo-Retención" ]

# Inicio del proceso
Start = time()

# Leer el archivo de Excel con los CUITs a consultar
Clientes = pd.read_excel(Excel)

# Leer el archivo de texto con el padrón
Padron = pd.read_csv(Txt, sep=";" , header=None)

# Eliminar la ultima columna (vacía)
#Padron = Padron.drop(Padron.columns[-1], axis=1)

# Eliminar la primera fila
Padron.columns = Titulos_Padron

# Convertir el campo CUIT a Int64
Clientes["cuit"] = Clientes["cuit"].astype(str).replace("-","" , regex=True).astype(np.int64)

# Combinar los dos dataframes
Clientes = pd.merge(Clientes, 
                    Padron, 
                    left_on="cuit",
                    right_on="CUIT",
                    how="left")

# Exportar el resultado a un archivo de Excel
Clientes.to_excel("Clientes_Procesado.xlsx", index=False)

# Fin del proceso
End = time()

# Mostrar el tiempo de ejecución
showinfo("Fin del proceso", "El proceso ha finalizado en " + str(round(End - Start, 2)) + " segundos.")
