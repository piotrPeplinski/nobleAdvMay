class BankAccount:
    accounts = []

    def __init__(self, balance: int|float):
        """imitated a bank account

        Args:
            balance (int | float): money that user has
        """
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount:int|float)->bool:
        '''Add money to balance'''
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    @classmethod
    def audit(cls)->int|float:
        money = 0
        for account in cls.accounts:
            money += account.balance
        return money

    @staticmethod
    def curr_conv_usd(money):
        return money/4

    def __str__(self):
        return f'Bank account: {self.balance}'


class JuniorBankAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance*(self.interest_rate/100)
        return True

kazik_konto = BankAccount()
piotr_konto = BankAccount(1000)
piotrus_konto = JuniorBankAccount(10000, 10)
piotrus_konto.add_interest()
print(vars(piotrus_konto))
print(vars(BankAccount))
print(vars(JuniorBankAccount))
piotr_konto.deposit()
