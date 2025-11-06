"*******************************************************************"
"               Ejercicio Integrador de Conversiones                "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"


import json
import os
from datetime import datetime
from typing import Any, Dict
from weakref import ref

#Inicializacion de variables globales
usuario_registro = {"id" : 0 ,"nombre" : "", "apellido": "", "edad" : 0 , "carrera" : "", "altura" : 0 , 
                    "peso" : 0 , "casado?" : False }

lista_Usuarios = []

url_archivo_usuarios = "registro_usuarios_ext.json"

def cargarRegistro() -> Any:
    """
    Carga el registro de usuarios desde el archivo JSON
    
    Args:
        
    Returns:
        list: Diccionarios de los usuarios
    """
    try:
        if os.path.exists(url_archivo_usuarios):
            with open(url_archivo_usuarios, "r") as archivo:
                return json.load(archivo)
        else:
            return []
    except (json.JSONDecodeError, Exception) as e:
        print("ERROR AL CARGAR EL HISTORIAL")

def guardarRegistro(datos_usuario: dict):
    """
    Guarda los datos en el archivo JSON
    
    Args:
        
    Returns:

    """
    try:
        registro = cargarRegistro()
        for id_usu in registro:
            if id_usu.get("id") == datos_usuario.get("id"):
                datos_usuario["id"] = id_usu["id"]
                id_usu.update(datos_usuario)
                break
        else:
            datos_usuario["fecha_registro"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            registro.append(datos_usuario)

        with open(url_archivo_usuarios, "w" ) as archivo:
            json.dump(registro, archivo, ensure_ascii=False, indent=2)

        print("DATOS GUARDADOS EXITOSAMENTE")
    
    except Exception as e:
        print(f"ERROR AL GUARDAR EL REGISTRO:  {e}")
        return False

def guardarXEliminacion(registro_act: list):
    """
    Guarda el registro pos-eliminacion de usuario
    
    Args:
        registro_act (list): Registro actualizado para almacenamiento
        
    Returns:
        
    """
    with open(url_archivo_usuarios, "w" ) as archivo:
            json.dump(registro_act, archivo, ensure_ascii=False, indent=2)

def ordenamientoXEliminacion(reg: list) -> list:
    """
    Ordena la lista con usuario eliminado y reindexa
    
    Args:
        reg (list): Lista con "hueco" de usuarios
        
    Returns:
        list: Lista acomodada y reindexada
    """
    reg.sort(key=lambda x: x["id"])
    index = 1
    print(reg)
    for usu in reg:
        usu["id"] = index
        index += 1
    return reg

#Funcion de comprobacion de Vacios
def comp_Vacio(txt: str) -> bool:
    """
    Verifica la existencia de espacios en blanco en entradas
    
    Args:
        txt (str): Entradas de string
        
    Returns:
        bool: La existencia o no de espacios en blanco
    """
    if len(txt) <= 0:
        print("EL CAMPO NO PUEDE QUEDAR VACIO!!!")
        return True
    else:
        return False
    
#Funcion de Formato: Primera letra mayuscula
def format_Mayus(txt: str) -> str:
    """
    Formato de primer letra mayuscula
    
    Args:
        txt (str): Entrada de string
        
    Returns:
        str: Texto con formato capital
    """
    return str(txt).capitalize()

#Funcion de comprobacion de Edades Validas
def comp_Edad(num : int):
    """
    Valida la edad ingresada
    
    Args:
        num (int): Edad en años
        
    Returns:
        bool: Si es valida o no
    """
    if 18 <= num < 120:
        return True
    elif num < 0:
        print("LA EDAD NO PUEDE SER UN VALOR NEGATIVO!!")
    elif num < 18:
        print("MENOR DE EDAD!! ACCESO DENEGADO!! ")
        return False
    elif num >= 120:
        print("EDAD INVALIDA --FUERA DE RANGO (18-119) ")
        return False
    
#Funcion de comprobacion de Altura Validas
def comp_Altura(alt: float):
    """
    Valida la altura ingresada
    
    Args:
        alt (float): Altura en metros
        
    Returns:
        bool: Si es valida o no
    """
    if 1.10 < alt < 2.51:
        return True
    elif alt < 0:
        print("LA ALTURA NO PUEDE SER UN VALOR NEGATIVO!!")
    else:
        print("ALTURA INVALIDA   --FUERA DE RANGO (1.10 mts - 2.50 mts)")
        return False
#Funcion de comprobacion de Pesos Validos
def comp_Peso(pe : float):
    """
    Valida el peso ingresado
    
    Args:
        pe (float): Peso en kilogramos
        
    Returns:
        bool: Si es valida o no
    """
    if 39 < pe < 269:
        return True
    elif pe < 0:
        print("EL PESO NO PUEDE SER UN VALOR NEGATIVO!!")
    else:
        print("PESO INVALIDO   --FUERA DE RANGO (39 kg - 269 kg)")
        return False
#Funciones de Peticiones de DATOS
def peticionNombre() -> str:
    """
    Solicita el nombre del usuario
    
    Args:
        
    Returns:
        str: El nombre del usuario
    """
    while True: 
        try: 
            var = input("Ingrese su NOMBRE : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
                
        except ValueError:
            print("Ingrese un dato valido!!")
    
def peticionApelllido() -> str:
    """
    Solicita el apellido del usuario
    
    Args:
        
    Returns:
        str: El apellido del usuario
    """
    while True: 
        try:
            var = input("Ingrese su Apellido : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionEdad() -> int:
    """
    Solicita la edad del usuario
    
    Args:
        
    Returns:
        int: La edad del usuario
    """
    while True: 
        try:
            var = input("Ingrese su Edad : ").strip()
            if comp_Vacio(var) == False and comp_Edad(int(var)) == True:
                return int(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionCarrera() -> str:
    """
    Solicita la carrera del usuario
    
    Args:
        
    Returns:
        str: La carrera del usuario
    """
    while True: 
        try:
            var = input("Ingrese su Carrera : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionAltura() -> float:
    """
    Solicita la altura del usuario
    
    Args:
        
    Returns:
        float: La altura del usuario
    """
    while True: 
        try:
            var = input("Ingrese su Altura : ").strip()
            if comp_Vacio(var) == False and comp_Altura(float(var)) == True:
                return float(var)
        except ValueError:
            print("Ingrese un dato valido!!")
        
def peticionPeso() -> float:
    """
    Solicita el peso del usuario
    
    Args:
        
    Returns:
        float: El peso del usuario
    """
    while True: 
        try:
            var = input("Ingrese su Peso : ").strip()
            if comp_Vacio(var) == False and comp_Peso(float(var)) == True:
                return float(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionEstadoCivil() -> bool:
    """
    Solicita el estado civil del usuario
    
    Args:
        
    Returns:
        bool: El estado civil del usuario
    """
    while True: 
        try:
            var = input("Es usted Casado/a [S] o [N] : ").strip().upper()
            if comp_Vacio(var) == False :
                if var == "S":
                    return True
                elif var == "N":
                    return False
                else:
                    print("Ingrese una LETRA VALIDA!!   (S/N)")
        except Exception as e:
            print("Ingrese un dato VALIDO!!")
#Funcion de generacion de ID
def gen_ID() -> int:
    """
    Genera el ID del usuario
    
    Args:
        
    Returns:
        int: El ID del usuario
    """
    registro = cargarRegistro()
    print(len(registro))
    id = len(registro)+1
    return id

#Funcion de resumen de datos de registro
def resumen_Registro(registro : Any):
    """
    Muestra los datos del usuario para confirmacion y los almacena
    
    Args:
        dict: Los datos del usuario
        
    Returns:

    """
    global lista_Usuarios
    print(f"DATOS DEL USUARIO A REGISTRAR \nID : {registro['id']} \nNombre : {registro['nombre']} \nApelido : {registro['apellido']}" +
           f"\nEdad : {registro["edad"]} \nCarrera : {registro["carrera"]}\nAltura : {registro["altura"]}"+
           f"\nPeso : {registro["peso"]} \nCasado : " + ("Si" if registro.get("casado?") == True else "NO" ))
    var = input("Los datos capturados son CORRECTOS? [S] o [N] : ").strip().upper()
    if comp_Vacio(var) == False :
        if var == "S":
            print(registro)
            lista_Usuarios.append(registro)
            guardarRegistro(registro)
            print("DATOS DEL USUARIO ALMACENADOS!!!!! ")
            print(registro)
            main()
        elif var == "N":
            modificar_Registro(registro)
        else:
            print("Ingrese una LETRA VALIDA!!   (S/N)")
            
def resumen_Usuario(registro : Any):
    """
    Muestra solo los datos del usuario 
    
    Args:
        dict: Los datos del usuario
        
    Returns:

    """
    print(f"DATOS DEL USUARIO REGISTRADO \nID : {registro['id']} \nNombre : {registro['nombre']} \nApelido : {registro['apellido']}" +
           f"\nEdad : {registro["edad"]} \nCarrera : {registro["carrera"]}\nAltura : {registro["altura"]}"+
           f"\nPeso : {registro["peso"]} \nCasado : " + ("Si" if registro.get("casado?") == True else "NO" ))
    var = input("Presione S para regresar al MENU [S] : ").strip().upper()
    if comp_Vacio(var) == False :
        if var == "S":
            main()
       
        else:
            print("Ingrese una LETRA VALIDA!!   (S)")

#Funcion tipo Menu de modificacion de datos individuales
def modificar_Registro(registro):
    """
    Modifica los datos del usuario 
    
    Args:
        dict: Los datos del usuario
        
    Returns:
        dict: Los datos del usuario para validacion
    """
    opciones_menu = [1,2,3,4,5,6,7,8]
    
    while True: 
        try:
            print("INGRESE EL NUMERO DE LA OPCCION CON EL DATO A MODIFICAR : ")
            print("1. NOMBRE")
            print("2. APELLIDO")
            print("3. EDAD")
            print("4. CARRERA")
            print("5. ALTURA")
            print("6. PESO")
            print("7. ESTADO CIVIL")
            print("8. CONFIRMAR DATOS")
            op = input("Ingrese opcion deseada : ")
            op = int(op)
            if op in opciones_menu:
                if op == 1:
                    n_nombre = peticionNombre()
                    registro["nombre"] = n_nombre
                elif op == 2:
                    n_apellido = peticionApelllido()
                    registro["apellido"] = n_apellido
                elif op == 3:
                    n_edad = peticionEdad()
                    registro["edad"] = n_edad
                elif op == 4:
                    n_carrera = peticionCarrera()
                    registro["carrera"] = n_carrera
                elif op == 5:
                    n_altura = peticionAltura()
                    registro["altura"] = n_altura
                elif op == 6:
                    n_peso = peticionPeso()
                    registro["peso"] = n_peso
                elif op == 7:
                    n_estadoCivil = peticionEstadoCivil()
                    registro["casado?"] = n_estadoCivil
                elif op == 8:
                    print(registro)
                    resumen_Registro(registro)
            else:
                print("INGRESE UNA OPCION VALIDA!")
        except ValueError:
            print("INGRESE UNA OPCION VALIDA!")
#Funcion de registro de Usuario
def registro_Usuario():
    """
    Solicita los datos del usuario para confirmacion y almacenamiento
    
    Args:
        
    Returns:
        dict: Los datos del usuario recabados
    """
    print("\nIngrese los datos del Usuario a Registrar, por favor!! \n")

    usu_id = gen_ID()
    usu_nombre = peticionNombre()
    usu_apellido = peticionApelllido()
    usu_edad = peticionEdad()
    usu_carrera = peticionCarrera()
    usu_altura = peticionAltura()
    usu_peso = peticionPeso()
    usu_esCasado = peticionEstadoCivil()

    usuario_registro = {"id" : usu_id ,"nombre" : usu_nombre, "apellido": usu_apellido, "edad" : usu_edad , "carrera" : usu_carrera, "altura" : usu_altura , 
                    "peso" : usu_peso , "casado?" : usu_esCasado }
    
    resumen_Registro(usuario_registro)

#Funcion tipo Menu de modificacion de datos individuales
def eliminar_Registro(dic_usuario):
    """
    Elimina el registro del usuario seleccionado por ID
    
    Args:
        dict: Los datos del usuario
        
    Returns:
        list: El registro de usuarios actualizado
    """
    print(dic_usuario)
    var = input(f"LOS DATOS DEL USUARIO CON EL ID {dic_usuario.get("id")} SERAN ELIMINADOS PERMANENTEMENTE? [S] o [N] : ").strip().upper()
    if comp_Vacio(var) == False :
        if var == "S":
            
            registro = cargarRegistro()
            print(registro)
            registro.pop(dic_usuario.get("id")-1)
            print(registro)
            registro = ordenamientoXEliminacion(registro)
            guardarXEliminacion(registro)
            print("DATOS DEL USUARIO ELIMINADOS!!!!! ")
            main()
        elif var == "N":
            main()
    else:
            print("Ingrese una LETRA VALIDA!!   (S/N)")

#Funcion de Busqueda por ID
def busqueda_Usuario():
    """
    Busca los datos del usuario en el registro por medio del ID
    
    Args:
        
    Returns:
        dict: El registro del usuario buscado

    """
    id_usu = input("Ingrese el ID del usuario : ")
    id_usu = int(id_usu)
    registro = cargarRegistro()
    for iter in registro:
        if iter.get('id') == id_usu:
            return iter

#Funcion Principal de recoleccion de datos e impresion del registro
def main():
    """
    Muestra el menu principal
    
    """
    
    print("*"*10 + "BIENVENIDOS AL REGISTRO DE USUARIOS v1" + "*"*10 + "\n") #58
    print("*"*23 + "     MENU     " + "*"*23 + "\n")
    opciones_menu = [1,2,3,4,5]
    while True: 
        try:
            print("INGRESE LA OPCCION DE LA OPERACION : ")
            print("1. REGISTAR USUARIO")
            print("2. ELIMINAR USUARIO")
            print("3. MODIFICAR USUARIO")
            print("4. CONSULTAR USUARIO")
            print("5. SALIDA")
            op = input("Ingrese opcion deseada : ")
            op = int(op)
            if op in opciones_menu:
                if op == 1:
                    registro_Usuario()
                elif op == 2:
                    usu = busqueda_Usuario()
                    eliminar_Registro(usu)
                elif op == 3:
                    usu = busqueda_Usuario()
                    modificar_Registro(usu)
                elif op == 4:
                    usu = busqueda_Usuario()
                    resumen_Usuario(usu)
                elif op == 5:
                    exit()
            else:
                print("INGRESE UNA OPCION VALIDA!")
        except ValueError:
            print("INGRESE UNA OPCION VALIDA!")

#Funcion inicial
if __name__ == "__main__":
    """
    Inicia el programa
    
    """
    main()