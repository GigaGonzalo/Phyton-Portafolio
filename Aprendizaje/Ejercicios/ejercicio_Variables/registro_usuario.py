"*******************************************************************"
"               Ejercicio Integrador de Conversiones                "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"
#Inicializacion de variables globales
usuario_registro = {"id" : 0 ,"nombre" : "", "apellido": "", "edad" : 0 , "carrera" : "", "altura" : 0 , 
                    "peso" : 0 , "casado?" : False }

lista_Usuarios = []

#Funcion de comprobacion de Vacios
def comp_Vacio(txt):
    if len(txt) <= 0:
        print("EL CAMPO NO PUEDE QUEDAR VACIO!!!")
        return True
    else:
        return False
    
#Funcion de Formato: Primera letra mayuscula
def format_Mayus(txt):
    mayus = []
    cont = 1
    for c in txt:
        if cont == 1:
            mayus.append(str(c).upper())
            cont += 1
        else:
            mayus.append(str(c).lower())
            cont += 1
    formato =  "".join(mayus)
    print(formato)
    return formato 


        
#Funcion de comprobacion de Edades Validas
def comp_Edad(num):
    num = int(num)
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
def comp_Altura(alt):
    alt = float(alt)
    if 1.10 < alt < 2.51:
        return True
    elif alt < 0:
        print("LA ALTURA NO PUEDE SER UN VALOR NEGATIVO!!")
    else:
        print("ALTURA INVALIDA   --FUERA DE RANGO (1.10 mts - 2.50 mts)")
        return False
#Funcion de comprobacion de Pesos Validos
def comp_Peso(pe):
    pe = float(pe)
    if 39 < pe < 269:
        return True
    elif pe < 0:
        print("EL PESO NO PUEDE SER UN VALOR NEGATIVO!!")
    else:
        print("PESO INVALIDO   --FUERA DE RANGO (39 kg - 269 kg)")
        return False
#Funciones de Peticiones de DATOS
def peticionNombre():
    while True: 
        try: 
            var = input("Ingrese su NOMBRE : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
                
        except ValueError:
            print("Ingrese un dato valido!!")
    
def peticionApelllido():
    while True: 
        try:
            var = input("Ingrese su Apellido : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionEdad():
    while True: 
        try:
            var = input("Ingrese su Edad : ").strip()
            if comp_Vacio(var) == False and comp_Edad(var) == True:
                return int(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionCarrera():
    while True: 
        try:
            var = input("Ingrese su Carrera : ").strip()
            if comp_Vacio(var) == False :
                return format_Mayus(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionAltura():
    while True: 
        try:
            var = input("Ingrese su Altura : ").strip()
            if comp_Vacio(var) == False and comp_Altura(var) == True:
                return float(var)
        except ValueError:
            print("Ingrese un dato valido!!")
        
def peticionPeso():
    while True: 
        try:
            var = input("Ingrese su Peso : ").strip()
            if comp_Vacio(var) == False and comp_Peso(var) == True:
                return float(var)
            
        except ValueError:
            print("Ingrese un dato valido!!")

def peticionEstadoCivil():
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
def gen_ID():
    global lista_Usuarios

    id = len(lista_Usuarios) + 1

    return id

#Funcion de resumen de datos de registro
def resumen_Registro(registro):
    global lista_Usuarios
    print(f"DATOS DEL USUARIO REGISTRADO \nID : {registro['id']} \nNombre : {registro['nombre']} \nApelido : {registro['apellido']}" +
           f"\nEdad : {registro["edad"]} \nCarrera : {registro["carrera"]}\nAltura : {registro["altura"]}"+
           f"\nPeso : {registro["peso"]} \nCasado : " + ("Si" if registro.get("casado?") == True else "NO" ))
    var = input("Los datos capturados son CORRECTOS? [S] o [N] : ").strip().upper()
    if comp_Vacio(var) == False :
        if var == "S":
            print("DATOS DEL USUARIO ALMACENADOS!!!!! ")
            lista_Usuarios.append(registro)
            #usuario_registro.clear
            print(lista_Usuarios)
            main()
        elif var == "N":
            modificar_Registro(registro)
        else:
            print("Ingrese una LETRA VALIDA!!   (S/N)")

#Funcion tipo Menu de modificacion de datos individuales
def modificar_Registro(registro):
    opciones_menu = [1,2,3,4,5,6,7,8]
    global usuario_registro
    usuario_registro = registro
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
                    usuario_registro["nombre"] = n_nombre
                elif op == 2:
                    n_apellido = peticionApelllido()
                    usuario_registro["apellido"] = n_apellido
                elif op == 3:
                    n_edad = peticionEdad()
                    usuario_registro["edad"] = n_edad
                elif op == 4:
                    n_carrera = peticionCarrera()
                    usuario_registro["carrera"] = n_carrera
                elif op == 5:
                    n_altura = peticionAltura()
                    usuario_registro["altura"] = n_altura
                elif op == 6:
                    n_peso = peticionPeso()
                    usuario_registro["peso"] = n_peso
                elif op == 7:
                    n_estadoCivil = peticionEstadoCivil()
                    usuario_registro["casado?"] = n_estadoCivil
                elif op == 8:
                    resumen_Registro(usuario_registro)
            else:
                print("INGRESE UNA OPCION VALIDA!")
        except ValueError:
            print("INGRESE UNA OPCION VALIDA!")
#Funcion de registro de Usuario
def registro_Usuario():
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
def eliminar_Registro(id):
    global lista_Usuarios
    var = input(f"LOS DATOS DEL USUARIO CON EL ID {id.get("id")} SERAN ELIMINADOS PERMANENTEMENTE? [S] o [N] : ").strip().upper()
    if comp_Vacio(var) == False :
        if var == "S":
            print("DATOS DEL USUARIO ELIMINADOS!!!!! ")
            del lista_Usuarios[id.get("id")-1]
            #usuario_registro.clear
            print(lista_Usuarios)
            main()
        elif var == "N":
            main()
        else:
            print("Ingrese una LETRA VALIDA!!   (S/N)")

#Funcion de Busqueda por ID
def busqueda_Usuario():
    id_usu = input("Ingrese el ID del usuario : ")
    id_usu = int(id_usu)
    for iter in lista_Usuarios:
        print(iter)
        if iter.get('id') == id_usu:
            print(iter)
            return iter

#Funcion Principal de recoleccion de datos e impresion del registro
def main():
    
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
                    resumen_Registro(usu)
                elif op == 5:
                    exit()
            else:
                print("INGRESE UNA OPCION VALIDA!")
        except ValueError:
            print("INGRESE UNA OPCION VALIDA!")


    

#Funcion inicial
if __name__ == "__main__":
    main()