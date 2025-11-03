"*******************************************************************"
"                   Ejercicio String a Float                        "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"

#Creacion de Variables
var_float = 0
var_string = ""
#Bucle while para peticion de dato
while True:
    #Try para validar datos numericos
    try:
        #Peticion de valor numerico
        var = input("Ingrese un valor numerico con DECIMALES : ").strip()
        #Conversion de String a Float e impresion
        var_float = float(var)

        print(f"\nSu valor ingresado es {var_float} de tipo {type(var_float)} \n")
        #Conversion de Float a String e impresion
        var_string = str(var_float)

        print(f"Ahora su valor Decimal es {var_string} y es de tipo {type(var_string)}")
        #Salida del bucle al termino
        break
    #Excepcion para Valor no Numerico
    except ValueError:
        
        print(f"El valor {var} no es un Numero Decimal")

    except Exception as e:
        print(f"Error inesperado!! {e}")
        