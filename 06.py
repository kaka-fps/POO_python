from rich import print
from rich.panel import Panel

class barbecue:

    comsumption:float = 0.400
    price:float = 82.40

    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def __str__(self):
        return f"Esse é {self.title} com {self.amount} pessoas participando"
    
    def totalQuantity(self) -> float:
        return self.amount * barbecue.comsumption

    def totalCost(self) -> float:
        return self.totalQuantity() * barbecue.price

    def individualCost(self) -> float:
        return self.totalCost() / self.amount


    def analysis (self):
        content = f"Analisando [blue]{self.title}[/] com [green]{self.amount} convidados[/]"
        content += f"\nCada participante comerá {barbecue.comsumption} Kg e cada Kg custa R${barbecue.price:,.2f}"
        content += f"\nRecomendo [green]comprar {self.totalQuantity():.3f}[/]Kg de carne "
        content += f"\nOcusto total será de [blue]R${self.totalCost():.2f}[/]"
        content += f"\nCada pessoa pagará [yellow]R${self.individualCost():.2f}[/] para participar."
        analys = Panel(content,title=self.title)
        print(analys)
        
group1 = barbecue("churras dos cria",15)
group1.analysis()

group2 = barbecue("festa do fim de ano",80)
group2.analysis()

