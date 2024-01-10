
from turtle import Turtle
import time

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
IZQUIERDA = 180
ABAJO = 270
DERECHA = 0

class Snake:
    
    # Crea la serpiente en el init.
    def __init__(self):
        self.segmentos = []
        self.crea_serpiente()
        self.cabeza = self.segmentos[0]
        self.posicion_cabeza = ()
    
    # Función para crear la serpiente:
    def crea_serpiente(self):
        for posicion in POSICIONES_INICIALES:
            snake = Turtle(shape = "square")
            snake.color("white")
            snake.penup()
            snake.goto(posicion)
            self.segmentos.append(snake)
            
    # Función para el movimiento automático de la serpiente.
    def moverse_auto(self):
        for seg_num in range(len(self.segmentos) -1, 0, -1):
            nueva_x = self.segmentos[seg_num - 1].xcor()
            nueva_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(nueva_x, nueva_y)
        self.cabeza.forward(DISTANCIA_MOVIMIENTO)
        
    # Funciones para los movimientos de la serpiente:            
    def arriba(self):
        if self.cabeza.heading() != ABAJO and self.debug_posicion():
            self.cabeza.setheading(ARRIBA)
            self.posicion_cabeza = (self.cabeza.xcor(), self.cabeza.ycor())
    
    def izquierda(self):
        if self.cabeza.heading() != DERECHA and self.debug_posicion():
            self.cabeza.setheading(IZQUIERDA)
            self.posicion_cabeza = (self.cabeza.xcor(), self.cabeza.ycor())
        
    def abajo(self):
        if self.cabeza.heading() != ARRIBA and self.debug_posicion():
            self.cabeza.setheading(ABAJO)
            self.posicion_cabeza = (self.cabeza.xcor(), self.cabeza.ycor())
        
    def derecha(self):
        if self.cabeza.heading() != IZQUIERDA and self.debug_posicion():
            self.cabeza.setheading(DERECHA)
            self.posicion_cabeza = (self.cabeza.xcor(), self.cabeza.ycor())
    
    # Funcion para asegurarse que la cabeza no gira rapidamente 180 grados sin moverse de la posicion.
    def debug_posicion(self):
        posicion_actual = (self.cabeza.xcor(), self.cabeza.ycor())
        if posicion_actual == self.posicion_cabeza:
            return False
        return True
               
    # Funcion para comer.
    def crea_segmento(self):
        snake = Turtle(shape = "square")
        snake.color("white")
        snake.penup()
        posicion = (self.segmentos[len(self.segmentos) -1].xcor(), self.segmentos[len(self.segmentos) -1].ycor())
        snake.goto(posicion)
        self.segmentos.append(snake)
        
            