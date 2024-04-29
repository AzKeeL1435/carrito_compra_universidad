import os
import random

clear = lambda: os.system("cls")

#Stock
Pears = random.randint(0, 50)
Apples = random.randint(0, 50)
Oranges = random.randint(0, 50)

#Prices
Pear_price = 0.75
Apple_price = 0.50
Orange_price = 0.25

#User
shopping_cart = [0, 0, 0]
identification = 0

print("Tienda whaveter bienvenido")

while True:
    print("1. Agregar producto\n2. Mostrar pedido\n3. Pagar\n0. Salir")
    menu_option = input("Opcion: ")
    
    if menu_option == "0": # Salir
        break
    elif menu_option == "1": # Agregar producto
        clear()
        print(f"Fruta:  Cantidad\n1. Peras {Pears}\n2. Manzanas {Apples}\n3. Naranjas {Oranges}")
        product_option = int(input("Ingrese el producto a agregar: "))
        if product_option == 1: # pears
            user_quantity = int(input("Ingrese la cantidad de peras: "))
            if user_quantity <= Pears:
                shopping_cart[0] += user_quantity
                Pears -= user_quantity
            else:
                print("no hay suficientes stock")
        if product_option == 2: # apples
            user_quantity = int(input("Ingrese la cantidad de Manzanas: "))
            if user_quantity <= Apples:
                shopping_cart[1] += user_quantity
                Apples -= user_quantity
            else:
                print("no hay suficientes stock")
        if product_option == 3: # oranges
            user_quantity = int(input("Ingrese la cantidad de Naranjas: "))
            if user_quantity <= Oranges:
                shopping_cart[2] += user_quantity
                Oranges -= user_quantity
            else:
                print("no hay suficientes stock")
    elif menu_option == "2": # Mostrar carrito
        clear()
        print(f"Peras: {shopping_cart[0]}\nManzanas: {shopping_cart[1]}\nNaranjas: {shopping_cart[2]}\n\nSiendo un total de ${shopping_cart[0]*Pear_price + shopping_cart[1]*Apple_price + shopping_cart[2]*Orange_price}")
        input("Presione enter para salir")
        clear()
    elif menu_option == "3": # Pagar
        clear()
        while True:
            identification = input("Ingrese su documento: ")
            if len(identification) >= 6 and len(identification) <= 12:
                print(f"Numero de factura {random.randint(000000,999999)} a la identificacion {identification}\nPeras: {shopping_cart[0]}\nManzanas: {shopping_cart[1]}\nNaranjas: {shopping_cart[2]}\n\nSiendo un total de ${shopping_cart[0]*Pear_price + shopping_cart[1]*Apple_price + shopping_cart[2]*Orange_price}")
                input("presione enter para continuar")
                clear()
                shopping_cart = [0,0,0]
                break
            else:
                print("Identificacion no valida, intente de nuevo")
