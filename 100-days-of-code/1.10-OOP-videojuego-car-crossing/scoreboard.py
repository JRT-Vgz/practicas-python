
from turtle import Turtle

POSICION = (-200, 260)
ALINEACION = "center"
FUENTE = "Courier"
TAMANO_FUENTE = 16
TIPO_FUENTE = "bold"
FUENTE = (FUENTE, TAMANO_FUENTE, TIPO_FUENTE)


class Scoreboard(Turtle):
    
    # Configuracion del scoreboard.
    def __init__(self):
        super().__init__()
        self.nivel = 1
        self.penup()
        self.goto (POSICION)
        self.hideturtle()
        self.actualiza_scoreboard()
        
    # Funcion para actualizar el scoreboard.   
    def actualiza_scoreboard(self):
        self.clear()
        self.write(f"Nivel: {self.nivel}", align = ALINEACION, font = FUENTE)
        
    # Funcion para aumentar el nivel del scoreboard.
    def aumenta_nivel(self):
        self.nivel += 1
        self.actualiza_scoreboard()
        
    # Funcion para resetear el scoreboard.
    def resetea_scoreboard(self):
        self.nivel = 1
        self.actualiza_scoreboard()
    
    # Funcion para escribir el Game Over.     
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALINEACION, font = FUENTE)
        self.goto(0, -20)
        self.write("V para volver a empezar.", align = ALINEACION, font = FUENTE)
        
        
    
