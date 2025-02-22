import unittest
from test_bank_account import BackAccountTests


def back_account_suite():
    #Crea una suite
    suite = unittest.TestSuite()
    #agrega una prueba en la suite
    suite.addTest(BackAccountTests("test_deposit"))
    suite.addTest(BackAccountTests("test_witdraw"))
    
if __name__ == "__main__":
    #se crea el runner que va a correr las pruebas
    runner = unittest.TextTestRunner()
    runner.run(back_account_suite())
    