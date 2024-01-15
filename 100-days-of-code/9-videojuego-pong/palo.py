
from turtle import Turtle

class Palo(Turtle):
    posicion = ()
    # Crea el palo en el init.
    def __init__(self, posicion):
        super().__init__()
        self.posicion = posicion
        self.crea_palo(self.posicion)
    
    # Funcion para crear el palo en la posición indicada.
    def crea_palo(self, posicion):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.speed("fastest")
        self.goto(posicion)
    
    # Funcion para mover arriba el palo.
    def arriba(self):
        # Comprueba que el palo no esté en el límite superior.
        if self.ycor() < 240:
            nueva_y = self.ycor() + 20
            self.goto(self.xcor(), nueva_y)
   
    # Funcion para mover abajo el palo.        
    def abajo(self):
        # Comprueba que el palo no esté en el límite inferior.
        if self.ycor() > -240:
            nueva_y = self.ycor() - 20
            self.goto(self.xcor(), nueva_y)
        
        