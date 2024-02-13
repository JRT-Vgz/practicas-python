#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                 🐢🐢🐢  DOCUMENTACION CON TURTLE  🐢🐢🐢
Practica de varios ejercicios con el módulo Turtle, leyendo la documentación para llegar al objetivo.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""
import turtle
from turtle import Turtle, Screen
import random as r

# 1. Dibuja un cuadrado de 100 utilizando la tortuga.
# python -c "from main import cuadrado; cuadrado()"
def cuadrado():
    timmy = Turtle()
    timmy.shape("turtle")
    
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

    screen = Screen()
    screen.exitonclick()
#cuadrado()
   
    
# 2. Dibuja una linea recta intermitente de 10 cada sección.
# python -c "from main import intermitente; intermitente()"
def intermitente(): 
    timmy = Turtle()
    timmy.shape("turtle")
    
    pinta = True
    for _ in range(10):
        if timmy.isdown() == True:
            timmy.penup()
        else:
            timmy.pendown()
        timmy.forward(10)

    screen = Screen()
    screen.exitonclick()
#intermitente()

    
# 3. Dibuja un triangulo, cuadradfo, pentagono, hexagono, heptagono, octagono, nonagono y decagono. Todos partiendo del mismo vertice.
# TIP: el angulo se consigue dividiendo 360 entre el numero de lados. EJ: Cuadrado = 360 / 4 = 90 grados cada giro.
# python -c "from main import formasGeo; formasGeo()"
def formasGeo():
    timmy = Turtle()
    timmy.shape("turtle") 
    
    lados = 3
    while lados < 11:
        angulo = 360/lados
        angulo_total = 0
        while angulo_total < 360:
            timmy.forward(100)
            timmy.right(angulo)
            angulo_total += angulo
        lados += 1
    
    screen = Screen()
    screen.exitonclick()
#formasGeo()


# Otra solucion:
# python -c "from main import formasGeo2; formasGeo2()"
def formasGeo2():
    timmy = Turtle()
    timmy.shape("turtle") 
    
    def dibuja_forma(num_lados):
        angulo = 360 / num_lados
        for _ in range(num_lados):
            timmy.forward(100)
            timmy.right(angulo)
    
    for forma in range(3, 11):
        dibuja_forma(forma)
        
    screen = Screen()
    screen.exitonclick()
#formasGeo2()
    
    
# 4. Random walk. Randomiza la dirección de la tortuga. Cambiale el color a uno aleatorio a cada paso.
# python -c "from main import random; random()"
def random():
    timmy = Turtle()
    timmy.shape("turtle")
    
    colores = ["light steel blue", "blue", "green", "green yellow", "chocolate", "light green", "aquamarine", "beige"]
    direcciones = ["Gira Izda", "Gira Derecha", "Misma"]
    
    def mueve_a_timmy(direccion):
        if direccion == "Gira Izda":
            timmy.left(90)
        elif direccion == "Gira Derecha":
            timmy.right(90)
        timmy.forward(50)
        
    for _ in range(50):
        color = r.choice(colores)
        direccion = r.choice(direcciones)
        mueve_a_timmy(direccion)
        timmy.color(color)
    
    screen = Screen()
    screen.exitonclick()
#random()

    
# Otra solucion:
# python -c "from main import random2; random2()"
def random2():
    timmy = Turtle()
    timmy.shape("turtle")
    
    colores = ["light steel blue", "blue", "green", "green yellow", "chocolate", "light green", "aquamarine", "beige"]
    direcciones = [0, 90, 180, 270]
    
    for _ in range(50):
        timmy.color(r.choice(colores))
        timmy.forward(50)
        timmy.setheading(r.choice(direcciones))
        
    screen = Screen()
    screen.exitonclick()
#random2()

   
# 5. Haz el mismo ejercicio de antes, pero creando colores totalmente random en cada paso.
# python -c "from main import random3; random3()"
def random3():
    timmy = Turtle()
    timmy.shape("turtle")
    turtle.colormode(255)
    
    def crea_color():
        rojo = r.randint(0, 255)
        verde = r.randint(0, 255)
        azul = r.randint(0, 255)
        return rojo, verde, azul
    
    direcciones = [0, 90, 180, 270]
    
    for _ in range(50):
        timmy.color(crea_color())
        timmy.forward(50)
        timmy.setheading(r.choice(direcciones))
        
    screen = Screen()
    screen.exitonclick()
#random3()

    
# 6. Dibuja un spirograph, dibuja un circulo de radio 100 en cada paso hasta completar la forma. Ponle un color random cada vez.
# python -c "from main import spiro; spiro()"
def spiro():
    timmy = Turtle()
    timmy.shape("turtle")
    turtle.colormode(255)
    timmy.speed("fastest")
    
    def crea_color():
        rojo = r.randint(0, 255)
        verde = r.randint(0, 255)
        azul = r.randint(0, 255)
        return rojo, verde, azul
    
    angulo = 0
    while angulo < 360:
        timmy.color(crea_color())
        timmy.circle(100)
        angulo += 5
        timmy.seth(angulo)
    
    screen = Screen()
    screen.exitonclick()
#spiro()

    
# Otra solucion:
# python -c "from main import spiro2; spiro2()"
def spiro2():
    timmy = Turtle()
    timmy.shape("turtle")
    turtle.colormode(255)
    timmy.speed("fastest")
    
    def crea_color():
        rojo = r.randint(0, 255)
        verde = r.randint(0, 255)
        azul = r.randint(0, 255)
        return rojo, verde, azul
    
    def crea_spiro(tamaño_hueco):
        for _ in range(int(360 / tamaño_hueco)):
            timmy.color(crea_color()) 
            timmy.circle(100)
            timmy.setheading(timmy.heading() + tamaño_hueco)

    crea_spiro(5)
    
    screen = Screen()
    screen.exitonclick()
#spiro2()