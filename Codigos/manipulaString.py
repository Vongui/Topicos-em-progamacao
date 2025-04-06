class ManipulaString:

    def __init__(self, string=""):
        self.string = string

    def inverter(self):
        reverso = ''.join(reversed(self.string))
        return reverso

    # def inverter(self):
    #     return self.string[::-1]

    def primeira_palavra(self):
        #return self.string[1:' ']
        return self.string.split()[0]

    def maisculo(self):
        return self.string.upper()

    def minusculo(self):
        return self.string.lower()

    def atribuir(self, string2):
        self.string = string2

m = ManipulaString("Teste test")
print(m.inverter())
print(m.primeira_palavra())
print(m.maisculo())
print(m.minusculo())
print(m.atribuir("final"))
print(m.string)