class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')
        
    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New Balance: {self.balance}")
        
        return self.balance

    def witdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"withdrew {amount}. New Balance: {self.balance}")
        return self.balance
    
    def get_balance(self):
        print(f"el balance es: {self.balance}")
        self._log_transaction(f"Checked balance. Current balance: {self.balance}")
        return self.balance