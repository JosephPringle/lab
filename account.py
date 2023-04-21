class Account:

    def __init__(self, name:str)-> None:
        '''
        function that sets up the initial variables
        :param name: string value-account holder's name
        '''
        self.__account_name = name   # account name is equal to name
        self.__account_balance = 0   # account balance is 0

    def deposit(self, amount:str)-> bool:
        '''
        function that adds amount to the account balance
        :param amount: numeric value-how much money being deposited
        :return: True if tansaction is successful and false if not
        '''
        if amount > 0:
            self.__account_balance += amount   #sum of account balance and amount
            return True
        else:
            return False

    def withdrawl(self, amount:float)-> bool:
        '''
        function that subtracts the amount from the account balance
        :param amount: numeric value-how much money being withdrawn
        :return: True if tansaction is successful and false if not
        '''
        if amount >= 0 and amount < self.__account_balance:   #difference between balance and amount
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_name(self)-> str:
        '''
        function that gets the account holder's name
        :return: the account holder's name
        '''
        return self.__account_name

    def get_balance(self)-> float:
        '''
        function that gets the balance
        :return: the account balance
        '''
        return float(self.__account_balance)

