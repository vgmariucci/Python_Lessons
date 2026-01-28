'''
A class representing a bank account simulation.
'''
class BankAccount:
    '''
    Creates a bank accout with basic operations like deposit, withdraw and check balance.
    '''
    def __init__(self, id, name, balance=0):
        
        self.id = id
        self.owner = name
        self.balance = balance
    
    def withdraw(self, amount):
        '''
        Withdraw a specific amount from the bank account.
        '''
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew U${amount:,.2f}. New balance is U${self.balance:,.2f}."

    def deposit(self, amount):
        '''
        Deposit a specific amount into the bank account.
        '''
        self.balance += amount
        return f"Deposited U${amount:,.2f}. New balance is U${self.balance:,.2f}."
    
    def __str__(self):
        return f"The Bank account id={self.id} of {self.owner} has U${self.balance:,.2f}."




# Instance creation and method calls
c1 = BankAccount(1, "Alice", 1000)
print('\nInitial account state:\n')
print(c1)

withdraw_amount = 250
withdraw_trials = 6

print('\nStarting withdrawals:\n')
while (withdraw_trials > 0):  
    print(c1.withdraw(withdraw_amount))
    withdraw_trials -= 1

print('\nStarting deposits:\n')
deposit_amount = 500
deposit_trials = 4

while(deposit_trials > 0):
    print(c1.deposit(deposit_amount))
    deposit_trials -= 1

print('\nFinal account state:\n')
print(c1)