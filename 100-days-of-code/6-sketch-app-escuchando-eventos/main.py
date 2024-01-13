#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                     🖊🖋🖊 SKETCH APP CON TURTLE 🖊🖋🖊
Crea un programa usando Turtle que sea capaz de escuchar eventos y tenga la siguiente configuracion.
W (Forward), S(Backward), A(Girar contra-reloj), D(Girar reloj) C(Limpiar el dibujo y poner el cursor en el centro.)
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

import turtle as t
from turtle import Turtle, Screen

# Creamos el cursor.
timmy = Turtle()

# Definimos funciones de movimiento y eventos.
def move_forward():
    timmy.forward(10)
    
def move_backwards():
    timmy.backward(10)
    
def rotate_left():
    timmy.left(5)
    
def rotate_right():
    timmy.right(5)
    
def clear():
    timmy.reset()
    
# Preparamos el programa para escuchar eventos y creamos la logica de aplicación de las funciones.
t.listen()
t.onkeypress(move_forward, "w")
t.onkeypress(move_backwards, "s")
t.onkeypress(rotate_left, "a")
t.onkeypress(rotate_right, "d")
t.onkeypress(clear, "c")

# Creamos la pantalla.
screen = Screen()
screen.exitonclick()