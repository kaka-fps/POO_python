class BankAccount:
    """
    Cria uma conta bancaria e permite fazer depositos
    """

    def __init__(self, id, name, balance = 0):
        self.id = id
        self.holder = name
        self.balance = balance
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.balance:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.holder} tem R${self.balance:,.2f} de saldo"

    def deposit(self, value):
        self.balance += value
        print(f"Depósito de R${value:,.2f} autorizado na conta {self.id}")

    def sake(self, value):
        if self.balance < value:
            print(f"saque de R${value:,.2f} NEGADO na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.balance -= value
            print(f"Depósito de R${value:,.2f} autorizado na conta {self.id}")


account1 = BankAccount(112, "Guntavo", 3000)
account1.deposit(500)
account1.sake(200000)
print(account1)
