#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                 🚗🚗🚗 TKINTER MILE-KM CONVERTER 🚗🚗🚗
Pasos.
1. Utiliza la libreria tkinter para crear un conversor de km a millas bien bonito.
2. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

from tkinter import *

# CONFIGURACION DE LA VENTANA.
window = Tk()
window.title("Conversor Millas - Km")
window.config(padx = 20, pady = 20)

# FUNCIONES.
def millas_a_km():
    millas = float(input_millas.get())
    km = millas * 1.60934
    label_resultado.config(text = round(km, 1))
 
# CONFIGURACION Y PSICIONAMIENTO DE LOS WIDGETS.
input_millas = Entry(text = "0", width = 9)
input_millas.insert(END, "0")
input_millas.grid(column = 1, row = 0)

label_millas = Label(text = "Millas")
label_millas.grid(column = 2, row = 0)

label_igual = Label(text = "es igual a")
label_igual.grid(column = 0, row = 1)

label_resultado = Label(text = "0")
label_resultado.grid(column = 1, row = 1)
    
label_kms = Label(text = "Kms")
label_kms.grid(column = 2, row = 1)

boton_convertir = Button(text = "Convertir", command = millas_a_km)
boton_convertir.grid(column = 1, row = 2)

# TERMINA EL BUCLE DE LA VENTANA.
window.mainloop()