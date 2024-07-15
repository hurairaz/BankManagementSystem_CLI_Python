import functions as func
from datetime import datetime


class User:
    def __init__(self, user_file):
        self.user_file = user_file
        self.user_data = func.get_data_from_file(user_file)

    def check_balance(self):
        print("Your current balance is: ", self.user_data["balance"])

    def withdraw_amount(self):
        amount = func.populate_int_data(
            1, 50000, "Please enter the amount you wish to withdraw"
        )
        if amount <= self.user_data["balance"]:
            print(f"\nTo withdraw ${amount}, please provide the following details.")
            bank_name = func.populate_string_data("Bank Name")
            password_input = func.populate_string_data("Enter your password")
            if password_input == self.user_data["password"]:
                self.user_data["balance"] -= amount
                transaction_data = {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "amount": amount,
                    "receiver_account_number": "Anonymous User",
                    "sender_account_number": self.user_data["account_number"],
                    "type": "Withdraw",
                    "bank_name": bank_name,
                }
                self.user_data["transaction_history"].append(transaction_data)
                func.set_data_in_file(
                    f"{self.user_data['account_number']}.json", self.user_data
                )
                print("Withdrawal Successful!")
                print(f"${amount} has been successfully withdrawn from your account.")
            else:
                print("Withdrawal Failed")
                print("Invalid password. Please try again.")
        else:
            print("Withdrawal Failed")
            print("Insufficient balance. Please enter a valid amount.")

    def deposit_amount(self):
        amount = func.populate_int_data(
            1, 50000, "Please enter the amount you wish to deposit"
        )
        print(f"\nTo deposit ${amount}, please provide the following details.")
        bank_name = func.populate_string_data("Bank Name")
        password_input = func.populate_string_data("Enter your password")
        if password_input == self.user_data["password"]:
            self.user_data["balance"] += amount
            transaction_data = {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "amount": amount,
                "receiver_account_number": self.user_data["account_number"],
                "sender_account_number": "Anonymous User",
                "type": "Deposit",
                "bank_name": bank_name,
            }
            self.user_data["transaction_history"].append(transaction_data)
            func.set_data_in_file(
                f"{self.user_data['account_number']}.json", self.user_data
            )
            print("Deposit Successful!")
            print(f"${amount} has been successfully deposited to your account.")
        else:
            print("Deposit Failed")
            print("Invalid password. Please try again.")

    def transfer_money(self):
        amount = func.populate_int_data(
            1, 50000, "Please enter the amount you wish to transfer"
        )
        if amount <= self.user_data["balance"]:
            print(f"\nTo transfer ${amount}, please provide the following details.")
            receiver_account_number = func.populate_string_data(
                "Receiver Account Number"
            )
            receiver_data = func.get_data_from_file(
                f"{receiver_account_number}.json", "User does not exist."
            )
            if receiver_data:
                password_input = func.populate_string_data("Enter your password")
                if password_input == self.user_data["password"]:
                    self.user_data["balance"] -= amount
                    receiver_data["balance"] += amount
                    transaction_data = {
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "amount": amount,
                        "receiver_account_number": receiver_data["account_number"],
                        "sender_account_number": self.user_data["account_number"],
                        "type": "Money Transfer",
                        "bank_name": "Swift Bank",
                    }
                    self.user_data["transaction_history"].append(transaction_data)
                    receiver_data["transaction_history"].append(transaction_data)
                    func.set_data_in_file(
                        f"{self.user_data['account_number']}.json", self.user_data
                    )
                    func.set_data_in_file(
                        f"{receiver_data['account_number']}.json", receiver_data
                    )
                    print(
                        f"${amount} has been successfully transferred to account number {receiver_data['account_number']}."
                    )
                else:
                    print("Money Transfer Failed")
                    print("Invalid password. Please try again.")
        else:
            print("Money Transfer Failed")
            print("Insufficient balance. Please enter a valid amount.")

    def change_password(self):
        print("\nTo change your password, please provide the following details.")
        current_password = func.populate_string_data("Current Password")
        if current_password == self.user_data["password"]:
            new_password = func.populate_string_data("New Password")
            self.user_data["password"] = new_password
            func.set_data_in_file(
                f"{self.user_data['account_number']}.json", self.user_data
            )
            user_record = func.get_data_from_file("user_record.json")
            if user_record:
                for user in user_record:
                    if user["account_number"] == self.user_data["account_number"]:
                        user["password"] = new_password
                        break
                func.set_data_in_file("user_record.json", user_record)
        else:
            print("Incorrect current password. Please try again.")

    def show_transaction_history(self):
        transaction_history = self.user_data["transaction_history"]
        if transaction_history:
            for transaction_record in transaction_history:
                print("*" * 30)
                print(f"Date: {transaction_record['date']}")
                print(f"Transaction Type: {transaction_record['type']}")
                print(f"Amount: ${transaction_record['amount']}")
                print(f"Sender: {transaction_record['sender_account_number']}")
                print(f"Receiver: {transaction_record['receiver_account_number']}")
                print(f"Bank: {transaction_record['bank_name']}")
                print("*" * 30)
        else:
            print("No Transaction Records Found.")

    def print_statement(self):
        print("*" * 30)
        print(f"Username: {self.user_data["username"]}")
        print(f"Account Number: {self.user_data["account_number"]}")
        print("*" * 30)
        print("")
        print("Transaction History: ")
        self.show_transaction_history()

