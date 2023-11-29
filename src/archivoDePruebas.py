"""import tkinter as tk
from tkinter import ttk

def mostrar_contenido(event):
    current_tab = notebook.index(notebook.select())
    if current_tab == 0:
        label_texto.config(text="Contenido de la Pestaña 1")
    elif current_tab == 1:
        label_texto.config(text="Contenido de la Pestaña 2")
    elif current_tab == 2:
        label_texto.config(text="Contenido de la Pestaña 3")

# Crear la ventana principal
root = tk.Tk()
root.title("Notebook con Tkinter")
root.geometry("400x300")

# Crear el notebook (pestañas)
notebook = ttk.Notebook(root)

# Pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Agregar pestañas al notebook
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')
notebook.add(tab3, text='Pestaña 3')

notebook.pack(expand=1, fill="both")

# Contenido de las pestañas
label_texto = tk.Label(root, text="", width=30)
label_texto.pack()

# Manejar evento al cambiar de pestaña
notebook.bind("<<NotebookTabChanged>>", mostrar_contenido)

root.mainloop()
"""
import pandas as pd
import matplotlib.pyplot as plt

# Supongamos que tienes un DataFrame llamado 'df' con una columna de fechas 'Fecha' y otra de gastos 'Gasto'
# Asegúrate de tener estas dos columnas en tu DataFrame

# Ejemplo de cómo podría ser tu DataFrame
data = {'Fecha': ['2022-01-15', '2022-02-20', '2022-03-10', '2023-01-05', '2023-02-18'],
        'Gasto': [100, 150, 200, 120, 180]}

df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])  # Asegúrate de que la columna de fechas sea de tipo datetime

# Agrupa los datos por mes y suma los gastos
df['Mes'] = df['Fecha'].dt.to_period('M')  # Agrega una columna de Mes
gastos_por_mes = df.groupby('Mes')['Gasto'].sum()

# Crea un gráfico de barras para visualizar los gastos por mes
plt.figure(figsize=(10, 6))
gastos_por_mes.plot(kind='bar', color='skyblue')
plt.title('Gasto por Mes')
plt.xlabel('Mes')
plt.ylabel('Gasto ($)')
plt.show()
