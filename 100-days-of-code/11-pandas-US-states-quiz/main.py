#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                        🎏🎏🎏 ESTADOS USA 🎏🎏🎏
Pasos.
1. Crear una Screen y ponerle fondo.
2. Leer el csv. Crear el DataFrame y una lista con los estados.
3. Crear el input y filtrarlo correctamente.
4. Marcar la coordenada en los aciertos.
5. Seguir la cuenta de los aciertos.
6. Poner una palabra clave de salida que crea un csv con los estados que no se han acertado.
7. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

import turtle
from lapiz import Lapiz
from pygame import mixer
import pandas
import time

IMAGEN = "blank_states_img.gif"
CSV_PATH = "50_states.csv"
SOUND_SUCCESS = "ding.mp3"
SOUND_WRONG = "wrong.mp3"

# Configuración de la pantalla.
screen = turtle.Screen()
screen.title("Estados USA")
screen.setup(width=750, height=510)
screen.addshape(IMAGEN)
turtle.shape(IMAGEN)
screen.tracer(0)

# SETEA LOS SONIDOS.
mixer.init()
def lanza_sonido(sonido, volumen):
        mixer.music.load(sonido)
        mixer.music.set_volume(volumen)
        mixer.music.play()  
        
# Crea el DataFrame y la lista de los estados.
df = pandas.read_csv(CSV_PATH)
lista_estados = df.state.to_list()

# Crea el objeto que marca los aciertos.
lapiz = Lapiz()

# Crea el bucle de control del juego.
lista_aciertos = []
while len(lista_aciertos) < 50:
    # Recibe el input y filtralo: Solo acepta el input si forma parte del diccionario de estados y no se ha dicho antes.
    check_input = False
    while not check_input:
        if len(lista_aciertos) == 0:
            respuesta = screen.textinput(title = "  ADIVINA UN ESTADO", prompt = "Nombra un estado de USA: ").title()
        else:
            respuesta = screen.textinput(title = f"       ACIERTOS {len(lista_aciertos)}/50", prompt = "Nombra otro estado de USA: ").title()
        
        if respuesta == "Exit":
            break
                    
        elif respuesta in lista_estados and respuesta not in lista_aciertos:
            check_input = True
            break
        lanza_sonido(SOUND_WRONG, 0.1)
            
    
    # Si el input es "Exit", termina el juego y crea un csv con los estados que faltan.
    if respuesta == "Exit":
        lista_faltas = [estado for estado in lista_estados if estado not in lista_aciertos]
        nuevo_df = pandas.DataFrame(lista_faltas)
        nuevo_df.to_csv("estados_para_aprender.csv")
        break
    else:        
        # Escribe el acierto y añadelo a la lista. Actualiza el scoreboard.
        datos_estado = df[df.state == respuesta]
        lapiz.escribe(respuesta, int(datos_estado.x), int(datos_estado.y))
        lista_aciertos.append(respuesta)
        lanza_sonido(SOUND_SUCCESS, 0.2)
        screen.update()
        time.sleep(1)

screen.exitonclick()