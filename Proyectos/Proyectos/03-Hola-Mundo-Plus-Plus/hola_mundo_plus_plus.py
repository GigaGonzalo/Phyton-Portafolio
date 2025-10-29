"*******************************************************************"
"                HOLA MUNDO PERSONALIZADO v3                        "
"                                                                   "
"    Un saludo personalizado recogiendo informacion del usuario     "
"*******************************************************************"

#Funcion de Saludo personalizado usando la informacion recabada
def SaludoPersonalizado(nombre, edad, pais):
    print(f"Un gusto conocerte {nombre}, gracias por compartir tu informacion")
    print(f"Veo que tienes {edad} años y que nos visitas desde {pais}!!")
    print(f"Es un honor poderme ejecutar para ti {nombre}!!")

#Funcion de comprobacion de dato vacio
def ComprobacionVacio(texto):
    texto = str(texto)
    if len(texto) <= 0:
        return True
    else:
        return False 

#Funcion de peticion del dato Nombre
def PeticionNombre():
    valido = False
    while valido == False:
        try:
            nombre = input(f"Como te llamas?  \n")

            if ComprobacionVacio(nombre) == True:
                print("EL CAMPO NO PUEDE QUEDAR VACIO!! ")
            else:
                valido = True
                return nombre
            
        except:
            print("INGRESE DATOS VALIDOS!!")
            return
    
#Funcion de peticion del dato EDAD
def PeticionEdad():
    valido = False
    while valido == False:
        try:

            edad = int(input("Que edad tienes ?   \n"))
            
            if ComprobacionVacio(edad) == True:
                print("EL CAMPO NO PUEDE QUEDAR VACIO!! ")
            else:
                if 18 < edad < 110:
                    valido = True
                    return edad
                else:
                    print("INGRESE UNA EDAD VALIDA!! (entre 18 y 110)")
        
        except ValueError:
            print("INGRESE SOLAMENTE DIGITOS NUMERICOS!!  (0,1,2...)")

#Funcion de peticion del dato PAIS
def PeticionPais():
    valido = False
    while valido == False:
        
        pais = input("De que pais nos visitas?   \n")
        
        if ComprobacionVacio(pais) == True:
            print("EL CAMPO NO PUEDE QUEDAR VACIO!! ")
        else:
            valido = True
            return pais

#Funcion de bienvenida al usuario
def Bienvenida():
    print("\nHola usuario, un gusto tenerlo aqui!")
    print("Soy Hola Mundo v3, un programa de saludos personalizados")
    print("Pero hablame de ti, te parece? ")

    SaludoPersonalizado(PeticionNombre(), PeticionEdad(), PeticionPais())

#Funcion Primaria
def main():
    print(f"Tercer variacion del mitico Hola Mundo Personalizado \n")
    print(f"="*90 + "\n      HOLA MUNDO v.3      \n" + "="*90 + "\n")

    Bienvenida()

#Condicion de ejecucion
if __name__ == "__main__":
    main()