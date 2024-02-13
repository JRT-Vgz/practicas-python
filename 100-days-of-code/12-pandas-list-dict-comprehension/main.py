#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                📄📄📄 LIST / DICTIONARY COMPREHENSION 📄📄📄
Pasos.
1. Crear un diccionario en este formato utilizando el CSV: {"A": "Alfa", "B": "Bravo"} usando iterrows.
2. Printear una lista de los code words utilizando una palabra recibida como input.
UTILIZA LIST Y DICTIONARY COMPREHENSION.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""
import pandas

# Crea el dataframe leyendo el CSV.
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creea el diccionario utilizando la secuencia de rows del dataframe.
code_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# Crea el input y decodifica la palabra en una lista.
while True:
    # Forma mas larga.
    palabra = input("Escribe una palabra: ").upper()
    try:
        code_list = [code_dict[letra] for letra in palabra]
    except KeyError:
        print("Error: Escribe solo letras del alfabeto.\n")
    else:
        print(code_list)
        break

# Forma mas corta.
"""
print([code_dict[letra] for letra in input("Escribe una palabra: ").upper()])
"""






