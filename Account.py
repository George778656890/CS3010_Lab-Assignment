class Account(object):

    def __init__(self, number, name, balance=0):
        self.account_number = number
        self.account_holder = name
        self.balance = balance
        self.overdraft_limit = 1000
        
    def set_holder(self, holder):
        self.account_holder = holder
    
    def set_account_number(self, account_numebr):
        self.account_number = account_numebr

    def set_balance(self, balance):
        self.balance = balance        

    def get_holder(self):
        return self.account_holder
        
    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def display(self):
        print('Account number:', self.account_number)
        print('Account holder:', self.account_holder)
        print('Balance:', self.balance)
        print('='*50)

    def __str__(self):
        s = 'Account number: %s\n' % self.account_number
        s += 'Account holder: %s\n' % self.account_holder
        s += 'Balance: %.2f\n' % self.balance
        s += '='*30
        return s

    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if(self.balance + self.overdraft_limit < amount):
            print('Balance is not enough to withdraw £{}'.format(amount))
        else:
            self.balance -= amount
    



class CurrentAccount(Account):
    
    def __init__(self, number, name, balance=0,overdraft_limit=0):
         super().__init__(number, name, balance)
         self.overdraft_limit=overdraft_limit
         
    def set_overdraft_limit(self,limit):
        self.overdraft_limit=limit
        
    def get_overdraft_limit(self):
        return self.overdraft_limit
        
    def display(self):
        print('Account number:', self.account_number)
        print('Account holder:', self.account_holder)
        print('Account Type : Current')
        print('Balance:', self.balance)
        print('Overdraft Limit: ',self.overdraft_limit)
        print('='*50) 
        
    def __str__(self):
        s = 'Account number: %s\n' % self.account_number
        s += 'Account holder: %s\n' % self.account_holder
        s += 'Account Type : Current\n'
        s += 'Balance: %.2f\n' % self.balance
        s += 'Overdraft Limit:%.2f\n' % self.overdraft_limit
        s += '='*30
        return s
          

class SavingAccount(Account):
    def __init__(self, number, name, balance=0,interest_rate=5):
        super().__init__(number, name, balance)
        self.interest_rate=interest_rate
        
    def set_interest_rate(self,rate):
        self.interest_rate=rate
        
    def get_interest_rate(self):
        return self.interest_rate
        
    
    def display(self):
        print('Account number:', self.account_number)
        print('Account holder:', self.account_holder)
        print('Account Type : Saving')
        print('Balance:', self.balance)
        print('Interest Rate : ',self.interest_rate)
        print('='*50)
        
    def __str__(self):
        s = 'Account number: %s\n' % self.account_number
        s += 'Account holder: %s\n' % self.account_holder
        s += 'Account Type : Saving\n'
        s += 'Balance: %.2f\n' % self.balance
        s += 'Interest Rate :%.2f\n' % self.interest_rate
        s += '='*30
        return s


class InvestmentAccount(Account):
    def __init__(self, number, name, balance=0,interest_rate=-1,transaction_limit=5,transaction_done=0):
        super().__init__(number, name, balance)
        self.interest_rate=interest_rate
        self.transaction_limit=transaction_limit
        self.transaction_done=transaction_done
    
    def set_interest_rate(self,rate):
        self.interest_rate=rate
        
    def get_interest_rate(self):
        return self.interest_rate
        
    def set_transaction_limit(self,limit):
        self.transaction_limit=limit
    
    def get_transaction_limit(self):
        return self.transaction_limit
        
    def display(self):
        print('Account number:', self.account_number)
        print('Account holder:', self.account_holder)
        print('Account Type : Investment')
        print('Balance:', self.balance)
        print('Interest Rate : ',self.interest_rate)
        print('Transcation done : ',self.transaction_done,' of ',self.transaction_limit)
        print('='*50)   
  
    def __str__(self):
        s = 'Account number: %s\n' % self.account_number
        s += 'Account holder: %s\n' % self.account_holder
        s += 'Account Type : Investment\n'
        s += 'Balance: %.2f\n' % self.balance
        s += 'Interest Rate :%.1f\n' % self.interest_rate
        s += 'Transactions done: %d of %d\n' % (self.transaction_done, self.transaction_limit)
        s += '='*30
        return s   
    
    



    #account22=InvestmentAccount('111','Tom')
    #account22.set_overdraft_limit(500)
    #account22.display()





'''   
    # main program
    
    account1 = Account()
    account1.set_account_number('111')
    account1.set_holder('Jack')
    account1.set_balance(2500)
    account1.print()
    
    account2 = Account()
    account2.set_account_number('112')
    account2.set_holder('Rose')
    account2.set_balance(1200)
    account2.print()
    '''
    
 
