
from turtle import Turtle
import pantalla
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
            self.crea_segmento(posicion)
    
    # Funcion para crear un segmento.   
    def crea_segmento(self, posicion):
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
               
    # Funcion para extender la serpiente.
    def extender(self):
        posicion = (self.segmentos[-1].xcor(), self.segmentos[-1].ycor())
        self.crea_segmento(posicion)
    
    # Funcion para detectar si hemos chocado con un muro.    
    def choca_con_muro(self):
        if self.cabeza.xcor() > (pantalla.ANCHO_PANTALLA / 2) or self.cabeza.xcor() < -(pantalla.ANCHO_PANTALLA / 2) or self.cabeza.ycor() > (pantalla.ALTO_PANTALLA / 2) or self.cabeza.ycor() < -(pantalla.ALTO_PANTALLA / 2):
           return True 
    
    # Funcion para detectar si hemos chocado conb algún segmento de la cola.  
    def choca_con_cola(self):
        for segmento in self.segmentos[1:]:
            if self.cabeza.distance(segmento) < 10:
                return True
    
    # Funcion para resetear la serpiente.        
    def resetea_serpiente(self):
        for segmento in self.segmentos:
            segmento.hideturtle()
        self.__init__()