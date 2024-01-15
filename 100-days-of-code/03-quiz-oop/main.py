#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                            ❓❓❓  OOP QUIZ  ❓❓❓
Gestiona un minijuego de Quiz creando un objeto Question y un objeto manager QuizBrain.
Cambia las preguntas del minijuego simplemente cambiando la base de datos.
Gestionalo en scripts diferentes, emulando un trabajo que podría ser hecho por diferentes personas.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# Crea la batería de preguntas (lista de objetos) usando la base de datos y la clase Question, que contiene la pregunta y la respuesta para cada una.
question_bank = []
for question in question_data:
    pregunta = Question(question["text"], question["answer"])
    question_bank.append(pregunta)

# Crea el quiz usando la clase manager BrainQuiz y gestiona el juego utilizando los métodos de la clase.    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# Termina el quiz.    
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")