from BankFacade import BankFacade

def main():
    bank_facade = BankFacade()
    pin = input("Enter your PIN: ")

    if not bank_facade.authenticate(pin):
        print("Invalid PIN!")
        return

    print("1. Check Account Details")
    print("2. Transfer Funds")
    print("3. Send Notification")
    choice = input("Choose an option: ")

    if choice == "1":
        account_id = input("Enter account ID: ")
        bank_facade.get_account_details(account_id)
    elif choice == "2":
        from_account = input("Enter from account ID: ")
        to_account = input("Enter to account ID: ")
        amount = float(input("Enter amount to transfer: "))
        bank_facade.transfer_funds(from_account, to_account, amount)
    elif choice == "3":
        account_id = input("Enter account ID: ")
        message = input("Enter notification message: ")
        bank_facade.notification.send_notification(account_id, message)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
