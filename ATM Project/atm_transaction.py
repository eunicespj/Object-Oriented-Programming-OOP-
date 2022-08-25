from abc import ABC, abstractmethod 
import datetime
from account import Account

class ATM_Transaction(ABC):
    transaction_id = 0
    def __init__(self,transactiontype,date,amount=0):
        self._transactiontype = transactiontype
        self._amount = amount
        self.date = date
        if date is None:
            self.date = datetime.now()
            self.date = self.date.strftime("%d/%m/%Y")
        ATM_Transaction.transaction_id = ATM_Transaction.transaction_id + 1

    @abstractmethod
    def update(self,Account,amount,transferaccobj=None):
            pass
      
class Withdrawal(ATM_Transaction):
    def __init__(self,amount ,date = datetime.datetime.now() , transactiontype = 'withdrawal'):
        super().__init__(transactiontype,date,amount)
        

    def withdraw(self,Account):
        return self.update(Account,self._amount)
        
        
    def update(self,Account,amount,transferaccobj=None):
        return Account.debit(amount)
         
        
class Transfer(ATM_Transaction):

    def __init__(self,amount ,date = datetime.datetime.now() , transactiontype = 'transfer'):
        super().__init__(transactiontype,date,amount)

    def update(self,Account, amount,transferaccobj):
        Account.debit(amount)        
        return transferaccobj.credit(amount)
