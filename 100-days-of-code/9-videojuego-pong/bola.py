
from turtle import Turtle
import random
import time

DIRECCION_BOLA_X = 5
VELOCIDAD_INICIAL = 0.03

class Bola(Turtle):
    
    # Crea la bola en el init.
    def __init__(self):
        super().__init__()
        self.crea_bola()
    
    # Funcion para crear la bola.    
    def crea_bola(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direccion_x = self.randomizar_direccion_x()
        self.direccion_y = self.randomizar_direccion_y()
        self.velocidad = VELOCIDAD_INICIAL
        # Variable para desbugear que se de muchos golpes a la vez con el mismo palo.
        self.cuenta_atras = 30
    
    # Funcion para randomizar la direccion horizontal de la bola al principio de la partida.
    def randomizar_direccion_x(self):
        if random.randint(0,1) == 0:
            return DIRECCION_BOLA_X
        return -(DIRECCION_BOLA_X)
    
    # Funcion para randomizar la direccion vertical de la bola.
    def randomizar_direccion_y(self):
        direccion = random.choice([3,4,5,-3,-4,-5])
        return direccion
                         
    # Funcion para mover la bola automaticamente.   
    def mover_bola(self):
        nuevo_x = self.xcor() + self.direccion_x
        nuevo_y = self.ycor() + self.direccion_y
        self.goto(nuevo_x, nuevo_y)
    
    # Funcion para cambiar la direccion cuando se choca con la pared.
    def choca_pared(self):
        self.direccion_y *= -1
    
    # Funcion para cambiar la dirección cuando se choca con el palo.
    def choca_palo(self):
        # Usamos la variable para desbugear que se de muchos golpes con el mismo palo.
        if self.cuenta_atras == 0:
            self.direccion_x *= -1
            #self.direccion_y = self.randomizar_direccion_y()
            self.velocidad *= 0.9
            self.cuenta_atras = 30
        
    # Funcion para resetear la bola al marcar un punto y cambiar de lado.
    def marca_punto(self):
        self.goto(0, 0)
        self.velocidad = VELOCIDAD_INICIAL
        time.sleep(1)
        self.direccion_x *= -1 
        self.direccion_y = self.randomizar_direccion_y()
        
    # Funcion para desbugear que se de muchos golpes con el mismo palo a la vez.
    def reducir_contador_desbugear_golpes_palo(self):
        if self.cuenta_atras > 0:
            self.cuenta_atras -= 1
    