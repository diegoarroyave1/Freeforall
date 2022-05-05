"""Escribir un programa que pida el numero de gramos de masa de un camion(objeto)
 y usando varios metedos mostrar en pantalla las conversiones de dicha cantidad"

kilogramos
libras 
onzas
"""
class Camion:
    """
    clase tigo cliente
    """
    def __init__(self,gramos,Kilogramos,libras,onzas):
        self.gramos = gramos
        self.Kilogramos = 0
        self.libras = 0
        self.onzas = 0 

    def GaK(self):
        self.Kilogramos = self.gramos/1000

    def ka(self):
        self.Kilogramos = self.gramos/1000 

    def GaK(self):
        self.Kilogramos = self.gramos/1000             


if __name__ == "__main__":
    camion1 = Camion
    Camion.gramo = int(input("Dijiste los grampo:"))
    print(Camion.gramos)
    
