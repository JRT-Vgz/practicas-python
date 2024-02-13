
from turtle import Turtle
import random

# Heredamos la clase Turtle para nuestra comida.
class Comida(Turtle):
    
    def __init__(self):
        super().__init__()
        # Creamos la caracteristicas visuales de la comida.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")        
        self.cambia_de_sitio()
         
    def cambia_de_sitio(self):
        # Movemos la comida a un lugar aleatorio()
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
        
        
    