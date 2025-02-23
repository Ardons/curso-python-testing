import unittest, os
from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError, WithdramalTimeRestrictionError
from unittest.mock import patch


class BackAccountTests(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
        
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
            
    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())
        
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es el mismo")
        
    def test_witdraw(self):
        new_balance = self.account.witdraw(500)
        self.assertEqual(new_balance, 500, "El balance no es el mismo")
        
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es el mismo") 
        
    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"), "El archivo NO Existe") 
        
    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8    
        new_balance = self.account.witdraw(100)
        self.assertEqual(new_balance, 900)
        
    @patch("src.bank_account.datetime")
    def test_withdraw_raises_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18   
        with self.assertRaises(WithdramalTimeRestrictionError):
            new_balance = self.account.witdraw(100)