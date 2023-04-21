from pytest import *
from account import *

class Test:

    def setup_method(self):

        self.account1 = Account('mat')  #name is mat
    def teardown_method(self):
        del self.account1
    def test_deposit(self):
        assert self.account1.deposit(-2.0) is False   #returns false when depositting -2.0
        assert self.account1.deposit(0) is False   #returns false when depositting 0
        assert self.account1.deposit(2.0) is True   #returns true when depositting 2.0
        assert self.account1.get_balance() == 2   #makes sure the balance is 2

    def test_withdrawl(self):
        assert self.account1.withdrawl(-2.0) is False   #returns false when withdrawling -2.0
        assert self.account1.withdrawl(0) is False   #returns false when withdrawling 0
        assert self.account1.get_balance() == 0   #makes sure the balance is 0
        assert self.account1.withdrawl(200) is False   #returns false when withdrawling 200
        assert self.account1.deposit(20) is True   #returns true when depositting 20
        assert self.account1.withdrawl(3.0) is True   #returns true when withdrawling 3.0
        assert self.account1.get_balance() == 17   #makes sure the balance is 17