from rich import print
from time import sleep

class book:
    def __init__(self, title, page):
        self.title = title
        self.tot_page = page
        self.current_page = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.title}[/] que tem [green]{self.tot_page} paginas[/] no total. Voce agora está na [yellow]pagina {self.current_page}[/][/]")

    def leaf(self, amount = 1):
        cont = 0
        for i in range(0, amount, 1):
            if not self.end_book():
                self.current_page += 1
                print(f"pag{self.current_page} :arrow_forward:", end=' ')
                sleep(0.3)
                cont += 1
        print(f"[blue]Voce agora está na[/] [yellow]pagina {self.current_page}[/]")
        if self.end_book():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.title}'[/]")

    def end_book(self) -> bool:
        if self.current_page == self.tot_page:
            return True
        else:
            return False

read = book("10 coisas que aprendi", 20)
read.leaf(5)
read.leaf(10)
read.leaf(50)
