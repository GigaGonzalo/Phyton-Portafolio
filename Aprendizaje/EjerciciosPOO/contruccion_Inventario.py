
from typing import Any
from construccion_Articulo import C_Articulo
from contruccion_Almacen import Almacen
class SistemaInventario:

    def __init__(self):
        print("Sistema iniciado")

    def add_articulo(self : Any):
        obj_Almacen = Almacen()
        codigo = input("Ingrese el codigo del articulo :")
        nombre = input("Ingrese el precio del articulo :")
        existencias = input("Ingrese las existencias :")
        nuevo_articulo = C_Articulo(codigo, nombre, existencias)
        nuevo_articulo = obj_Almacen.obj_a_Dic(nuevo_articulo)
        obj_Almacen.guardar_Articulo(nuevo_articulo)
        obj_Almacen.guardar_Almacen()

    add_articulo("")

