from atm_transaction import Withdrawal, Transfer
from account import Savings_Account, Current_Account,Account
import customer
#from atm_card import ATM_Card
import bank
from additional_exceptions import AccountNotFound, InvalidATMCard, InvalidAccount


class ATM :
    def __init__(self,location,managedby):
        self.location = location
        self.managedby = managedby #bank obj
        self.__currentcard = None

    def get_currentcard(self):
        return self.__currentcard
  
    def set_currentcard(self,inputcard):
        self.__currentcard = inputcard

    def transactions(self,transactiontype,amount, accounttype, transacctnum = None):      
        if transactiontype == "withdrawal":
           accobj = self.__currentcard.access(accounttype)
           trans = Withdrawal(amount)
           return trans.update(accobj,amount)
        

        if transactiontype == "transfer":#transferoption
            accobj = self.__currentcard.access(accounttype)
            if accobj.get_accountnumber()!= transacctnum:
                tranaccobj = self.managedby.get_acct(transacctnum)
                trans = Transfer(amount)
                return trans.update(accobj,amount,tranaccobj)
            
    # check if customer has one or two accounts
    def check_accts(self):
        if len(self.get_currentcard().get_ownedby().getlistofaccounts())==2:#get_ownedby()
            return True
        elif len(self.get_currentcard().get_ownedby().getlistofaccounts()) ==1:
            return False

    def check_pin(self,userpin):
        #currentCustomerObj= self.get_currentcard().get_ownedby()
        return self.managedby.authorize_pin(self.get_currentcard().get_ownedby(),userpin)#.

    def check_card(self,useratmcard):
        x = self.managedby.listofatmcards
        for i in x:
            if i.get_cardnum() == useratmcard :
                self.set_currentcard(i) 
                return True
        else:
            raise InvalidATMCard("Invalid card. Please take your card")

    def show_balance(self,Accounttype):
        acctobj =  self.__currentcard.access(Accounttype)
        return f'Your {Accounttype} account has a balance of ${acctobj.check_balance():.2f}.'

    

