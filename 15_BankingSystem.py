#create a banking system which can do the account creation, deposit, payment
#create account should return true if account is created, if account already persisit it shoule return false
#deposit should return true if deposit is successful, if account is not found it should return false and it should return the amount
#payment should return true if payment is successful, if account is not found it should return false and

class BankingSystem:
    def __init__(self):
        self.accounts = {}
    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            print("Account already exist")
            return False
        else:
            self.accounts[account_id] = {"timestamp": timestamp, "balance": 0}
            return True
    def deposit(self, timestamp: int, account_id: str, amount: int) ->int | bool:
        if account_id not in self.accounts:
            print("Account not found")
            return False
        else:
            self.accounts[account_id]["balance"] += amount
            return self.accounts[account_id]["balance"]
    def payment(self, timestamp: int,account_id:str, amount:int)->int | bool:
        if account_id not in self.accounts:
            print("Account id is not present")
            return False
        elif self.accounts[account_id]["balance"] < amount:
            print("No enough balance")
            return False
        else:
            self.accounts[account_id]["balance"] -= amount
            return self.accounts[account_id]["balance"]
        
    def print_accounts(self):
        if not self.accounts:
            print("No accounts")
            return
        else:
            for account in self.accounts:
                print(f"Account ID: {account}, Balance: {self.accounts[account]['balance']}")

#test the banking system
banking_system = BankingSystem()
if banking_system.create_account(1,"acc1"):
    print(f"acc1 created successfully")
else:
    print(f"acc1 already exists")
assert banking_system.deposit(2,"acc1",100)==100, "deposit assertion failure"
assert banking_system.deposit(3,"acc1",100)==200, "deposit assertion failure"
assert banking_system.payment(4,"acc1", 50)==150, "balance is not correct"
assert banking_system.deposit(5,"acc1", 1000)==1150, "balance is not correct"
assert banking_system.create_account(6,"acc1")==False, "It is allowing to create new account number with existing acc no"
assert banking_system.deposit(7,"acc2", 1500)==False, "It is allowing to deposit to non existing account number"
assert banking_system.payment(8,"acc2", 50)==False, "It is allowing to withdraw from non existing account number"
banking_system.print_accounts()