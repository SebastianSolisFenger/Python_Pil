# for

# for i in range(10):
#     print(i)

# list = [1, 2, False, True, 'hola', 'mundo']

# for i in list:
# print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# list = []

# for i in range(10):
#     list.append(i)

# print(list)

# list = []

# for i in range(3):

#     list.append(int(input('Ingrese un numero: ')))
# print(list)


# while
# x = 10

# while x > 0:
#     print(x)

#     x -= 1


# function ATM


# x = 5
# if x == 5:
#     print("Es 5")
# elif x == 6:
#     print("Es 6")
# elif x == 7:
#     print("Es 7")

# x = 4
# if x == 5:
#     print("Es 5")
# elif x == 6:
#     print("Es 6")
# elif x == 7:
#     print("Es 7")
# else:
#     print("Es otro")

# Verifica si un número es par o impar
# x = 5
# if x % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")


# x = 5
# while x > 0:
#     x -= 1
#     print(x)
# else:
#     print("El bucle ha finalizado")


# -*- coding: utf -8 -*-
# import os


# class Cajero:

#     def __init__(self):
#         self.continuar = True
#         self.monto = 5000
#         self.menu()

#     def contraseña(self):
#         contador = 1
#         while contador <= 3:
#             x = int(input("ingrese su contraseña:"))
#             if x == 5467:
#                 print("Contraseña Correcta")
#                 break
#             else:
#                 print(
#                     f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
#                 if contador == 3:
#                     print("No puede realizar operaciones.")
#                     self.continuar = False
#                 contador += 1

#     def menu(self):
#         os.system("cls")  # esto es solo para windows
#         self.contraseña()
#         opcion = 0
#         while opcion != "4":
#             os.system("cls")
#             print(""" Bienvenido al cajero automatico
#             ******Menú******
#             1-  Depositar
#             2- Retirar
#             3- Ver saldo
#             4- Salir """)
#             opcion = input("Su opción es: ")
#             if self.continuar:
#                 if opcion == "1":
#                     self.depositar()
#                 elif opcion == "2":
#                     self.retiro()
#                 elif opcion == "3":
#                     self.ver()
#                 elif opcion == "4":
#                     print("Programa finalizado")
#                 else:
#                     print("NO existe esa opción")
#             else:
#                 if opcion in "123":
#                     print("Imposible realizar esa operación")
#                 elif opcion == "4":
#                     print("Programa finalizado")
#                 else:
#                     print("No existe esa opción")

#     def depositar(self):
#         dep = int(input("Ingrese su monto a depositar:"))
#         print("Usted a depositado", dep)
#         print(f"Su nuevo saldo es {self.monto + dep}")
#         self.monto += dep

#     def retiro(self):
#         retirar = int(input("¿Cuánto desea retirar? : "))
#         print("Su monto actual es", self.monto)
#         if self.monto >= girar:
#             print(
#                 f"Usted a retirado: {retirar} , su nuevo monto es {self.monto - retirar}")
#             self.monto -= retirar
#         else:
#             print("Imposible realizar el retiro, su monto es menor")

#     def ver(self):
#         print("Su saldo es: ", self.monto)


# app = Cajero()


# Realiza un programa en python de cajero automático, con un saldo inicial de $1000, en el se podrá retirar,
# depositar. Debe de estar en un bucle.


# Importar libreria para los colores
import os
from colorama import Fore, init
init()

# COLORES
azul = Fore.LIGHTBLUE_EX
verde = Fore.LIGHTGREEN_EX
rojo = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX



 # limpiar pantalla

def clearConsole(): return os.system('cls' if os.name in (
    'nt', 'dos') else 'clear') 


# banner

def __banner__():
    print(rojo+"""
    
      ______     ___            __   _______ .______        ______   
     /      |   /   \          |  | |   ____||   _  \      /  __  \  
    |  ,----'  /  ^  \         |  | |  |__   |  |_)  |    |  |  |  | 
    |  |      /  /_\  \  .--.  |  | |   __|  |      /     |  |  |  | 
    |  `----./  _____  \ |  `--'  | |  |____ |  |\  \----.|  `--'  | 
     \______/__/     \__\ \______/  |_______|| _| `._____| \______/  
                                                                 
       
    """)


clearConsole()
saldo = 1000

while True:

    __banner__()

    print("ESCOGE ALGUNA OPCIÓN")
    print(cyan+"\n1 - Retirar dinero")
    print(cyan+"\n2 - Depositar dinero")
    print(cyan+"\n3 - Salir del cajero")

    opc = int(input(verde+"\n->> "))

    if opc == 1:  # Retirar
        clearConsole()
        retirar = float(input("Cuanto vas a retirar?: "))

        if retirar > saldo:
            clearConsole()
            print(azul+"Error, no tienes esa cantidad disponible")

        else:
            clearConsole()
            saldo = saldo - retirar
            print(cyan+"Listo, tu nuevo saldo es de: ", saldo)

    elif opc == 2:  # Adiccionar
        clearConsole()
        agregar = float(input("Cuanto vas a depositar?: "))

        saldo = agregar + saldo
        clearConsole()

        print(cyan+"Se agrego exitosamente, tu nuevo saldo es de: ", saldo)

    elif opc == 3:  # salir
        clearConsole()
        print(Fore.MAGENTA+"Hasta luego")
        break

    else:
        clearConsole()
        print(Fore.MAGENTA+"La opcion no existe, intentalo de nuevo")
