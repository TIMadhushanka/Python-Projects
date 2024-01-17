class BankAccount:
    
    def __init__(self,AccName,InitialAmount):
        self.name=AccName
        self.balance=InitialAmount
        print(f'\nAccount "{self.name}" created.\nBalance = ${self.balance:.2f}.')
        
    #methods
    def getbalance(self):
        print(f'\nAccount "{self.name}" balance = ${self.balance:.2f}')
        
    def deposit(self,amount):
        self.balance+=amount
        print('\nDeposited')
        self.getbalance()
        
    def viable_transaction(self,trans):
        if self.balance>=trans:
            return
        else:
            raise Exception(f'\nSorry! Account balance of "{self.name}" is not sufficient for this transaction')
            
    def withdraw(self,withdrawal):
        try:
            self.viable_transaction(withdrawal)
            self.balance-=withdrawal
            print('Withdraw completed.')
            self.getbalance()
            
        except Exception as ex:
            print('Failed')
            print(ex)
    
    def transfer(self,amount,account):
        try:
            self.viable_transaction(amount)
            print('\nTransaction begins🚀\n*****\n')
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransaction complete✔')
            
        except Exception as ex:
            print(f'Transaction Failed❌\n{ex}')
            
            
class Interest(BankAccount):
    
    def deposit(self,amount):
        self.balance=self.balance+(amount*1.05)
        print('\nDeposited')
        self.getbalance()
        
class Saving(Interest):
    
    def __init__(self,AccName,InitialAmount):
        super().__init__(AccName,InitialAmount)
        self.fee=5
        
    def withdraw(self,withdrawal):
        try:
            self.viable_transaction(withdrawal+self.fee)
            self.balance-=withdrawal+self.fee
            print('Withdraw completed.')
            self.getbalance()
            
        except Exception as ex:
            print(f'Transaction Failed❌\n{ex}')