"""


            Clase Articulo



"""

departamento = 0

class articulo: 

    def __init__(self, codigo : str, nombre : str, unit_precio : float, paq_precio : float, num_art_paq : int):
        self.codigo = codigo
        self.nombre = nombre
        self.unit_precio = unit_precio
        self.paq_precio = paq_precio
        self.num_art_paq = num_art_paq

        print(f"Articulo agregao con Codigo {self.codigo} , nombre {self.nombre} , precio unitario {self.unit_precio} " + 
            f", precio paquete {self.paq_precio} y numero de articulos por paquete {self.num_art_paq}")