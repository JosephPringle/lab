class Account:

    def __init__(self, name)-> None:
        self.__account_name = self.name
        self.__account_balance = 0

    def deposit(self, amount)-> bool:
        if self.amount >= 0:
            self.__account_balance =+ self.amount
            return True
        else:
            return False

    def withdrawl(self, amount)-> bool:
        if self.amount >= 0 and self.__account_balance:
            self.__account_balance =- self.amount
            return True
        else:
            return False

    def get_name(self)-> str:
        return self.name

    def get_amount(self)-> float:
        return float(self.amount)

