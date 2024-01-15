#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                                 ☕☕☕ MÁQUINA EXPENDEDORA DE CAFÉ ☕☕☕
Gestiona el pedido, la introducción de dinero, dale el cambio al cliente y quita los recursos de la máquina. 
Lleva la contabilidad del dinero e imprime reportes con los ingredientes y el dinero que hay en la máquina. 
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# ------------------------------------------------------------------------------------------------------------
# -------------------------------------------- FUNCIONALIDADES -----------------------------------------------
# ------------------------------------------------------------------------------------------------------------

def printea_reporte_recursos():
    """Printea un reporte con los recursos restantes en la máquina y el dinero que hay dentro."""
    print(f"Water: {resources['water']}ml.")
    print(f"Milk: {resources['milk']}ml.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${profit}.")


def hay_suficientes_recursos(ingredientes_pedido):
    """True si la maquina tiene suficientes recursos, False si le falta alguno."""
    for ingrediente in ingredientes_pedido:
        if ingredientes_pedido[ingrediente] > resources[ingrediente]:
            print(f"Lo siento, no hay suficiente {ingrediente}.")
            return False
    return True

def introducir_dinero():
    """Devuelve un float con la cantidad de dinero introducido."""
    dic_monedas = {"cuartos": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    total = 0
    for moneda in dic_monedas:
        total += int(filtro_monedas(input(f"¿Cuantos {moneda}?: "))) * dic_monedas[moneda]
    return total

def procesar_dinero(dinero_total, coste):
    """True si hay suficiente dinero para el pedido, False si no hay suficiente. Devuelve el cambio."""
    global profit
    if dinero_total > coste:
        profit += coste
        cambio = round(dinero_total - coste,2)
        print(f"Aqui tienes ${cambio} de cambio.")
        return True
    elif dinero_total == coste:
        profit += coste
        return True
    print(" Lo siento, no hay suficiente dinero. Dinero devuelto.")
    return False


def hacer_cafe(nombre_bebida, ingredientes_pedido):
    """Haz café y reduce los ingredientes de la máquina."""
    for ingrediente in ingredientes_pedido:
        resources[ingrediente] -= ingredientes_pedido[ingrediente]
    print(f"Aquí tienes tu {nombre_bebida} ☕.")


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ FILTROS ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
    

def filtro_eleccion(eleccion):
    """Filtra el input para que no de error si no cumple las condiciones requeridas por la máquina de café."""
    for element in MENU:
        if eleccion.upper() == element.upper() or eleccion.upper() == "OFF" or eleccion.upper() == "REPORT":
            return eleccion
    return ""


def filtro_monedas(cantidad):
    """Filtra el input de dinero introducido para que no de error si no se introduce un numero."""
    if cantidad.isnumeric():
        return cantidad
    elif is_float(cantidad):
        return round(float(cantidad))
    return 0


def is_float(string):
    """ Comprueba si el string recibido como input puede ser convertido en float."""
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- PRINCIPAL --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
    

def main():
    # Crea un bucle para repetir el programa en el siguiente cliente.
    check_apagado = False
    while not check_apagado:
        eleccion = filtro_eleccion(input("What would you like? (espresso/latte/cappuccino): "))
        # Palabra secreta para apagar la máquina.
        if eleccion.upper() == "OFF":
            check_apagado = True
        # Palabra secreta para printear el reporte con las estadísticas.
        elif eleccion.upper() == "REPORT":
            printea_reporte_recursos()
        else:
            # Chequea que la eleccion ha pasado el filtro:
            if eleccion != "":
                bebida = MENU[eleccion]
                # Procesa si la máquina tiene suficientes ingredientes.
                if hay_suficientes_recursos(bebida["ingredients"]):
                    # Procesa la introducción de dinero en la máquina.
                    dinero_total = round(introducir_dinero(),2)
                    # Comprueba si se ha introducido suficiente dinero:
                    if procesar_dinero(dinero_total, float(bebida["cost"])):
                        # Haz cafe.
                        hacer_cafe(eleccion, bebida["ingredients"])


main()


