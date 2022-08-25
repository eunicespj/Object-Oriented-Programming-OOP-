
from additional_exceptions import AccountNotFound

class ATM_Card:
    def __init__ (self,cardnum,owned_by):
        self.__cardnum = cardnum
        self.__ownedby = owned_by #custobj

    def __str__(self):
        return f'Card Number: {self.get_cardnum()} Customer : {self.get_ownedby()}'

    def get_acct_types(self):
        acctobjlist = self.__ownedby.getlistofaccounts()
        getacctype = []
        for i in acctobjlist:
            getacctype.append(i.get_accounttype())
        return getacctype

    def access(self,accounttype):
        status = False
        for x in self.__ownedby.getlistofaccounts():
            if x.get_accounttype()==accounttype:
               status = True 
               return x
        if status == False:
            raise AccountNotFound
       
       
    def get_cardnum(self):
        return self.__cardnum

    def get_ownedby(self):
        return self.__ownedby

 
      
            
        
