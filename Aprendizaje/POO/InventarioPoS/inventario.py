

import articulo


def esta_Vacio(txt):
    if len(txt) <= 0:
        return True
    else: 
        return False

def add_Codigo():
    while True:
        try:
            codigo = input("Ingrese CODIGO del articulo : ")
            if esta_Vacio(codigo) == False:
                return codigo
        except:
            print()
def add_Nombre():
    while True:
        try:
            nombre = input("Ingrese el NOMBRE del producto :")
            if esta_Vacio(nombre) == False:
                return nombre
        except:
            print()
def add_PrecioUni():
    while True:
        try:
            precio_unit = input("Ingrese el PRECIO UNITARIO :")
            if esta_Vacio(precio_unit) == False:
                return float(precio_unit)
        except:
            print()
def add_PrecioPaq():
    while True:
        try:
            precio_paq = input("Ingrese el PRECIO POR PAQUETE :")
            if esta_Vacio(precio_paq) == False:
                return float(precio_paq)
        except:
            print()
def add_PiezasPaq():
    while True:
        try:
            piezas_paq = input("Ingrese el numero de PIEZAS POR PAQUETE :")
            if esta_Vacio(piezas_paq) == False:
                return int(piezas_paq)
        except: 
            print()

def agregar_Articulo():
    print("*"*80)
    print("*"*25 + " SISTEMA DE INVENTARIO UwU v1 " + "*"*25 )
    print("*"*80)
    print("")
    codigo = add_Codigo()
    nombre = add_Nombre()
    precio_unit = add_PrecioUni()
    precio_paq = add_PrecioPaq()
    piezas_paq = add_PiezasPaq()
    nuevo_articulo = articulo.articulo(codigo, nombre , precio_unit, precio_paq , piezas_paq)


def gestion_Inventario():
    while True:
        menu_inv = [1,2,3,4,5]
        print("*"*80)
        print("*"*25 + " SISTEMA DE INVENTARIO UwU v1 " + "*"*25 )
        print("*"*80)
        print("")
        print("1. Agregar articulo")
        print("2. BModificar Existencias")
        print("3. Consultar articulo")
        print("4. Eliminar articulo")
        print("5. Regresar Menu Principal")
        try:
            op = input("Seleccione la opcion correspondiente : ")
            if esta_Vacio(op)==False :
                op = int(op)
                if op in menu_inv:
                    if op == 1:
                        agregar_Articulo()
                    elif op == 2:
                        print("")
                        #modificar_Existencias()
                    elif op == 3:
                        print("")
                        #consultar_Articulo()
                    elif op == 4:
                        print("")
                        #eliminar_Articulo()
                    elif op == 5:
                        menu_Principal()
                else:
                    print("Ingrese un numero de opccion valido!!")
            else:
                print("El campo no puede quedar VACIO!!")
        except ValueError:
            print("La opccion no puede quedar el blanco y debe er un numero valido!")

def menu_Principal():
    menu_op = [1,2,3,4,5]
    while True:
        print("*"*80)
        print("*"*25 + " SISTEMA DE INVENTARIO UwU v1 " + "*"*25 )
        print("*"*80)
        print("")
        print("1. Gestion de Inventario")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. SALIR")
        try:
            op = input("Seleccione la opcion correspondiente : ")
            if esta_Vacio(op) == False:
                op =int(op)
                if op in menu_op:
                    if op == 1:
                        gestion_Inventario()
                    elif op == 2:
                        print()
                    elif op == 3:
                        print()
                    elif op == 4:
                        print()
                    elif op == 5:
                        exit()
            else:
                print("Ingrese un numero de opccion valido!!")
        except ValueError:
            print("La opccion no puede quedar el blanco y debe er un numero valido!")




def main():
    menu_Principal()


if __name__ == "__main__":
    main()