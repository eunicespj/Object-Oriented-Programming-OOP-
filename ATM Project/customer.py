from datetime import datetime

class Customer:
   
    def __init__ (self,name,address,dateofbirth):
        self.__name = name
        self.__address = address
        self.__dateofbirth = dateofbirth #put in time format
        self.__listofaccounts = []


    def __str__(self):
        return f'Name: {self.getname()} Address: {self.getaddress()} Date of birth: {self.getdateofbirth()}'
    
    def getname(self):
        return self.__name
    
    def getaddress(self):
        return self.__address
    
    def getdateofbirth(self):
        return self.__dateofbirth
    
    def getlistofaccounts(self):
        return self.__listofaccounts
    
    def owns(self,account):
        self.__listofaccounts.append(account)
       
    
