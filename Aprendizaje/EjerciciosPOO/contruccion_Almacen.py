
import os
import json
import re

from construccion_Articulo import C_Articulo
reg_almacen = "Registro_Almacen.json"
lista_articulos = []

class Almacen:

    lista_articulos = []

    def __init__(self):
        print("Iniciando Almacen!")

    
    def cargar_Almacen(self):
        if os.path.exists(reg_almacen):
            with open(reg_almacen, "r") as archivo:
                return json.load(archivo)

    def guardar_Almacen(self):
        with open(reg_almacen, "w") as archivo:
            json.dump(lista_articulos, archivo)

    def guardar_Articulo(self, nuevo_articulo):
        print(lista_articulos)
        lista_articulos.append(nuevo_articulo)
        print(lista_articulos)

    def obj_a_Dic(self , articulo):
        dicc = {"codigo" : articulo.codigo, "precio" : articulo.precio, "existencias" : articulo.existencias}
        return dicc
    def dic_a_Obj(self , articulo):
        obj_articulo = C_Articulo(articulo["codigo"], articulo["precio"], articulo["existencias"])
        return obj_articulo
