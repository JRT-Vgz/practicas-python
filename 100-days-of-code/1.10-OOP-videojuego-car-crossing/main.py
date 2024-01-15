#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                🚕🐢🚛 VIDEOJUEGO CAR CROSSING 🚑🐢🚙
Pasos.
1. Crear la pantalla.
2. Crear y mover la tortuga.
3. Crear los coches y randomizarlos.
4. Crear el scoreboard de niveles.
5. Que la tortuga pase de nivel al cruzar la meta.
6. Game Over: Cuando un coche choca con la tortuga.
7. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

import time
from turtle import Screen
from jugador import Jugador
from coche_manager import Coche_Manager
from scoreboard import Scoreboard

# Configuracion de la pantalla.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
    
# Creando los objetos.
jugador = Jugador()
coches = Coche_Manager()
scoreboard = Scoreboard()

# Teclas de movimiento()
screen.listen()
screen.onkey(jugador.arriba, "w")
screen.onkey(jugador.arriba, "Up")

# Control del juego.
jugando = True
while jugando:
    time.sleep(0.1)
    screen.update()
    
    # Crea y mueve los coches.
    coches.gestiona_creacion_coches()
    coches.mueve_coches()
    
    # Cuando el jugador cruza, sube de nivel y actualiza el scoreboard.
    if jugador.ha_cruzado():
        jugador.resetea_posicion()
        scoreboard.aumenta_nivel()
        coches.aumenta_velocidad()
        coches.lanza_sonido("sonido_cruza.mp3",0.3)
        
    # Si el jugador pasa cerca de un coche, pita. Si es atropellado, termina el juego.
    for coche in coches.lista_coches:
        if jugador.distance(coche) < 20:
            scoreboard.game_over()
            jugando = False
            coches.lanza_sonido("sonido_atropella.mp3",0.3)
        elif jugador.distance(coche) < 40:
            coches.pita_coche()
    
screen.exitonclick()
            

