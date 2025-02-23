import pytest
from src.bank_account import BankAccount


def test_sum():
    a = 4
    b = 4
    assert a + b == 8

@pytest.mark.parametrize("ammount, expected", [
    (100, 1100),
    (100, 1100),
    (100, 1100)    
])

def test_desposit_varios_ammpunts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transaction_log.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected