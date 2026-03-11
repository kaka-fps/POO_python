# declaração de Classe
class gafanhoto:
    def __init__(self): # Metodo Construtor
        #atributos de instância
        self.nome = ''
        self.idade = 0

# Metodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

#eclaração de objetos
g1 = gafanhoto()
g1.nome = 'mario'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = gafanhoto()
g2.nome = 'mariana'
g2.idade = 53
print(g2.mensagem())

g3 = gafanhoto()
print(g3.mensagem())
