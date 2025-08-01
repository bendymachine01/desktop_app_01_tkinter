# se importa la libreria tkinter con todas sus funciones 

from tkinter import *

# ---------------------------------------
# funciones de la app
# ---------------------------------------


# -----------------------------------------
# ventana principal de la app
#------------------------------------------

# se declara una variable llamada ventana principal que adquiere las caracteristicasde un objeto de tipo Tk

ventana_principal = Tk()

# titulo de la ventana 
ventana_principal.title("harold martinez")

# TAMAÑO DE LA VENTANA
ventana_principal.geometry("800x500")

# desabilitar boton maximisar de la ventana
ventana_principal.resizable(0,0)

# color de fonfo de la ventana 
ventana_principal.config(bg="purple")

# --------------------------------
# frame 1
# --------------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg= "yellow", width=780, height=240)
frame_1.place(x=10,y=10)

# --------------------------------
# frame 2
# --------------------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg= "blue", width=780, height=120)
frame_2.place(x=10,y=250)

# --------------------------------
# frame 3
# --------------------------------

frame_3 = Frame(ventana_principal)
frame_3.config(bg= "red", width=780, height=120)
frame_3.place(x=10,y=370)

# metodo principal que despliega la ventana de pantalla
ventana_principal.mainloop()
