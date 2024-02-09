#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                    🔑🔑🔑 PASSWORD MANAGER APP 🔑🔑🔑
Pasos.
1. Configuracion de la UI.
2. Funcion para guardar la contraseña.
3. Crear pop-ups de confirmación y error.
3. Funcion para generar una contraseña aleatoria.
4. Retoques finales.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

from tkinter import *
from tkinter import messagebox
import os
import re
import random
import pyperclip

WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_TYPE = "Times New Roman"
FONT_SIZE = 10
FONT_MODIFIER = "bold"
FONT = (FONT_TYPE, FONT_SIZE, FONT_MODIFIER)
DEFAULT_EMAIL = "jrtvgz@gmail.com"
  
# ------------------------------- GUARDAR CONTRASEÑA ---------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    
    if is_any_field_empty(website, email, password):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    
    if not confirm_entry_data(website, email, password):
        return
    
    create_file_if_doesnt_exist()
    
    with open("password.txt") as file:
        data = file.readlines()
    
    if website_already_registered(website, data):
        messagebox.showerror(title="Error", message=f"The website {website} already exists in the database.")
        return
       
    text = f"{website} | {email} | {password}\n"
    data.append(text) 
       
    with open("password.txt", "w",) as file:
        file.writelines(data)

    website_input.delete(0, END)
    pass_input.delete(0, END)


def is_any_field_empty(website, email, password):
    return len(website) == 0 or len(email) == 0 or len(password) == 0


def confirm_entry_data(website, email, password):
    return messagebox.askokcancel(title="Confirm data entry", message=f"These are the details entered:\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")


def create_file_if_doesnt_exist():
    file = os.path.join(os.getcwd(), "password.txt")
    if not os.path.exists(file):
        with open("password.txt", "w",) as file:
            pass

def website_already_registered(website, data):
    pattern = fr"^{website} \|"    
    for line in data:
        if re.match(pattern, f"{line} | "):
            return True


# ---------------------------- GENERADOR DE CONTRASEÑAS ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
   
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)
    
    
# ----------------------------- CONFIGURACION DE LA UI -------------------------------- #
# CONFIGURACION DE LA VENTANA.
window = Tk()
window.title("Password Manager")
window.config(padx = 40, pady = 40, bg = WHITE)

# CONFIGURACION DE LAS CAPAS DE IMAGEN Y TEXTO CON CANVAS.
canvas = Canvas(width = 200, height = 200, bg = WHITE, highlightthickness = 0)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)

# CONFIGURACION DE LOS WIDGETS.
website_label = Label(text = "Website:", bg = WHITE)
website_label.grid(column = 0, row = 1)
data_label = Label(text = "Email/Username:", bg = WHITE)
data_label.grid(column = 0, row = 2)
pass_label = Label(text = "Password:", bg = WHITE)
pass_label.grid(column = 0, row = 3)

##### poner padding vertical pequeño para que los campos no esten tan apelotonados
website_input = Entry(width = 43)
website_input.grid(column = 1, row = 1, columnspan = 2, padx =(2,0))
website_input.focus()
email_input = Entry(width = 43)
email_input.grid(column = 1, row = 2, columnspan = 2, padx =(2,0))
email_input.insert(0, DEFAULT_EMAIL)
pass_input = Entry(width = 25)
pass_input.grid(column = 1, row = 3, padx = (0,0))


generate_pass_button = Button(text = "Generate Pass", command = generate_password)
generate_pass_button.grid(column = 2, row = 3, padx = (0,23))
add_button = Button(text = "Add", width = 36, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2)

window.mainloop()