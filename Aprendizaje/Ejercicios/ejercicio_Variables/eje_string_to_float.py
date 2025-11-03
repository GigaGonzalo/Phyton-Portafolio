"*******************************************************************"
"                   Ejercicio String a Float                        "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"

from decimal import DecimalException


var_float = 0
var_string = ""

while True:
    try:
        var = input("Ingrese un valor numerico con DECIMALES : ").strip()

        var_float = float(var)

        print(f"\nSu valor ingresado es {var_float} de tipo {type(var_float)} \n")

        var_string = str(var_float)

        print(f"Ahora su valor Decimal es {var_string} y es de tipo {type(var_string)}")

        break
    
    except ValueError:
        
        print(f"El valor {var} no es un Numero Decimal")
        