#create bank account class
class BankAccount():
    def __init__(self,accn,name,balance):
        self.accountNo = accn
        self.ownername = name
        self._balance = balance
        # print(self.accountNo,self.ownername)

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self._balance:.2f}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance for withdrawal.")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")

    def get_balance(self):
        return self._balance

# create checkingaccount class
class CheckingAccount(BankAccount):#inherit bank account class
    tf = 5 #transaction fee

    def withdraw(self, amount):
        total_amount = amount + self.tf
        if total_amount > self._balance:
            print("Insufficient balance to cover withdrawal and transaction fee.")
            return
        self._balance -= total_amount
        print(f"Withdrew {amount:.2f} (Fee: {self.tf:.2f}). New balance: {self._balance:.2f}")

# create savingsaccount class
class SavingsAccount(BankAccount): #inherit bank account class
    min_bal = 500 #minimum balance
    interest_rate = 0.03   #interest rate

    def withdraw(self, amount):
        if self._balance - amount < self.min_bal:
            print("Withdrawal cross minimum balance requirement.")
            return
        super().withdraw(amount)

    def deposit(self,amount): #override deposit class
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._balance += amount
        print(f"Interest of {interest:.2f} applied. New balance: {self._balance:.2f}")

# create BusinessAccount class
class BusinessAccount(BankAccount):#inherit bank account class
    tf = 15.00 #transaction fee
    tl = 10000  # maximum amount per transaction
    def deposit(self, amount): #override deposit class
        if amount > self.tl:
            print(f"You cross the transaction limit.")
        else:
            return super().deposit(amount)
    def withdraw(self, amount): #override withdraw class
        if amount > self.tl:
            print(f"Transaction exceeds the limit of {self.tl:.2f}.")
            return
        total_amount = amount + self.tf
        if total_amount > self._balance:
            print("Insufficient balance to cover withdrawal and transaction fee.")
            return
        self._balance -= total_amount
        print(f"Withdrew {amount:.2f} (Fee: {self.tf:.2f}). New balance: {self._balance:.2f}")


if __name__ == "__main__":
    # Creating accounts
    # ac1 = int(input("Enter Account No.: "))
    # ac1_name = input("Enter Name: ")
    # ac1_bal = int(input("Enter balance: "))
    checking = CheckingAccount(101, "Anup", 1000)
    savings = SavingsAccount(102, "Abhishek", 1500)
    business = BusinessAccount(103, "Abdullah", 5000)

    # CheckingAccount operations
    checking.deposit(200)
    checking.withdraw(300)
    checking.withdraw(1200)

    # # SavingsAccount operations
    savings.deposit(500)
    savings.withdraw(1200)
   

    # # BusinessAccount operations
    business.deposit(5000)
    business.deposit(15000)
    business.withdraw(15000)
    business.withdraw(5000)
