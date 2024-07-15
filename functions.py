import json


class InvalidChoiceError(Exception):
    pass


def get_data_from_file(filename, special_message=""):
    data = None
    try:
        with open(filename, "r") as file:
            data = json.load(file)

    except json.JSONDecodeError:
        print("No records found. The file is empty.")
    except FileNotFoundError:
        if special_message:
            print(special_message)
        else:
            print("File not found.")
    except PermissionError:
        print("Permission denied. Unable to access the file.")
    except OSError as e:
        print(f"An error occurred while opening the file: {e}")
    finally:
        return data


def set_data_in_file(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
    except PermissionError:
        print("Permission denied. Unable to access the file.")
    except OSError as e:
        print(f"An error occurred while opening the file: {e}")


def populate_string_data(input_text):
    final_value = None
    while True:
        input_value = input(f"{input_text}: ").strip()
        if not input_value:
            print(f"{input_text} cannot be empty. Please enter a valid {input_text}.")
        else:
            value = input_value
            break
    return value


def populate_int_data(lower_bound, upper_bound, input_text):
    final_value = 0
    while True:
        input_value = input(f"{input_text}: ")
        try:
            input_value = int(input_value)
            if input_value not in range(lower_bound, upper_bound + 1):
                raise InvalidChoiceError
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidChoiceError:
            print("Invalid input. Choice out of range.")
        else:
            value = input_value
            break
    return value


