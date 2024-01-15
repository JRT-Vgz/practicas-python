
from turtle import Turtle
import random
from pygame import mixer

COLORES = ["red", "orange", "yellow", "green", "blue", "purple"]
PITIDOS = ["sonido_pito1.mp3", "sonido_pito2.mp3", "sonido_pito3.mp3", "sonido_pito4.mp3",]
VELOCIDAD_INICIAL = 5
INCREMENTO_VELOCIDAD = 3
X_INICIAL = 320
X_FINAL = -320
FRECUENCIA_COCHES = 6

# SETEA LOS SONIDOS.
mixer.init()
    
class Coche_Manager():
    # Crea una lista para gestionar los coches que existen.
    def __init__(self):
        self.lista_coches = []
        self.check_timing = 0
        self.velocidad = VELOCIDAD_INICIAL
    
    # Funcion para gestionar cuando deben crearse los coches.
    def gestiona_creacion_coches(self):
        if self.check_timing == FRECUENCIA_COCHES:
            self.crea_coche()
            self.check_timing = 0
        else:
            self.check_timing += 1
            
    # Funcion para crear un coche y añadirlo a la lista de coches.
    def crea_coche(self):
        coche = Turtle("square")
        coche.color(random.choice(COLORES))
        coche.shapesize(stretch_wid = 1, stretch_len = 2)
        coche.penup()
        coche.goto(self.randomizar_posicion_inicial())
        self.lista_coches.append(coche)
        
    # Funcion para randomizar la posicion del coche cuando se crea.    
    def randomizar_posicion_inicial(self):
        y_inicial = random.randint(-240, 240)
        return(X_INICIAL, y_inicial)
    
    # Funcion para mover y los coches y gestionar su destruccion.
    def mueve_coches(self):
        for coche in self.lista_coches:
            nueva_x = coche.xcor() - self.velocidad
            if nueva_x < X_FINAL:
                self.destruye_coche(coche)
            else:
                coche.goto(nueva_x, coche.ycor())
    
    # Funcion para destruir un coche.
    def destruye_coche(self, coche):
        coche.hideturtle()
        self.lista_coches.remove(coche)
        
    # Funcion para aumentar la velocidad de los coches.        
    def aumenta_velocidad(self):
        self.velocidad += INCREMENTO_VELOCIDAD

    # Funcion para lanzar un sonido.   
    def lanza_sonido(self, sonido, volumen):
        mixer.music.load(sonido)
        mixer.music.set_volume(volumen)
        mixer.music.play()
    
    # Funcion para lanzar un pitido si el jugador pasa cerca de un coche.    
    def pita_coche(self):
        sonido = random.choice(PITIDOS)
        self.lanza_sonido(sonido,0.3)   

        
        
