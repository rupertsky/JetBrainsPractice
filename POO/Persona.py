"""class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel

    def Doblar(self, grados):
        self.direccion += grados"""

def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
            def __init__(self, Especie, Color):
                self.Edad = 0
                self.Especie = Especie
                self.Color = Color

            def CumpliAnios(self):
                self.Edad += 1
                return self.Edad
    clase = Animal(especie, color)
    return clase

a = ClaseAnimal('perro', 'blanco')
a.CumpliAnios()
a.CumpliAnios()
print(a.CumpliAnios())


