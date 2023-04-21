from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.account1 = Account('mat')
    def teardown_method(self):
        del self.account1
    def test_deposit(self):
        assert self.account1.deposit(-2.0) is False
        assert self.account1.deposit(0) is False
        assert self.account1.deposit(2.0) is True
        assert self.account1.get_balance() == 2

    def test_withdrawl(self):
        assert self.account1.withdrawl(-2.0) is False
        assert self.account1.withdrawl(0) is False
        assert self.account1.get_balance() == 0
        assert self.account1.withdrawl(200) is False
        assert self.account1.deposit(20) is True
        assert self.account1.withdrawl(3.0) is True
        assert self.account1.get_balance() == 17