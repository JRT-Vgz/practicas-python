#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                          ❗⚽❗ VIDEOJUEGO PONG ❗⚽❗
Pasos.
1. Crear la pantalla.
2. Crear y mover el primer palo.
3. Crear y mover el segundo palo.
4. Crear la bola y hacer su movimiento.
5. Detectar colisión de la bola con paredes y su rebote.
6. Detectar colisión con palos y su rebote.
7. Scoreboard y sumar cuando se mete un punto.
8. El juego termina cuando se llega a 10.
9. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

from turtle import Screen
from palo import Palo
from bola import Bola
from scoreboard import Scoreboard
import time
from pygame import mixer

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
POSICION_PALO_IZDO = (-360, 0)
POSICION_PALO_DCHO = (360, 0)

# Configuración de la pantalla.
screen = Screen()
screen.setup(width = ANCHO_PANTALLA, height = ALTO_PANTALLA)
screen.bgcolor("black")
screen.title("                                                                                                                      PONG")
screen.tracer(0)
screen.listen()

# SETEA LOS SONIDOS.
mixer.init()
def lanza_sonido(sonido, volumen):
    mixer.music.load(sonido)
    mixer.music.set_volume(volumen)
    mixer.music.play()
    
# Crear los palos.
palo_izdo = Palo(posicion = POSICION_PALO_IZDO)
palo_dcho = Palo(posicion = POSICION_PALO_DCHO)

# Controlar el movimiento de los palos.

screen.onkey(palo_izdo.arriba, "w")
screen.onkey(palo_izdo.abajo, "s")
screen.onkey(palo_izdo.arriba, "W")
screen.onkey(palo_izdo.abajo, "S")
screen.onkey(palo_dcho.arriba, "Up")
screen.onkey(palo_dcho.abajo, "Down")


# Crear la bola.
bola = Bola()

# Crea el scoreboard.
scoreboard = Scoreboard()

screen.update()

# Controla el juego.
time.sleep(1)
jugando = True
while jugando:
    screen.update()
    time.sleep(bola.velocidad)
    bola.reducir_contador_desbugear_golpes_palo()
    bola.mover_bola()
       
    # Colision de la bola con los bordes.
    if bola.ycor() >= ((ALTO_PANTALLA / 2) - 10) or bola.ycor() <= -((ALTO_PANTALLA / 2) - 10):
        bola.choca_pared()
    
    # Colision de la bola con palo.
    if bola.xcor() >= (POSICION_PALO_DCHO[0] - 10) or bola.xcor() <= POSICION_PALO_IZDO[0] + 10:
        if bola.distance(palo_dcho) <= 50 or bola.distance(palo_izdo) <= 50:
            bola.choca_palo()
            # Lanza el sonido.
            lanza_sonido("rebotar.mp3", 0.1)
               
    # El izquierdo marca un punto.
    if bola.xcor() >= (ANCHO_PANTALLA / 2):
        scoreboard.marca_izdo()
        screen.update()
        if scoreboard.score_izda < 10:
            lanza_sonido("score.mp3", 0.1)
            palo_dcho.goto(POSICION_PALO_DCHO)
            palo_izdo.goto(POSICION_PALO_IZDO)
            bola.marca_punto()
        else:
            lanza_sonido("game_over.mp3", 0.3)
            jugando = False
               
    # El derecho marca un punto.
    elif bola.xcor() <= -(ANCHO_PANTALLA / 2):
        scoreboard.marca_dcho()
        screen.update()
        if scoreboard.score_dcha < 10:
            lanza_sonido("score.mp3", 0.1)
            palo_dcho.goto(POSICION_PALO_DCHO)
            palo_izdo.goto(POSICION_PALO_IZDO)
            bola.marca_punto()
        else:
            lanza_sonido("game_over.mp3", 0.3)
            jugando = False
        
# Salir de la pantalla con click.
screen.exitonclick()