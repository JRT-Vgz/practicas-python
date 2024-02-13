
from turtle import Turtle

FUENTE = "Courier"
TAMANO_FUENTE = 12
TIPO_FUENTE = "bold"
FUENTE = (FUENTE, TAMANO_FUENTE, TIPO_FUENTE)

class Lapiz(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
    
    # Escribe el nombre del estado en las coordenadas.    
    def escribe(self,estado,cor_x,cor_y):
        self.goto(cor_x,cor_y)
        self.write(estado, font = FUENTE)