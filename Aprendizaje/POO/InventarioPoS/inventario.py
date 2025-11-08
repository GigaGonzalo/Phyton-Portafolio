

from articulo import Articulo
from almacen import Almacen

class SistemaInventario:

    def __init__(self):
        obj_almacen = Almacen()

    def agregar_Articulo(self) -> object:
        
        print("*"*80)
        print("*"*25 + " SISTEMA DE INVENTARIO UwU v1 " + "*"*25 )
        print("*"*80)
        print("")



    """ef gestion_Inventario(self):
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
                if esta_Vacio(self, op)==False :
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
                            menu_Principal(self)
                    else:
                        print("Ingrese un numero de opccion valido!!")
                else:
                    print("El campo no puede quedar VACIO!!")
            except ValueError:
                print("La opccion no puede quedar el blanco y debe er un numero valido!")

    def menu_Principal(self):
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
                if esta_Vacio(self ,op) == False:
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

    def esta_Vacio( self, txt: str) -> bool:
    if len(txt) <= 0:
        return True
    else: 
        return False



    def main(self):
        menu_Principal(self)


    if __name__ == "__main__":
        main(self)"""