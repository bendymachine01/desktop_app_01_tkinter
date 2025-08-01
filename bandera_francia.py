# Se importa la librería tkinter con todas sus funciones
from tkinter import *

# ---------------------------------------
# Funciones de la app
# ---------------------------------------


# -----------------------------------------
# Ventana principal de la app
# ------------------------------------------

# Se declara una variable llamada ventana_principal que adquiere las características de un objeto de tipo Tk
ventana_principal = Tk()

# Título de la ventana 
ventana_principal.title("bandera de francia")

# Tamaño de la ventana
ventana_principal.geometry("800x500")

# Deshabilitar botón maximizar de la ventana
ventana_principal.resizable(0, 0)

# Color de fondo de la ventana 
ventana_principal.config(bg="purple")

# --------------------------------
# Frame 1 
# --------------------------------
frame_1 = Frame(ventana_principal)
frame_1.config(bg="blue", width=260, height=480)
frame_1.place(x=10, y=10)

# --------------------------------
# Frame 2 
# --------------------------------
frame_2 = Frame(ventana_principal)
frame_2.config(bg="white", width=260, height=480)
frame_2.place(x=270, y=10)

# --------------------------------
# Frame 3
# --------------------------------
frame_3 = Frame(ventana_principal)
frame_3.config(bg="red", width=260, height=480)
frame_3.place(x=530, y=10)

# Método principal que despliega la ventana de pantalla
ventana_principal.mainloop()