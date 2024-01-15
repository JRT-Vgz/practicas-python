#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                      🤦‍♂️🤦‍♂️🤦‍♂️  HIRST PAINTING  🤦‍♂️🤦‍♂️🤦‍♂️
Utilizamos el paquete colorgram para sacar la paleta de colores de una imagen y el módulo turtle para crear un patrón
de puntos igual a los creados por Hirst.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

import colorgram

# 1. Utiliza la documentación de colorgram para sacar una lista de tuples con la paleta de colores de la imagen.
def extraer_colores():
    colores = colorgram.extract("imagen.jpg",30)

    lista_colores = []
    for color in colores:
        rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
        lista_colores.append(rgb)
    return lista_colores

lista_colores = extraer_colores()

# 2. Crea un dibujo de 10x10 puntos con turtle usando la paleta que hemos extraido. Cada punto debe tener un tamaño de 20 y espaciados 50 entre ellos.
import turtle as turtle
from turtle import Turtle, Screen
import random

def crea_cuadro():

    def crea_linea_puntos():
        pos_x = round(timmy.xcor())
        pos_y = round(timmy.ycor())
        # Cada una de las columnas de puntos.
        for _ in range(10):
            # Cada una de las lineas de puntos.
            for _ in range(10):
                color = random.choice(lista_colores)
                timmy.dot(20, color)
                timmy.fd(50)
            # Cambia la posicion del puntero a la siguiente linea.
            timmy.goto(pos_x ,pos_y + 50)
            pos_y += 50
    
    # Crea la tortuga y muevela a la posicion inicial.   
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.speed("fastest")
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(-225,-225)
    turtle.colormode(255)

    crea_linea_puntos()

    screen = Screen()
    screen.exitonclick()

crea_cuadro()
