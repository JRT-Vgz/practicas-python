#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
--------------------------------------- 📙📙📙 FLASH CARD APP 📙📙📙 ----------------------------------------
--------------------------------------------------------------------------------------------------------------
Pasos.
1. Configuracion de la UI.
2. Funcion para crear una tarjeta y girarla a los 3 segs.
3. Funcionalidad para salvar el progreso de aciertos.
4. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

from tkinter import *
from pygame import mixer
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_IMG_FRONT = "images/card_front.png"
CARD_IMG_BACK = "images/card_back.png"
QUESTION_FONT = ("Ariel", 40, "italic")
ANSWER_FONT = ("Ariel", 60, "bold")
QUESTION_LANGUAGE = "French"
ANSWER_LANGUAGE = "English"
FULL_DATA_FILE = "data/french_words.csv"
TO_LEARN_FILE = "data/to_learn.csv"
FLIP_SOUND = "sounds/flip_sound.mp3"
SUCCESS_SOUND = "sounds/success_sound.mp3"
FAIL_SOUND = "sounds/fail_sound.mp3"

# ----------------------------- CREAR DICCIONARIO DE TARJETAS -------------------------------- #
try:
    data = pandas.read_csv(TO_LEARN_FILE)
except FileNotFoundError:
    data = pandas.read_csv(FULL_DATA_FILE)
to_learn = data.to_dict(orient="records")
last_card = {}
current_card = {}

# ---------------------------- CONFIGURACION DE SONIDOS ----------------------------
mixer.init()
def sound(sound, volume):
    mixer.music.load(sound)
    mixer.music.set_volume(volume)
    mixer.music.play()

# ----------------------------- CREAR UNA NUEVA TARJETA -------------------------------- #
def create_card():
    global current_card, last_card, flip_timer
    while last_card == current_card:
        if len(to_learn) == 1:
            last_card = {}
        current_card = random.choice(to_learn)
    last_card = current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_background, image=card_img_front)
    canvas.itemconfig(question_text, text = QUESTION_LANGUAGE, fill="black")
    canvas.itemconfig(answer_text, text = current_card[QUESTION_LANGUAGE], fill="black")

    flip_timer = window.after(3000,flip_card, current_card)
    

def flip_card(current_card):
    sound(FLIP_SOUND, 0.4)
    canvas.itemconfig(card_background, image=card_img_back)
    canvas.itemconfig(question_text, text = ANSWER_LANGUAGE, fill="white")
    canvas.itemconfig(answer_text, text = current_card[ANSWER_LANGUAGE], fill="white")
    
# ----------------------------- ACERTAR / FALLAR RESPUESTA -------------------------------- #
def right_answer():
    global to_learn, flip_timer
    sound(SUCCESS_SOUND, 0.3)
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(TO_LEARN_FILE, index=False)
    
    if len(to_learn) == 0:
        data = pandas.read_csv(FULL_DATA_FILE)
        data.to_csv(TO_LEARN_FILE, index=False)
        to_learn = data.to_dict(orient="records")
        messagebox.showinfo(title="Congratulations!", message="You learnt all the words!\nLesson has been restablished.")
    create_card()


def wrong_answer():
    sound(FAIL_SOUND, 0.3)
    create_card()
    
    
# ----------------------------- CONFIGURACION DE LA UI -------------------------------- #
# CONFIGURACION DE LA VENTANA.
window = Tk()
window.title("Flash Card")
window.config(bg = BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card, current_card)

# CONFIGURACION DE LAS CAPAS DE IMAGEN Y TEXTO.
canvas = Canvas(width=900, height=626, bg = BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file= CARD_IMG_FRONT)
card_img_back = PhotoImage(file= CARD_IMG_BACK)
card_background = canvas.create_image(450, 313, image = card_img_front)
canvas.grid(column = 0, row = 0, columnspan=2)
question_text = canvas.create_text(425, 200, text="Title", font = QUESTION_FONT)
answer_text = canvas.create_text(425, 313, text="Word", font = ANSWER_FONT)

# CONFIGURACION DE LOS WIDGETS.
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command= wrong_answer)
wrong_button.grid(column = 0, row = 1, pady = (0,50))
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command= right_answer)
right_button.grid(column = 1, row = 1, pady = (0,50))

create_card()

window.mainloop()

