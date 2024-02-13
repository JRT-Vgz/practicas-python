
from turtle import Turtle

POSICION_INICIAL = (0, -280)
DISTANCIA_MOVIMIENTO = 10
LINEA_LLEGADA_Y = 300

class Jugador(Turtle):
    
    # Crea la tortuga.
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(POSICION_INICIAL)
    
    # Funcion para moverse arriba.    
    def arriba(self):
        self.forward(DISTANCIA_MOVIMIENTO)
        
    # Funcion para resetear la posicion del jugador.
    def resetea_posicion(self):
        self.goto(POSICION_INICIAL)
        
    # Funcion para detectar cuando el jugador ha cruzado la carretera.
    def ha_cruzado(self):
        return self.ycor() == LINEA_LLEGADA_Y
