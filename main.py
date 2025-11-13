#importacion de archivos
from functions import suma
from calculos import area_triangulo
from calculos import area_cuadrado
from calculos import area_circulo
#programa
print("Practicas git 13/11/2025")

while True:
    #Creacion del menu y solicitud de operacion
    print("Seleccione la operacion a realizar:")
    print("1.Area del cuadrado")
    print("2.Area del triangulo")
    print("3.Suma")
    print("4.Salir")
    print("5.Area del circulo")
    #Se solicita la opcion al usuario
    eleccion = input("Ingrese la opcion: ")
    #si el ususario escoge la opcion 1 se realiza el area del cuadrado
    if eleccion == '1':
        #Se solicita la medida del lado del cuadrado
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        #Se muestra el resultado
        print("El area del cuadrado es:", area_cuadrado(lado))
    #Si el usuario escoge la opcion 2 se realiza el area del triangulo
    elif eleccion == '2':
        #Se solicitan la base y la altura del triangulo
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        #Se muestra el resultado
        print("El area del triangulo es:", area_triangulo(base, altura))
    #Si el usuario escoge la opcion 3 se realiza la suma
    elif eleccion == '3':
        #Se solicitan los numeros a sumar
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        #Se muestra el resultado
        print("La suma es:", suma(num1, num2))
    #Si el usuario escoge la opcion 4 se sale del programa
    elif eleccion == '4':
        print("Saliendo del programa.")
    elif eleccion=='5':
        radio = float(input("Ingrese el radio del circulo: "))
        print("El area del circulo es:", area_circulo(radio))
        break




