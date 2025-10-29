"********************************************************************"
"                    REGISTRO PERSISTENTE v1                         "
"                                                                    "
" Registro que almacena datos de manera externa para su persistencia "
"********************************************************************"
import json
import os
from datetime import datetime

# Nombre del archivo para el historial
ARCHIVO_HISTORIAL = "historial_usuarios.json"

def CargarHistorial():
    try:
        if os.path.exists(ARCHIVO_HISTORIAL):
            with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return []
    except (json.JSONDecodeError, Exception) as e:
        print(f"⚠️ Error al cargar historial: {e}")
        return []

def GuardarEnHistorial(datos_usuario):
    try:
        historial = CargarHistorial()
        datos_usuario["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datos_usuario["id"] = len(historial) + 1

        historial.append(datos_usuario)

        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            json.dump(historial, archivo, ensure_ascii=False, indent=2)

        print("Datos almacenados")
    except Exception as e:
        print(f"❌ Error al guardar en historial: {e}")
        return False
#Funcion de comprobacion de dato vacio
def ComprobacionVacio(texto):
    if len(str(texto).strip()) == 0:
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
            elif any(char.isdigit() for char in nombre):
                print("EL NOMBRE NO DEBE CONTENER NÚMEROS!!")
            else:
                valido = True
                return nombre
            
        except ValueError:
            print("INGRESE DATOS VALIDOS!!")
            return
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario")
            exit()
    
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
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario")
            exit()

#Funcion de peticion del dato PAIS
def PeticionPais():
    valido = False
    paises_permitidos = {"Mexico", "Alemania", "Yugoslavia", "Berlin"}
    while valido == False:
        try:
            pais = input("De que pais nos visitas?   \n")
            
            if ComprobacionVacio(pais) == True:
                print("EL CAMPO NO PUEDE QUEDAR VACIO!! ")
            elif any(char.isdigit() for char in pais):
                    print("EL PAIS NO DEBE CONTENER NÚMEROS!! ")
            elif pais not in paises_permitidos:
                print("Su pais no es miembro, acceso DENEGADO!! ")
            else:
                valido = True
                return pais
        except ValueError:
            print("INGRESE DATOS VALIDOS!!")
            return
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario")
            exit()

def RegistroUsuario():
    datos_usuario = {"nombre" : PeticionNombre(), "edad" : PeticionEdad(),
                     "pais" : PeticionPais()}
    GuardarEnHistorial(datos_usuario)

def ConsultaUsuario():
    try:
        id = input("Ingrese el ID del usuario a Consultar: ")
        if ComprobacionVacio(id) == True:
            print("EL CAMPO NO PUEDE QUEDAR VACIO!! ")
        #elif id in :
            
        
    except ValueError:
        print("INGRESE SOLAMENTE DIGITOS NUMERICOS!!  (0,1,2...)")
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
        exit()

def main():

    print("*"*90)
    print("\nBienvenido al Menu de Registro de Usuarios - MRU \n")
    print("*"*90)
    print("Elija la opcion correspondiente : ")
    print("1. Registrar Usuario ")
    print("2. Eliminar Usuario ")
    print("3. Modificar Usuario ")
    print("4. Consultar Usuario ")
    print("5. SALIR ")

    seleccion = input("Ingrese opcion: ")

    if seleccion is "1":
        RegistroUsuario()
    #elif seleccion is "2":
        #EliminarUsuario()
    #elif seleccion is "3":
        #ModificarUsuario()
    elif seleccion is "4":
        ConsultaUsuario()
    #elif seleccion is "5":
        #CierrePrograma()
    else:
        print("Ingrese una opcion VALIDA!! ")


#Condicion de ejecucion
if __name__ == "__main__":
    main()