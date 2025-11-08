class C_Articulo:

    tienda = "La tienda de la esquina"

    #Constructor
    def __init__(self, codigo , precio, existencias):
        self.codigo = codigo
        self.precio = precio
        self.existencias = existencias
        print(f"El articulo con codigo {self.codigo} cuesta ${self.precio} y hay en existencia {self.existencias}")

    