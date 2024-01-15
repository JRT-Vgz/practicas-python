
from turtle import Turtle

ALINEACION = "center"
FUENTE = "Courier"
TAMANO_FUENTE = 40
TIPO_FUENTE = "bold"
FUENTE = (FUENTE, TAMANO_FUENTE, TIPO_FUENTE) 

class Scoreboard(Turtle):
    # Configuracion del scoreboard.
    def __init__(self):
        super().__init__()
        self.score_izda = 0
        self.score_dcha = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto (0, 230)
        self.hideturtle()
        self.actualiza_scoreboard()
    
    # Funcion para actualizar el scoreboard.   
    def actualiza_scoreboard(self):
        self.clear()
        self.write(f"{self.score_izda}      {self.score_dcha}", align = ALINEACION, font = FUENTE)
        
    # Funcion para cuando marca punto el Palo Izquierdo.
    def marca_izdo(self):
        self.score_izda += 1
        self.actualiza_scoreboard()
        
    # Funcion para cuando marca punto el Palo Derecho.
    def marca_dcho(self):
        self.score_dcha += 1
        self.actualiza_scoreboard()