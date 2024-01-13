
from turtle import Screen

ANCHO_PANTALLA = 590
ALTO_PANTALLA = 590

class Pantalla:   
    # Configura la pantalla en el init.
    def __init__(self):
        self.screen = Screen()
        self.ancho = ANCHO_PANTALLA
        self.alto = ALTO_PANTALLA
        self.screen.setup(width = self.ancho, height = self.alto)
        self.screen.bgcolor("black")
        self.screen.title("                                                                                    SNAKE")
        # Método para que no refresque la pantalla hasta que llamemos un update.
        self.screen.tracer(0)
    
    # Funcion para cerrar la pantalla con click.  
    def salir_con_click(self):
        self.screen.exitonclick()
    
    # Funcion para updatear el estado de la pantalla y que se vean los cambios.    
    def updatear_pantalla(self):
        self.screen.update()