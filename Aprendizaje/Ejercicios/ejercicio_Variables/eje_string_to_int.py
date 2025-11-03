"*******************************************************************"
"                    Ejercicio String a Int                         "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"

#Creacion de Variables 
var_int = 0
var_string = ""

#Bucle while para peticion de dato
while True:
    #Try para validar datos numericos
    try:
        #Peticion de valor numerico
        var = input("Ingrese un numero : ")
        #Convercion de String a Int e impresion
        var_int = int(var)

        print(f"\nEl numero ingresado es un {var_int} y es de tipo {type(var_int)} \n")
        #Conversion de Int a String e impresion
        var_string = str(var_int)

        print(f"Ahora el numero que ingreso es {var_string} y  es de tipo {type(var_string)}")
        #Salida del bucle añ termino
        break
    #Excepcion para Valor no Numerico
    except ValueError:
        print("Ingrese un VALOR NUMERICO ENTERO!")
    #Excepcion para cualquier otro error
    except:
        print("Error inesperado!!")




