#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                    🍅🍅🍅 TKINTER POMODORO APP 🍅🍅🍅
Pasos.
1. Configuracion de la UI.
2. Funcion para la cuenta atras.
3. Funcion para resetear el contador.
4. Prevenir bugs al dar click muchas veces.
5. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

from tkinter import *
from pygame import mixer
import math

# ---------------------------- VARIABLES -------------------------------
ROSA = "#e2979c"
ROJO = "#e7305b"
VERDE = "#9bdeac"
AMARILLO = "#f7f5dd"
TIPO_FUENTE = "Courier"
TAMANO_FUENTE = 25
MOD_FUENTE = "bold"
FUENTE = (TIPO_FUENTE, TAMANO_FUENTE, MOD_FUENTE)
MINUTOS_TRABAJO = 1
TIEMPO_DESCANSO_CORTO = 1
TIEMPO_DESCANSO_LARGO = 1

reps = 0
evento_contando = None

# ---------------------------- CONFIGURACION DE SONIDOS ----------------------------
mixer.init()
def lanza_sonido(sonido, volumen):
    mixer.music.load(sonido)
    mixer.music.set_volume(volumen)
    mixer.music.play()
    
    
# ---------------------------- MECANISMO DEL CONTADOR ------------------------------- 
# Función para comenzar la cuenta atrás. Decide si estamos en una fase de trabajo, descanso corto o descanso largo y lanza el contador.
def empieza_contador():
    global reps
    reps += 1
    segundos_de_trabajo = MINUTOS_TRABAJO * 60
    segundos_descanso_corto = TIEMPO_DESCANSO_CORTO * 60
    segundos_descanso_largo = TIEMPO_DESCANSO_LARGO * 60
    
    if reps % 8 == 0:
        window.attributes('-topmost',True)
        titulo.config(text = "Descanso", fg = ROJO)
        cuenta_atras(segundos_descanso_largo)
        reps = 0
    elif reps % 2 == 0:
        window.attributes('-topmost',True)
        titulo.config(text = "Descanso", fg = ROSA)
        cuenta_atras(segundos_descanso_corto)
    else:
        window.attributes('-topmost',False)
        titulo.config(text = "Trabajo", fg = VERDE)
        cuenta_atras(segundos_de_trabajo)
        
    lanza_sonido("Campana.wav", 0.5)


# ---------------------------- CUENTA ATRAS -------------------------------  
# Gestiona la cuenta atrás hasta llegar a 0 y lanzar el siguiente pomodoro. 
def cuenta_atras(tiempo):
    global reps
    global evento_contando
    minutos = math.floor(tiempo / 60)
    segundos = tiempo%60
    if segundos < 10:
        segundos = f"0{segundos}"
    tiempo_restante = f"{minutos}:{segundos}"
       
    #Actualiza el contador y vuelve a llamar la funcion hasta que se acabe el tiempo.
    canvas.itemconfig(texto_contador, text = tiempo_restante)
    if tiempo > 0:
        evento_contando = window.after(100,cuenta_atras,tiempo - 1)
    else:
        empieza_contador()
        # Iteramos por la cantidad de veces que hemos completado un ciclo para añadir un tic.
        tics = ""
        sesiones_de_trabajo = math.floor(reps / 2)
        for _ in range(sesiones_de_trabajo):
            tics += "✔"
        checks.config(text = tics)
        

# ---------------------------- RESETEO DEL CONTADOR ------------------------------- 
# Resetea el contador y todas las variables implicadas.
def reseteo_contador():
    global reps
    reps = 0
    window.after_cancel(evento_contando)
    canvas.itemconfig(texto_contador, text = "00:00") 
    titulo.config(text = "Contador", fg = VERDE)
    checks.config(text = "")
      
     
# ---------------------------- CONFIGURACION DE LA UI ------------------------------- #
# CONFIGURACION DE LA VENTANA.
window = Tk()
window.title("Pomodoro APP")
window.config(padx = 100, pady = 50, bg = AMARILLO)

# CONFIGURACION DE LAS CAPAS DE IMAGEN Y TEXTO CON CANVAS.
canvas = Canvas(width = 200, height = 224, bg = AMARILLO, highlightthickness = 0)
tomate = PhotoImage(file = "tomate.png")
canvas.create_image(100, 112, image = tomate)
texto_contador = canvas.create_text(103, 130, text = "00:00", fill = "white", font = FUENTE)
canvas.grid(column = 1, row = 1)

# CONFIGURACION DEDL LABEL Y LOS BOTONES.
titulo = Label(text = "Contador", font = FUENTE, bg = AMARILLO, fg = VERDE)
titulo.grid(column = 1, row = 0)

boton_start = Button(text = "Empezar", command = empieza_contador)
boton_start.grid(column = 0, row = 2)

boton_reset = Button(text = "Reset", command = reseteo_contador)
boton_reset.grid(column = 2, row = 2)

checks = Label(text ="", bg = AMARILLO)
checks.grid(column = 1, row = 3)

window.mainloop()