#Librerias
#-----------------------------------------------------------------------------------------------------------------------------------------------------
import ctypes

from calculadora import *
from dataAnalisys import *

from tkinter import ttk, messagebox, filedialog
from pandastable import Table, TableModel
from PIL import Image, ImageTk


#Variables globales:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
ruta_carpeta = "/Users/gabri/OneDrive/Escritorio/PROYECTO/archivos"

meses       = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre"]
nDiasMeeses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
categoria   = ["Transporte", "Comida", "Entretenimiento", "Impuestos", "Servicios públicos", "Otros"]
bancos      = ["BAC ahorros","BAC cred", "BCR ahorros", "BCR cred", "PROMERICA" ]
opcionesFil = ["Última semana", "Último mes", "Último año"]

lastLine=20
