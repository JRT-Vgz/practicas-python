
from turtle import Screen

class Pantalla:
    
    screen = ""
    # Configura la pantalla en el init.
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width = 600, height = 600)
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