from rich import print
class employee:

    enterprise = "Curso em Vídeo"

    def __init__(self, name, sector, function):
        self.name = name
        self.sector = sector
        self.function = function

    def presentation(self):
        print(f":people_holding_hands: Olá sou [blue]{self.name}[/] e sou [gold1]{self.function}[/] do setor de [green]{self.sector}[/] da empresa {employee.enterprise}")
    
people1 = employee("Maria", "Administração", "Diretora")
people1.presentation()

people2 = employee("Pedro", "TI", "Programador")
people2.presentation()
