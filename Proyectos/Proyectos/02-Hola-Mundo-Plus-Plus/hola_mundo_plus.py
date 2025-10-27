"""
Hola Mundo Plus - Proyecto Python
Un saludo personalizado interactivo que recoge informacion del usuario

"""
#Funcion de comprobacion de Vacios para volver a solicitar informacion
def ComprobacionDeVacio(nombre):
    print(len(nombre.strip()))
    if (len(nombre.strip()) > 0) == False:
        print(f"EL CAMPO NO PUEDE ESTAR VACIO!!")
        return False
    else:
        return True

#Funcion para comprobar rango de edad valido
def ComprobacionEdad(edad):
    print(edad)
    edadC = int(edad)
    print(edadC)
    if edadC > 0 : 
        if edadC < 110:
            return True
        else:
            print(f"INGRESE UNA EDAD VALIDA!")
            return False

#Funcion de peticion y comprobacion de Nombre
def PeticionNombre():
    nombreP = ""
    while ComprobacionDeVacio(nombreP) == False:
        nombreP = input(f"Ingrese su nombre : ")
    return nombreP

#Funcion de peticion y comprobacion de Edad
def PeticionEdad():
    edadP = ""
    while ComprobacionDeVacio(edadP) == False:
        edadP = input(f"Ingrese su edad : ")
        if ComprobacionEdad(edadP) == True:
            return edadP
        else:
            edadP = ""

#Funcion de peticion y comprobacion de Pais
def PeticionPais():
    paisP = ""
    while ComprobacionDeVacio(paisP) == False:
        paisP = input(f"Ingrese su pais : ")
    return paisP
    

#Saludo personalizado con la informacion del usuario
def SaludoPersonalizado(nombre, edad, pais):
    print("*"*130 + "\n")
    print(f" Es un gusto saludarte {nombre}, veo que tienes {edad} y nos visitas desde {pais}")
    print(f" Es un honor!\n")
    print("*"*130)

#Funcion de bienvenida y ejecucion
def Apertura():
    print("="*130 + "\n" + f"BIENVENIDOS VISITANTES \n" + "="*130)
    print(f"Llene los siguientes campos por favor!")
    SaludoPersonalizado(PeticionNombre(), PeticionEdad(), PeticionPais())

#Funcion Primaria
def main():
    print(f"Este es mi primer proyecto en Python pero mejorado\n")
    print(f"="*5 + " HOLA MUNDO PLUS " + "="*5 + "\n")

    Apertura()

#Condicion de ejecucion
if __name__ == "__main__":
    main()
