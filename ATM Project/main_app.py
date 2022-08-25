from account import *
from atm import ATM
from atm_transaction import ATM_Transaction, Withdrawal, Transfer
from bank import Bank # from bank.py import Bank class
from additional_exceptions import AccountNotFound, InsufficientFunds, InvalidATMCard, InvalidAccount

def atm_app(ATM_card):
    while True: 
        print("Avaliable options:")
        print("1. Insert ATM card")
        print("2. Quit Simulation")
        option = int(input("Enter an option:"))
        if option == 1 :
            cardnum = input("Enter a ATM card number ")
            x = ATM_card.check_card(cardnum) #check card number if valid
            if x == True:
                intpin = input("Enter a pin number:")
                atm_app.pin = intpin
                y = ATM_card.check_pin(intpin) #check if input pin is valid
                if y == True:
                    atm_menu_sys(ATM_card) #if both valid, proceed to atm menu
        elif option == 2 :
            print("Quit Simulation.")
            break

def atm_menu_sys(ATM_card):
    while True:
        print("Avaliable options:")
        print("1. Check balance")
        print("2. Withdraw Funds")
        print("3. Transfer Funds")
        print("4. Return Card")
        option = int(input("Enter a transaction option:"))
        if option == 1:
            if ATM_card.check_accts() == True:
                print("Choose Account")
                print("1.Current Account")
                print("2.Savings Account")
                choice = int(input("Enter an account option:"))
                if choice == 1 :
                    print(ATM_card.show_balance('current')) #display account balance
                elif choice == 2 :
                    print(ATM_card.show_balance('savings'))
                else:
                    print("Invalid option selected")
            elif ATM_card.check_accts() == False:
                print(ATM_card.show_balance('savings'))
                break
        elif option == 2:
            temp2 = 'withdrawal'
            try:
                if ATM_card.check_accts() == True:
                    print("Choose Account")
                    print("1.Current Account")
                    print("2.Savings Account")
                    choice = int(input("Enter an account option:"))
                    withdrawalamount = float(input("Enter an amount to withdraw"))
                    if choice == 1 :
                        temp5='current'
                    elif choice == 2 :
                        temp5='savings'
                    else:
                        print("Invalid option selected")
                
                    ATM_card.transactions(temp2,withdrawalamount,temp5) #withdraw amount
                    
                    print("Card Returned")
                    print(ATM_card.show_balance(temp5)) #display balance after withdraw amount
                    break 
            
                elif ATM_card.check_accts() == False: # if only one account , default is savings account
                    withdrawalamount = float(input("Enter an amount to withdraw"))
                    temp5='savings'
                    ATM_card.transactions(temp2,withdrawalamount,temp5) #withdraw amount
                    print("Card Returned")
                    print(ATM_card.show_balance(temp5)) #display balance after withdraw amount
                    break 
            except InvalidAccount:
                print("Invalid Account")
        elif option == 3:
            temp4 = 'transfer'
            if ATM_card.check_accts() == True:
                print("Choose Account")
                print("1.Current Account")
                print("2.Savings Account")
                choice = int(input("Enter an account option:"))
                if choice == 1 :
                    temp5='current'
                elif choice == 2 :
                    temp5='savings'
                else:
                    print("Invalid option selected")
                choice2 = input("Enter the account number to transfer funds to : ")
                choice3 = float(input("Enter the amount to transfer : "))
                ATM_card.transactions(temp4,choice3,temp5,choice2) #transfer amount if account number is valid
                print("Card Returned")
                print(ATM_card.show_balance(temp5)) #show balance after transfer
                break
            elif ATM_card.check_accts() == False:
                temp5='savings'
                choice2 = input("Enter the account number to transfer funds to : ")
                choice3 = float(input("Enter the amount to transfer : "))
                ATM_card.transactions(temp4,choice3,temp5,choice2) #transfer amount if account number is valid
                print("Card Returned")
                print(ATM_card.show_balance(temp5)) #show balance after transfer
                break          
        elif option == 4:
            print("Card returned")
            break
        
        else:
            print("Wrong Input")
            break
            



            
            








                                         

