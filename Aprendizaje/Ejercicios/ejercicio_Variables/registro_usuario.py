"*******************************************************************"
"               Ejercicio Integrador de Conversiones                "
"                                                                   "
"               Practica de conversion de valores                   "
"*******************************************************************"
#Inicializacion de variables globales
usu_nombre = ""
usu_apellido = ""
usu_edad = 0
usu_carrera = ""
usu_altura = 0.0
usu_peso = 0.0
usu_esCasado = False

usuario_registro = {"nombre" : "", "apellido": "", "edad" : 0 , "carrera" : "", "altura" : 0 , 
                    "peso" : 0 , "casado?" : False }

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
        print("ALTURA INVALIDA   --FUERA DE RANGO (1.10 - 2.50)")
        return False
#Funcion de comprobacion de Pesos Validos
def comp_Peso(pe):
    pe = float(pe)
    if 39 < pe < 269:
        return True
    elif pe < 0:
        print("EL PESO NO PUEDE SER UN VALOR NEGATIVO!!")
    else:
        print("PESO INVALIDO   --FUERA DE RANGO (39 - 269)")
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
                return var
            
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
                return var
        except ValueError:
            print("Ingrese un dato valido!!")
        
def peticionPeso():
    while True: 
        try:
            var = input("Ingrese su Peso : ").strip()
            if comp_Vacio(var) == False and comp_Peso(var) == True:
                return var
            
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
#Funcion Principal de recoleccion de datos e impresion del registro
def main():
    global usu_nombre
    global usu_apellido 
    global usu_edad
    global usu_carrera
    global usu_altura 
    global usu_peso 
    global usu_esCasado
    global usuario_registro

    print("\nIngrese los datos del Usuario a Registrar, por favor!! \n")

    usu_nombre = peticionNombre()
    usu_apellido = peticionApelllido()
    usu_edad = peticionEdad()
    usu_carrera = peticionCarrera()
    usu_altura = peticionAltura()
    usu_peso = peticionPeso()
    usu_esCasado = peticionEstadoCivil()

    usuario_registro = {"nombre" : usu_nombre, "apellido": usu_apellido, "edad" : usu_edad , "carrera" : usu_carrera, "altura" : usu_altura , 
                    "peso" : usu_peso , "casado?" : usu_esCasado }
    
    print(f"DATOS DEL USUARIO REGISTRADO \nNombre : {usuario_registro['nombre']} \nApelido : {usuario_registro['apellido']}" +
           f"\nEdad : {usuario_registro["edad"]} \nCarrera : {usuario_registro["carrera"]}\nAltura : {usuario_registro["altura"]}"+
           f"\nPeso : {usuario_registro["peso"]} \nCasado : " + ("Si" if usu_esCasado == True else "NO" ))

#Funcion inicial
if __name__ == "__main__":
    main()