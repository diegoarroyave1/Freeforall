from operator import truediv


class Cliientes:
    """
    clase tigo cliente
    """
    def __init__(self):
        self.nombre = "luis"
        self.apellido = "avila"
        self.__edad = 22 

    def getEdad(self):
        return self.__edad   

    def setEdad(self,nuevaEdad):
        
        if nuevaEdad > 18:  
            self.__edad = nuevaEdad
            return True 
        else:
            return False 

    def __str__(self) -> str:""     



if __name__ == "__main__":

    cliente1 = Cliientes()
    print( cliente1.getEdad())

    edad = int(input("dijite la edad del cliente"))
    if cliente1.setEdad(edad):
        print(f"la nueva edad es: {cliente1.getEdad()}")
    else:    
        print("no se puede cambiar edad")

    


