#!/usr/bin/env python

"""
--------------------------------------------------------------------------------------------------------------
-------------------------------------------------- PRACTICA --------------------------------------------------
                               ☕☕☕ MÁQUINA EXPENDEDORA DE CAFÉ: OOP ☕☕☕
Misma práctica de la máquina de café, pero utilizando objetos en vez de programación procedural.
Utilizamos los objetos ya definidos para lograr la misma funcionalidad.
Clases: CoffeeMaker, Menu, MenuItem, MoneyMachine.
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------
"""

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------ CLASS: COFFEE MAKER ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")


# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- CLASS: MENU -------------------------------------------------
# ------------------------------------------------------------------------------------------------------------


class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
            # Quitamos la última letra del string, que sertá /.
        options = options[:len(options) - 1]
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------- CLASS: MONEY MACHINE ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------


class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def is_float(self, string):
        """ Comprueba si el string recibido como input puede ser convertido en float."""
        if string.replace(".", "").isnumeric():
            return True
        else:
            return False
    
    def filtro_monedas(self, cantidad):
        """Filtra el input de dinero introducido para que no de error si no se introduce un numero."""
        if cantidad.isnumeric():
            return cantidad
        elif self.is_float(cantidad):
            return round(float(cantidad))
        return 0
       
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(self.filtro_monedas(input(f"How many {coin}?: "))) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        


# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ FILTROS ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
    

def filtro_eleccion(eleccion, menu):
    """Filtra el input para que no de error si no cumple las condiciones requeridas por la máquina de café."""
    for element in menu:
        if eleccion.upper() == element.name.upper() or eleccion.upper() == "OFF" or eleccion.upper() == "REPORT":
            return eleccion
    return ""


# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- PRACTICA ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
        
def main():
    # Crea los objetos que vamos a utilizar.
    maquina_cafe = CoffeeMaker()
    menu = Menu()
    maquina_dinero = MoneyMachine()
    # Crea un bucle para repetir el programa en el siguiente cliente.
    check_apagado = False
    while not check_apagado:
        eleccion = filtro_eleccion(input(f"What would you like? ({menu.get_items()}): "),menu.menu)
        # Palabra secreta para apagar la máquina.
        if eleccion.upper() == "OFF":
            check_apagado = True
        # Palabra secreta para printear el reporte con las estadísticas.
        elif eleccion.upper() == "REPORT":
            maquina_cafe.report()
            maquina_dinero.report()
        else:
            # Chequea que la eleccion ha pasado el filtro:
            if eleccion != "":
                bebida = menu.find_drink(eleccion)
                # Procesa si la máquina tiene suficientes ingredientes y la introducción de dinero en la máquina.
                if maquina_cafe.is_resource_sufficient(bebida) and maquina_dinero.make_payment(bebida.cost):
                    maquina_cafe.make_coffee(bebida)
main()


