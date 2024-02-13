
from turtle import Turtle
import csv

POSICION_SCOREBOARD = (0, 270)
ALINEACION = "center"
FUENTE = "Arial"
TAMANO_FUENTE = 16
TIPO_FUENTE = "normal"
FUENTE = (FUENTE, TAMANO_FUENTE, TIPO_FUENTE)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.record = self.carga_record()
        # Creamos la caracteristicas visuales del scoreboard
        self.penup()
        self.color("white")
        self.speed("fastest")        
        self.goto(POSICION_SCOREBOARD)
        self.hideturtle()
        self.actualiza_scoreboard()
        
    def actualiza_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}      |      Record = {self.record}", align = ALINEACION, font = FUENTE)
        
    def aumenta_scoreboard(self):
        self.score += 1
        self.actualiza_scoreboard()
        
    def resetea_scoreboard(self):
        if self.score > self.record:
            self.record = self.score
        self.score = 0
        self.actualiza_scoreboard()
        self.guarda_record()
        
    def guarda_record(self):
        with open("record.txt", "w") as file:
            file.write(str(self.record))
            
    def carga_record(self):
        with open("record.txt") as file:
            return int(file.read())