#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                     🏆🐢🏆 CARRERA DE TORTUGAS 🏆🐢🏆
Crea una carrera de tortugas aleatoria con turtle. 
Crea un pop-up inicial para apostar por la tortuga ganadora antes de empezar la carrera.
Setea la pantalla a 500x400.
Printea al final si hemos ganado o perdido y qué tortuga ha ganado la carrera. 
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

import turtle as t
from turtle import Turtle, Screen
import random
from pygame import mixer

ALINEACION = "center"
FUENTE = "Arial"
TAMANO_FUENTE = 16
TIPO_FUENTE = "normal"
FUENTE = (FUENTE, TAMANO_FUENTE, TIPO_FUENTE)

# Setea la pantalla y su tamaño.
screen = Screen()
screen.setup(width = 500, height = 400)
screen.title("                                                   CARRERA DE TORTUGAS")

# Setea la musica
mixer.init()
def cambia_cancion(cancion, volumen):
    mixer.music.load(cancion)
    mixer.music.set_volume(volumen)
    mixer.music.play()

# Crea el pop-up inicial. Aplica un filtro para que se de una respuesta correcta.
colores = {"roja": "red", "amarilla": "yellow", "morada": "purple", "verde": "green", "negra": "black", "naranja": "orange"}
check_apuesta = False
while not check_apuesta:
    apuesta = screen.textinput(title ="Hagan sus apuestas.", prompt = "¿Qué tortuga ganará la carrera? Introduce un color: \n    (Roja, amarilla, morada, verde, negra, naranja)")
    for color in colores:
        if apuesta.upper() == color.upper():
            check_apuesta = True

# Crea las tortugas y posicionalas.
tortugas = []
pos_y = -150
for color_ingles in colores.values():
    timmy = Turtle(shape = "turtle")
    timmy.color(color_ingles)
    timmy.penup()
    pos_y += 45
    timmy.goto( x = -230, y = pos_y)
    tortugas.append(timmy)

# Define la logica del movimiento random.
def movimiento_random(tortuga):
    if random.randint(1, 8) == 1:
        pasos = random.randint(1, 5)
        tortuga.forward(pasos)
        
# Crea el bucle de la carrera.
tortuga_ganadora = ""
termina_carrera = False
cambia_cancion("song.mp3", 0.3)
while not termina_carrera:
    for tortuga in tortugas:
        movimiento_random(tortuga)
        if tortuga.xcor() >= 250:
            termina_carrera = True
            tortuga_ganadora = tortuga.pencolor()

# Traduce el color de la tortuga ganadora.
for color, color_ingles in colores.items():
    if tortuga_ganadora == color_ingles:
        tortuga_ganadora = color
        break
                
# Resuelve la apuesta.
texto_final = ""
if apuesta.upper() == tortuga_ganadora.upper():
    texto_final += "¡Has ganado! "
else:
    texto_final += "¡Has perdido! "
texto_final += "La tortuga ganadora es la " + tortuga_ganadora + "."
print(texto_final)

# Crea un texto en la pantalla con el resultado.
resultado = Turtle()
resultado.penup()      
resultado.hideturtle()
resultado.speed("fastest")
resultado.goto(0, 160)
resultado.write(texto_final, align = ALINEACION, font = FUENTE)

cambia_cancion("finish.mp3", 0.1)
            
# Configura la pantalla para salir del programa con click.
screen.exitonclick()