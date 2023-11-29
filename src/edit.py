from header import *
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def borrar_contenido_archivo(nombre_archivo):
    texto = f"¿Está seguro que desea eliminar el contenido del archivo {nombre_archivo}"
    response = messagebox.askyesno("PREGUNTA", texto)

    if response:
        # Abre el archivo en modo escritura ("w") para truncar su contenido
        with open(nombre_archivo, "w") as archivo:
            archivo.truncate(0)
        texto = f"Contenido de '{nombre_archivo}' ha sido eliminado."
        messagebox.showinfo("EXITO", texto)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Eliminar concepto:
def eliminar_Valor(filename= "conceptosGuardados.txt"):
    valor_combobox = combo.get()
    print(valor_combobox,conceptosGuardados[valor_combobox])
    try:
        texto_a_eliminar = f"{valor_combobox}:{conceptosGuardados[valor_combobox]}"  # Texto específico que deseas eliminar
    except:
        messagebox.showerror("ERROR", "No se pudieron eliminar los datos")
    else:
        with open(filename, 'r') as file:
            lineas = file.readlines()

        # Filtrar las líneas que no contienen el texto a eliminar
        lineas_actualizadas = [linea for linea in lineas if texto_a_eliminar not in linea]

        # Escribir el contenido actualizado al archivo
        with open(filename, 'w') as file:
            file.writelines(lineas_actualizadas)
        
        #Actualizar conceptos:
        messagebox.showinfo("Exito", "Se eliminaron los datos existosamente.")
        ventana.destroy()
        
# Crear la ventana principal
def eliminarConcepto():
    global combo, ventana, conceptosGuardados

    ventana = Toplevel()
    ventana.resizable(False, False)
    ventana.iconbitmap("iconos/icon.ico")
    ventana.title("Eliminar concepto")
    conceptosGuardados=readSavedConcepts()

    # Crear el Combobox
    comboLabel =Label(ventana, text=" •Concepto a eliminar: ")
    comboLabel.grid(row=1, column=0, sticky="w")

    combo = ttk.Combobox(ventana, values=list(conceptosGuardados.keys()))
    combo.grid(row=1, column=1)


    # Crear el botón "Continuar"
    boton_continuar = Button(ventana, text="Continuar", command=eliminar_Valor, bg="green", fg="white", width=20)
    boton_continuar.grid(row=2, column=1, pady=4)

    # Ejecutar la ventana
    ventana.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Guardar concepto:
def guardar_valor(filename= "conceptosGuardados.txt"):
    valor_entry = entry.get()
    valor_combobox = combo.get()
    conceptosGuardados=readSavedConcepts()

    if valor_entry not in conceptosGuardados:
        with open(filename, "a") as archivo:
            archivo.write(f"{valor_entry}:{valor_combobox}\n")
            messagebox.showinfo("Exito", "Se añadieron los datos existosamente.")
            ventana.destroy()
    else:
        messagebox.showerror("ERROR", "El concepto que intenta guardar ya está registrado")


# Crear la ventana principal
def guardarConcepto():
    global entry, combo, ventana

    ventana = Toplevel()
    ventana.resizable(False, False)
    ventana.iconbitmap("iconos/icon.ico")
    ventana.title("Guardar concepto")

    # Crear el Entry
    entryLabel =Label(ventana, text=" •Ingrese el concepto: ")
    entryLabel.grid(row=0, column=0, sticky="w")

    entry = Entry(ventana, width=23)
    entry.grid(row=0, column=1)

    # Crear el Combobox
    comboLabel =Label(ventana, text=" •Ingrese su categoría: ")
    comboLabel.grid(row=1, column=0, sticky="w")

    combo = ttk.Combobox(ventana, values=categoria)
    combo.grid(row=1, column=1)

    # Crear el botón "Continuar"
    boton_continuar = Button(ventana, text="Continuar", command=guardar_valor, bg="green", fg="white", width=20)
    boton_continuar.grid(row=2, column=1, pady=4)

    # Ejecutar la ventana
    ventana.mainloop()
