# declaração de Classe
class gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    para criar uma nova pessoa, use 
    variavel = gafanhoto(nome, idade)
    """
    def __init__(self, name = "", age = 0): # Metodo Construtor
        #atributos de instância
        self.nome = name
        self.idade = age

# Metodos de instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

#eclaração de objetos
g1 = gafanhoto('Mario', 17)
g1.aniversario()
print(g1)
print(g1.__dict__)# Attribute
print(g1.__getstate__())# Method
print(g1.__class__)

g2 = gafanhoto('Mariana', 53)
print(g2)
print(g2.__getstate__())

g3 = gafanhoto()
print(g3)

print(g1.__doc__) #Dunder Attribute
