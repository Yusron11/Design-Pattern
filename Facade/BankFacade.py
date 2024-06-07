from Account import Account
from Transaction import Transaction
from Notification import Notification

class BankFacade:
    def __init__(self):
        self.account = Account()
        self.transaction = Transaction()
        self.notification = Notification()
        self.pin = "1234"

    def authenticate(self, input_pin):
        return self.pin == input_pin

    def transfer_funds(self, from_account, to_account, amount):
        if self.account.check_balance(from_account) is not None and self.account.check_balance(to_account) is not None:
            self.transaction.make_transaction(from_account, to_account, amount)
            self.notification.send_notification(from_account, f"Amount {amount} transferred to {to_account}")
            self.notification.send_notification(to_account, f"Amount {amount} received from {from_account}")
        else:
            print("Invalid account ID(s).")

    def get_account_details(self, account_id):
        self.account.get_account_details(account_id)
