# def sum(a, b):
#     result = a + b
#     return result


# def main():
#     print(sum(1, 2))
#     print(sum(3, 4))


# main()


# def sayHi(name):
#     print("Hi " + name)


# sayHi("Juan")


# def saludo(name):

#     lista_nombres = []

#     for i in range(cantidad_nombres):

#         lista_nombres.append(input("Ingrese un nombre: "))

#     print(lista_nombres)

#     for i in lista_nombres:
#         print("Hola " + i)


# cantidad_nombres = int(input("Ingrese la cantidad de nombres: "))
# saludo(cantidad_nombres)


def saludo(cantidad_saludos):

    lista_nombres = []

    for i in range(cantidad_saludos):

        nombre = input("Ingrese un nombre: ")
        print("Hola " + nombre)

        lista_nombres.append(nombre)

    print(lista_nombres)

    return lista_nombres


#
# print(nombres)

def orden(lista, sentido):

    lista.sort(reverse=sentido)
    return lista


nombres = saludo(int(input("Ingrese la cantidad de saludos: ")))

print(orden(nombres, False))
