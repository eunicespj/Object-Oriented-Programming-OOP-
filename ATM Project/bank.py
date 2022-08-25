import random
import atm_card 
from  additional_exceptions import AccountNotFound, InvalidPinNumber
from account import Savings_Account, Current_Account, Account
from atm_transaction import Transfer
from customer import Customer

class Bank :
    
    def __init__(self,code,address):
        self.__code = code
        self.__address = address
        self.listofatm = []
        self.listofcustomers = []
        self.listofatmcards = []
        
        
   #generate list of customers
    def add_customer(self, customer_object, pin):
        name_id = customer_object.getname() + str(random.randint(1000, 9999))
        self.list_of_cust = {}
        self.list_of_cust['customer_id'] = name_id
        self.list_of_cust['cust_detail'] = customer_object
        self.list_of_cust['cust_pin'] = pin
        self.listofcustomers.append(self.list_of_cust)
     
    def manages(self,ATM_Card):
        self.listofatmcards.append(ATM_Card)
     
        
    def maintains(self,ATM):
        self.listofatm.append(ATM)
    
    #check if customer input pin is correct
    def authorize_pin(self,customerobj,inputpinnum): 
        for customer in self.listofcustomers:
            if customer['cust_pin'] == inputpinnum and customer['cust_detail'] == customerobj:
                return True
        raise InvalidPinNumber
            

    def get_acct(self,inputacc):
        for customer in self.listofcustomers:
            for acctobj in customer['cust_detail'].getlistofaccounts():
                if inputacc == acctobj.get_accountnumber():
                    return acctobj
        raise AccountNotFound
     
        


