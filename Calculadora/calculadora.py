class Calculadora:

    def __init__(self, x=0, y=0): #Construtor
        self.x = x #self é basicamente o this de java
        self.y = y

    def __repr__(self): # ToString
        return "Classe calculadora"

    @property
    def get_valox_x(self):
        return self.x

    @get_valox_x.setter
    def set_valor_x(self, x):
        self.x=x

    def somar(self):
        return self.x+self.y

    def subtrair(self):
        return self.x-self.y

    def multiplicar(self):
        return self.x*self.y

    def dividir(self):
        return self.x/self.y

