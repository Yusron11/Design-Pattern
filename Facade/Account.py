class Account:
    def __init__(self):
        self.accounts = {"12345": 5000, "67890": 3000}

    def get_account_details(self, account_id):
        if account_id in self.accounts:
            print(f"Account ID: {account_id}, Balance: {self.accounts[account_id]}")
        else:
            print(f"Account ID: {account_id} not found.")

    def check_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]
        return None
