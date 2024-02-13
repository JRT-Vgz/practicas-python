#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                     🐍🐍🐍 VIDEOJUEGO SNAKE :🐍🐍🐍
Pasos para completar el proyecto:
1. Crear el cuerpo de la serpiente.
2. Mover la serpiente.
3. Controlar la serpiente.
4. Detectar la colisión con la comida.
5. Crear el scoreboard.
6. Termina el juego: detectar la colisión con un muro.
7. Termina el juego: detectar la colisión con la cola.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""
import turtle as t
import time
from snake import Snake
from pantalla import Pantalla
from comida import Comida
from scoreboard import Scoreboard
from pygame import mixer

# SETEA LOS SONIDOS.
mixer.init()
def lanza_sonido(cancion, volumen):
    mixer.music.load(cancion)
    mixer.music.set_volume(volumen)
    mixer.music.play()

# Prepara turtle para escuchar eventos.
t.listen()

def main():  
    # CONFIGURACIÓN DE LA PANTALLA.
    t.clearscreen()
    screen = Pantalla()
    scoreboard = Scoreboard()
  
    # 1. CREAR EL CUERPO DE LA SERPIENTE Y LA COMIDA.
    serpiente = Snake()
    comida = Comida()
    screen.updatear_pantalla()
        
    # 2. MOVER LA SERPIENTE.
    juego_terminado = False
    time.sleep(0.5)
    while not juego_terminado:
        screen.updatear_pantalla()
        time.sleep(0.1)   
        serpiente.moverse_auto()
        
        # Movimientos por evento. Se puede jugar con flechas o WASD:       
        t.onkeypress(serpiente.arriba, "Up")
        t.onkeypress(serpiente.izquierda, "Left")
        t.onkeypress(serpiente.abajo, "Down")
        t.onkeypress(serpiente.derecha, "Right")
            
        t.onkeypress(serpiente.arriba, "w")
        t.onkeypress(serpiente.izquierda, "a")
        t.onkeypress(serpiente.abajo, "s")
        t.onkeypress(serpiente.derecha, "d")      

        # Detectar la colision con la comida.
        if serpiente.cabeza.distance(comida) <= 20:
            serpiente.extender()
            comida.cambia_de_sitio()
            # Chequeamos que el sitio nuevo no esté ocupado.
            check_comida_bloqueada = True
            while check_comida_bloqueada:
                pasa_check = True
                for segmento in serpiente.segmentos:
                    if comida.distance(segmento) <= 20:
                        comida.cambia_de_sitio()
                        pasa_check = False
                if pasa_check:               
                    check_comida_bloqueada = False
            # Actualiza el scoreboard.
            scoreboard.aumenta_scoreboard()
            # Lanza el sonido.
            lanza_sonido("recoger.mp3", 0.1)
            
        # Detectar la colisión con el muro o la cola.
        if serpiente.choca_con_muro() or serpiente.choca_con_cola():
            # Resetea scoreboard.
            scoreboard.resetea_scoreboard()
            screen.updatear_pantalla()
            # Lanza el sonido.
            lanza_sonido("game_over.mp3", 0.1)
            time.sleep(1)
            serpiente.resetea_serpiente()
    time.sleep(1)
    main()
   
main() 