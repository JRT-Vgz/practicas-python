#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                             @@@ DECORADORES @@@
Crea un decorador que valide si las entradas de la siguiente función son enteros, si no lo son retornar un TypeError.

def add(a, b):
    return a + b
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

# Decorador
def check_if_integers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Los parámetros deben ser números integros.")
        for key, kwarg in kwargs.items():
            if not isinstance(kwarg, int):
                raise TypeError("Los parámetros deben ser números integros.")
        return func(*args, **kwargs)
    return wrapper


@check_if_integers
def add(a,b):
    return a + b

print(add(1,5))