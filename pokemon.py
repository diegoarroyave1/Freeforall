class Cliientes:
    """
    clase tigo cliente
    """
    def __init__(self, nombre, apellido, edad:int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self) -> str:
        return f"Hola soy {self.nombre} y tengo {self.edad} años"    

if __name__ == "__main__":

    n = input("Dijiste su nombre:")
    a = input("Dijiste su apellido:")
    e = int(input("Dijiste su edad:"))
    cliente1 = Cliientes(n,a,e)
    print(cliente1)
    print(cliente1.edad * 2)

    cliente1.edad = cliente1.edad * 2

    print(cliente1.edad)

    print(f"edad: {cliente1.edad}")

    del cliente1.edad


