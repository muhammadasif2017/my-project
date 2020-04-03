# -*- coding: utf-8 -*-
"""
Created on Thursday 2 April 2:18:00 2020

@author: Muhamamd Asif
"""

"""
Bank Management System
"""
import secrets
import string
import sys
def Interface():
    '''
    This function defines the interface
    '''
    
    print('             ***********************')
    print('             BANK MANAGEMENT SYSTEM')
    print('             ***********************')
    print('           MAIN MENU')
    print('           1. NEW ACCOUNT')
    print('           2. DEPOSIT AMOUNT')    
    print('           3. WITHDRAW AMOUNT')
    print('           4. BALANCE ENQUIRY')
    print('           5. ALL ACCOUNT HOLDERS LIST')
    print('           6. CLOSE AN ACCOUNT')
    print('           7. MODIFY AN ACCOUNT')
    print('           8. EXIT')
    
    
def Get_Input():
    '''
    Its takes Input from user
    1-8 of his/her choice mentioned
    in interface
    '''
    
    user_input = input('Select Your Option(1-8):> ')
    while not user_input.isdigit() or (int(user_input) < 1) or (int(user_input) > 8):
        print('Invalid Choice! Select the valid one !')
        user_input =  input('Select Your Option(1-8):> ')
    user_input = int(user_input)
    return user_input


class Bank(object):
    
    pass

class Account(object):
    '''
    Class Variables:
        name: Name of Customer
        age : Age of the customer
        typeAccount: Type of Account
        balance: Amount of Customer
        accountNo: Account No of Customer
    '''
    user_dic = dict()
    def __init__(self, name ,age, typeAccount, balance, accountNo):
        '''Constructor of Account Class'''
        self.name = name
        self.age = age
        self.typeAccount = typeAccount
        self.balance = balance
        self.accountNo = accountNo
        self.user_dic[self.accountNo] = [self.name,self.age,self.typeAccount, self.balance] 
        
    def show_detail(self):
        '''
        This show the detail of current user object
        '''
        print('\n')
        print('************************')
        print('Your Account Information')
        print('************************')
        print(f'Account Hoder Account Number: {self.accountNo}')
        print(f'Account Holder Name :{self.name}')
        print(f'Account Holder Age :{self.age}')
        print(f'Account Holder Account Type :{self.typeAccount}')
        print(f'Account Holder Balance :{self.balance}')
        print('\n')
        print('')
        
    def deposit(self, money):
        '''
        The amount is add in balance
        '''
        self.balance += money
        print(f'After Deposit. your Balance is {self.balance}')
    
    def show_balance(self):
        '''
        Show the Account Balance
        '''
        print(f'Your balance is {self.balance}')
        #return self.balance
    
    def withdraw(self):
        '''
        Withdrwal amount and update the amount after every withdrwal
        '''
        money = float(input('Enter Amount for Withdrwal: >'))
        if self.balance < money:
            print('Not Ennough Funds! Your amount is {self.balance}')
        if self.balance - money >= 0:
            self.balance -= money 
            print(f'After withdrawl Your Balance is {self.balance}')
        else:
            print(f'Not Ennough Funds! Your amount is {self.balance}')
    def remove_account(self):
        '''It delete the account'''
        accountNo = input('Enter Account Number: ')
        flag = self.user_dic.pop(accountNo)
        if flag != '':
            print('Account has been Deleted!')
    def show_all_user(self):
        if not bool(self.user_dic):
            print('No Account Holder')
        else:
            print(self.user_dic)

def get_account_type():
    '''
    This function shows user the options of bank account
    type and ask him to enter his choice and return that 
    value to take_account_info() function.
    '''
    
    print('There are 3 types of Accounts')
    print('1.Current Account', end = ' ')
    print('2.Saving Account' , end = ' ')
    print('3.Commercial Account', end='\n')
    accountType = ['Current Account','Saving Account','Commercial Account']
    user_choice = input('Select Your Options (1-3):> ')
    while not user_choice.isdigit() or (int(user_choice) < 1) or (int(user_choice) > 3):
        print('Invalid Choice! Select the valid one !')
        user_choice =  input('Select Your Option(1-3):> ')
    user_choice = int(user_choice)
    return accountType[user_choice-1]

def take_account_info():
    '''
    This function is for new user. It ask for required
    information and create the account in the bank.
    '''
    global accountHolder
    user_name = input('Enter Name: ')
    user_age = int(input('Enter Age: '))
    user_account_type = get_account_type()
    user_deposit = int(input('Initial Deposit Amount: '))
    
    digits = string.digits
    accountNumber = ''.join(secrets.choice(digits) for i in range(4))
    accountHolder = Account(user_name, user_age, user_account_type, user_deposit, accountNumber)
    accountHolder.show_detail()

def main():
    Interface()
    n = Get_Input()
    
    while n!=8:
        if n == 1:
            take_account_info()
        if n == 2:
            money = int(input('Enter the Amount You want to Deposit: '))
            accountHolder.deposit(money)
        if n == 3:
            accountHolder.withdraw()
        if n == 4:
            accountHolder.show_balance()
        if n == 5:
            accountHolder.show_all_user()
        if n == 6:
            accountHolder.remove_account()
        
        if n == 8:
            sys.exit()
        Interface()
        n = Get_Input()    


main()