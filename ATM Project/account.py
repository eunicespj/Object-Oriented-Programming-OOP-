from additional_exceptions import InsufficientFunds
class Account:
    
    def __init__ (self,owner, accounttype = "savings" or "current",balance = 0, ):
        self._accounttype = accounttype
        self.__owner = owner
        self.__balance=balance


    def check_balance(self):
        return self.__balance
    
    def set_balance(self,newbalance):
        self.__balance = newbalance
        

    def get_owner(self):
        return self.__owner

    def get_accounttype(self):
        return self._accounttype
    
    def debit(self,amount):
        if self.__validate_amount(amount) == True:
            x = self.__balance - amount
            if x >= 0: #check if balance is negative amount
                self.__balance = self.__balance - amount #minus off amount
                return self.__balance              
            else: 
                raise InsufficientFunds
        
            
 
    def credit(self,amount):
        if self.__validate_amount(amount) == True:
            self.__balance = self.__balance + amount #add amount
            
           
        
    def __validate_amount(self,amount):
        amount = str(amount)
        z = amount.split(".")       
        x = float(amount)
        y = 0
        if len(z) > 1 : #check for more than two decimal places
            y = len(z[1])
        if x <= 0 or y > 2 : #check if value is negative
            raise ValueError("amount") 
        else :
            return True

        
class Savings_Account(Account):
    def __init__(self, accountnumber, owner):
        # calling Parent method
        super().__init__(accounttype = "savings",owner=owner,balance=0)
        self.__accountnumber = accountnumber
       

    def get_accountnumber(self):
        return self.__accountnumber
            
    
class Current_Account(Account):
    def __init__(self,accountnumber,owner):
        # calling Parent method
        super().__init__(accounttype = "current",owner=owner,balance=0)
        self.__accountnumber = accountnumber
        
     
    def get_accountnumber(self):
        return self.__accountnumber

    


