class BankAccount:
    def __init__(self):
        self.account_number = 0
        self.customer_name = ""
        self.balance = 0

    def accept_details(self):
        self.account_number = int(input("Enter Account Number :"))
        self.customer_name = input("Enter Customer Name :")
        self.balance = int(input("Enter Initial Balance : "))

    def deposit(self,amount):
        self.balance += amount
        print("Deposit Successful.")
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")
        
    def display_balance(self):
        print("-----Account Details-----")
        print("Account Number :",self.account_number)
        print("Customer Name :",self.customer_name)
        print("Current Balance :",self.balance)

account1 = BankAccount()

account1.accept_details()
# Deposit Operation
deposit_amount = int(input("Enter Deposit Amount : "))
account1.deposit(deposit_amount)

# Withdrawal operation
withdraw_amount = int(input("Enter Withdrawal Amount : "))
account1.withdraw(withdraw_amount)

# Display account details
account1.display_balance()
