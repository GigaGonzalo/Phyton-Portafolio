"""


            Clase Articulo



"""

departamento = 0

class Articulo: 

    def __init__(self, codigo : str, nombre : str, unit_precio : float, paq_precio : float, num_art_paq : int):
        self.codigo = codigo
        self.nombre = nombre
        self.unit_precio = unit_precio
        self.paq_precio = paq_precio
        self.num_art_paq = num_art_paq

        print(f"Articulo agregao con Codigo {self.codigo} , nombre {self.nombre} , precio unitario {self.unit_precio} " + 
            f", precio paquete {self.paq_precio} y numero de articulos por paquete {self.num_art_paq}")
    
    """def add_Codigo(self):
        while True:
            try:
                codigo = input("Ingrese CODIGO del articulo : ")
                if esta_Vacio(self ,codigo) == False:
                    return codigo
            except:
                print()

    def add_Nombre(self ):
        while True:
            try:
                nombre = input("Ingrese el NOMBRE del producto :")
                if esta_Vacio(nombre) == False:
                    return nombre
            except:
                print()

    def add_PrecioUni(self) :
        while True:
            try:
                precio_unit = input("Ingrese el PRECIO UNITARIO :")
                if esta_Vacio(precio_unit) == False:
                    return float(precio_unit)
            except:
                print()

    def add_PrecioPaq(self):
        while True:
            try:
                precio_paq = input("Ingrese el PRECIO POR PAQUETE :")
                if esta_Vacio(precio_paq) == False:
                    return float(precio_paq)
            except:
                print()

    def add_PiezasPaq(self):
        while True:
            try:
                piezas_paq = input("Ingrese el numero de PIEZAS POR PAQUETE :")
                if esta_Vacio(self , piezas_paq) == False:
                    return int(piezas_paq)
            except: 
                print() 

    
    def esta_Vacio(self , txt: str) -> bool:
        if len(txt) <= 0:
            return True
        else: 
            return False"""
