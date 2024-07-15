import os
import functions as func
from user import User


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.serial_number = 0

    def approve_account(self):
        user_record = func.get_data_from_file("user_record.json")
        if user_record:
            for user in user_record:
                if user["status"] == "Under Admin Review":
                    print(
                        f"\nUsername: {user["username"]}\tPassword: {user["password"]}"
                    )
                    print("1. Approve \t 2. Disapprove \t 3. Skip")
                    choice = func.populate_int_data(
                        1,
                        3,
                        "Please select an option by entering the corresponding number",
                    )
                    if choice == 1:
                        user["status"] = "Approved"
                        self.serial_number += 1
                        account_number = "SWIFT 1234 " + str(self.serial_number).zfill(
                            4
                        )
                        user["account_number"] = account_number
                        user_data = {
                            "username": user["username"],
                            "password": user["password"],
                            "account_number": account_number,
                            "balance": 0,
                            "transaction_history": [],
                        }
                        func.set_data_in_file(f"{account_number}.json", user_data)
                    elif choice == 2:
                        user["status"] = "Disapproved"

            func.set_data_in_file("user_record.json", user_record)

    def show_user_details(self):
        user_record = func.get_data_from_file("user_record.json")
        if user_record:
            for user in user_record:
                print()
                print("*" * 30)
                print(f"Username: {user['username']}")
                print(f"Status: {user['status']}")
                if user["account_number"]:
                    print(f"Account Number: {user['account_number']}")
                print("*" * 30)
        else:
            print("No User Record Found!")

    def delete_account(self):
        print("\nTo delete an account, please provide us with the following details.")
        user_account_number = func.populate_string_data("User Account Number")
        file_path = f"{user_account_number}.json"
        deleted_user = {}
        if os.path.exists(file_path):
            os.remove(file_path)
            user_record = func.get_data_from_file("user_record.json")
            for user in user_record:
                if user["account_number"] == user_account_number:
                    deleted_user = user
                    break
            user_record.remove(deleted_user)
            func.set_data_in_file("user_record.json", user_record)
            print(f"{user_account_number} was successfully deleted.")
        else:
            print(
                f"Deletion failed! No user exits with account number {user_account_number}"
            )

    def freeze_account(self):
        print("\nTo freeze an account, please provide us with the following details.")
        user_account_number = func.populate_string_data("User Account Number")
        file_path = f"{user_account_number}.json"
        if os.path.exists(file_path):
            user_record = func.get_data_from_file("user_record.json")
            for user in user_record:
                if user["account_number"] == user_account_number:
                    user["status"] = "Freeze"
                    break
            func.set_data_in_file("user_record.json", user_record)
        else:
            print(
                f"Could not freeze account! User with {user_account_number} is not active"
            )

    def show_user_transactions(self):
        user_record = func.get_data_from_file("user_record.json")
        if user_record:
            for user in user_record:
                if user["status"] == "Approved" or user["status"] == "Freeze":
                    user_obj = User(f"{user["account_number"]}.json")
                    user_obj.print_statement()
        else:
            print("No User Record Found!")


