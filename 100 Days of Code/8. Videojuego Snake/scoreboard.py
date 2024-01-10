
from turtle import Turtle

POSICION_SCOREBOARD = (0, 270)
ALINEACION = "center"
fuente = "Arial"
tamaño_fuente = 16
tipo_fuente = "normal"
FUENTE = (fuente, tamaño_fuente, tipo_fuente)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Creamos la caracteristicas visuales del scoreboard
        self.penup()
        self.color("white")
        self.speed("fastest")        
        self.goto(POSICION_SCOREBOARD)
        self.hideturtle()
        self.actualiza_scoreboard()
        
    def actualiza_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align = ALINEACION, font = FUENTE)
        
    def aumenta_scoreboard(self):
        self.score += 1
        self.actualiza_scoreboard()
        
    def resetea_scoreboard(self):
        self.score = 0
        self.actualiza_scoreboard()