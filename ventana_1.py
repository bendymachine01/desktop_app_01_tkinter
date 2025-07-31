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

# metodo principal que despliega la ventana de pantalla
ventana_principal.mainloop()