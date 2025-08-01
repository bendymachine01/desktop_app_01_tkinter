# Se importa la librería tkinter con todas sus funciones
from tkinter import *

# ---------------------------------------
# Funciones de la app
# ---------------------------------------


# -----------------------------------------
# Ventana principal de la app
# ------------------------------------------

# Se declara una variable llamada ventana_principal que adquiere las características de un objeto de tipo Tkinte
ventana_principal = Tk()

# Título de la ventana 
ventana_principal.title("bandera de noruega")

# Tamaño de la ventana
ventana_principal.geometry("800x500")

# Deshabilitar botón maximizar de la ventana
ventana_principal.resizable(0, 0)

# Color de fondo de la ventana 
ventana_principal.config(bg="purple")

# --------------------------------
# Fondo rojo (Bandera base)
# --------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=780, height=480)
frame_rojo.place(x=10, y=10)

# --------------------------------
# Cruz blanca vertical
# --------------------------------
cruz_blanca_vertical = Frame(ventana_principal)
cruz_blanca_vertical.config(bg="white", width=60, height=40)
cruz_blanca_vertical.place(x=220, y=10)

# --------------------------------
# Cruz blanca horizontal
# --------------------------------
cruz_blanca_horizontal = Frame(ventana_principal)
cruz_blanca_horizontal.config(bg="white", width=780, height=60)
cruz_blanca_horizontal.place(x=10, y=180)

# --------------------------------
# Cruz azul vertical
# --------------------------------
cruz_azul_vertical = Frame(ventana_principal)
cruz_azul_vertical.config(bg="blue", width=30, height=480)
cruz_azul_vertical.place(x=235, y=10)

# --------------------------------
# Cruz azul horizontal
# --------------------------------
cruz_azul_horizontal = Frame(ventana_principal)
cruz_azul_horizontal.config(bg="blue", width=780, height=30)
cruz_azul_horizontal.place(x=10, y=195)

# Método principal que despliega la ventana de pantalla
ventana_principal.mainloop()
