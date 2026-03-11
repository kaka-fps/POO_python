from rich import print
from rich.panel import Panel

class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} custa  R${self.price:,.2f}"

    def tag(self):
        content = f"{self.name:^30}"
        content += f"{'-' * 30}"
        pricef = f"R${self.price:,.2f}"
        content += f"{pricef.center(30, '.')}"
        tag = Panel(content,title = "Produto", width=34)
        print(tag)

item1 = product("iPhone 17 Pro Max", 25000.85)
item2 = product("Notebook Gamer", 8000)

item1.tag()
item2.tag()
