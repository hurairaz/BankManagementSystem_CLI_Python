import functions as func
import json
from admin import Admin
from user import User


def main():
    bank_admin = Admin("admin", "admin123")

    while True:
        print("\n**********\tSwiftBank Limited\t**********\n")
        print("1. Login")
        print("2. Request to create an account")
        print("3. Check status")
        print("4. About")
        print("5. Exit")
        choice = func.populate_int_data(
            1, 5, "Please select an option by entering the corresponding number"
        )

        if choice == 4:
            print("\nAbout FinGuard Bank Limited")
            print(
                "FinGuard Bank Limited is a premier financial institution dedicated to secure banking solutions."
            )
            print(
                "Our mission is to safeguard your financial future while offering a comprehensive range of services."
            )
            print(
                "We are committed to helping you achieve your financial goals with confidence and peace of mind."
            )

        elif choice == 2:
            print(
                "\nTo request an account, please provide us with the following details."
            )
            username_input = func.populate_string_data("Username")
            password_input = func.populate_string_data("Password")
            new_user = {
                "username": username_input,
                "password": password_input,
                "status": "Under Admin Review",
                "account_number": "",
            }

            try:
                try:
                    with open("user_record.json", "r") as file:
                        user_record = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    user_record = []

                if any(
                    user["username"] == username_input
                    and user["password"] == password_input
                    for user in user_record
                ):
                    print("User already exists. Please log in to your account.")
                else:
                    user_record.append(new_user)
                    with open("user_record.json", "w") as file:
                        json.dump(user_record, file)

                    print(
                        f"\nThank you, {username_input}! Your account request has been submitted."
                    )
                    print(
                        "You can check the status of your account (Under Admin Review, Approved, or Disapproved)."
                    )

            except PermissionError:
                print("You do not have permission to access this file.")
            except OSError as e:
                print(f"Something went wrong when opening the file: {e}")

        elif choice == 3:
            print(
                "\nTo check your account status, please provide us with the following details."
            )
            username_input = func.populate_string_data("Username")
            password_input = func.populate_string_data("Password")
            try:
                with open("user_record.json", "r") as file:
                    user_record = json.load(file)
                found = False
                for user in user_record:
                    if (
                        user["username"] == username_input
                        and user["password"] == password_input
                    ):
                        print(f"Status: {user['status']}")
                        found = True
                if not found:
                    print(
                        "No record found! Please submit a request to create an account."
                    )
            except json.JSONDecodeError:
                print("No record found! Please submit a request to create an account.")
            except FileNotFoundError:
                print("The file was not found.")
            except PermissionError:
                print("You do not have permission to access this file.")
            except OSError as e:
                print(f"Something went wrong when opening the file: {e}")

        elif choice == 1:
            print(
                "\nTo login to your account, please provide us with the following details."
            )
            username_input = func.populate_string_data("Username")
            password_input = func.populate_string_data("Password")
            if username_input == "admin" and password_input == "admin123":
                while True:
                    print()
                    print("Admin Dashboard")
                    print("1. Approve User Accounts")
                    print("2. Show User Details")
                    print("3. Delete User Account")
                    print("4. Freeze User Account")
                    print("5. Show User Transactions")
                    print("6. Logout")
                    choice_2 = func.populate_int_data(
                        1,
                        6,
                        "Please select an option by entering the corresponding number",
                    )
                    if choice_2 == 1:
                        bank_admin.approve_account()
                    elif choice_2 == 2:
                        bank_admin.show_user_details()
                    elif choice_2 == 3:
                        bank_admin.delete_account()
                    elif choice_2 == 4:
                        bank_admin.freeze_account()
                    elif choice_2 == 5:
                        bank_admin.show_user_transactions()
                    elif choice_2 == 6:
                        break

            else:
                user_record = func.get_data_from_file("user_record.json")
                found = False
                login_user = ""
                if user_record:
                    for user in user_record:
                        if (
                            user["username"] == username_input
                            and user["password"] == password_input
                            and user["status"] == "Approved"
                        ):
                            found = True
                            login_user = f"{user['account_number']}.json"
                            break
                    if found:
                        new_user = User(login_user)
                        while True:
                            print()
                            print("User Dashboard")
                            print("1. Check Balance")
                            print("2. Deposit Money")
                            print("3. Withdraw Money")
                            print("4. Money Transfer")
                            print("5. Change Password")
                            print("6. Show Transaction History")
                            print("7. Print Statement")
                            print("8. Logout")
                            choice_2 = func.populate_int_data(
                                1,
                                8,
                                "Please select an option by entering the corresponding number",
                            )
                            if choice_2 == 1:
                                new_user.check_balance()
                            elif choice_2 == 2:
                                new_user.deposit_amount()
                            elif choice_2 == 3:
                                new_user.withdraw_amount()
                            elif choice_2 == 4:
                                new_user.transfer_money()
                            elif choice_2 == 5:
                                new_user.change_password()
                            elif choice_2 == 6:
                                new_user.show_transaction_history()
                            elif choice_2 == 7:
                                new_user.print_statement()
                            elif choice_2 == 8:
                                break
                    else:
                        print(
                            "No user with the following credentials exists. Or check your status"
                        )
                else:
                    print("No User Record Found!")

        elif choice == 5:
            print("Thank you for using SwiftBank Limited. Goodbye!")
            break


if __name__ == "__main__":
    main()
