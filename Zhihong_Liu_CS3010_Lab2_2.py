from Account import Account, CurrentAccount, SavingAccount, InvestmentAccount
import copy as copy


class Bank(object):

    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def load_accounts(self, infile):
        input = open(infile)
        for line in input:
            values = line.split()
            acc_num = int(values[0])            # convert from str to int
            name = values[1]                    # no conversion required
            balance = int(values[2])            # convert from str to int
            acc_type=int(values[0][2])
            if(acc_type==1):
                self.accounts.append(  CurrentAccount(acc_num, name, balance) )
            elif(acc_type==2):
                self.accounts.append(  SavingAccount(acc_num, name, balance)   )
            elif(acc_type==3):
                self.accounts.append(  InvestmentAccount(acc_num, name, balance) )
        input.close()

    def print_accounts(self):
        print('###################################')      
        print('List of all accounts in', self.name)
        print('###################################')      
        for account in self.accounts:
            print(account)
        print()      
        
    def print_overdrwan_accounts(self):
        print('###################################')      
        print('List of overdrawn accounts in', self.name)
        print('###################################')      
        for account in self.accounts:
            if account.get_balance() < 0:
                print(account)
        print()     
        
    def get_account(self, acc_num):
        for account in self.accounts:
            if account.get_account_number() == acc_num:
                return account
        return None
    

bank = Bank('My Bank')
bank.load_accounts('accounts.txt')
bank.get_account(111).set_overdraft_limit(2500)

a = bank.get_account(113)
a.set_interest_rate(8)

bank.print_accounts()

a.withdraw(500)
bank.get_account(111).withdraw(3000)

#bank.print_overdrwan_accounts()



