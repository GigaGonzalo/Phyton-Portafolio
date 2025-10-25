
# Se solicitan datos personales para personalizar el saludo
def informacionPersonal():
    nombre = input("Como te llamas? ")
    edad = input("Cuantos años tienes? ")
    pais = input("De que pais eres? ")
    
    print(f"\n☺ Mucho gusto {nombre}, es un placer! ")
    print(f"☺ Veo que tienes {edad} y que eres de {pais}")
    print(f"☺ Es un honor conocerte!\n")

# Se personaliza el saludo con los datos obtenidos
def SaludoInicial():
    print("HOLA! Un gusto el que estes aqui, por favor responde las siguientes preguntas: \n")
    
    informacionPersonal()


# Es la funcion inicial
def main():
    print(f"Este es mi primer proyecto en Python\n")
    print(f"="*5 + " HOLA MUNDO PLUS " + "="*5 + "\n")

    SaludoInicial()

if __name__ == "__main__":
    main()