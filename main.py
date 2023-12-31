phone_book = {}


def input_error(func):
    def wrapper(*args, **argv):
        try:
            result = func(*args, **argv)
        except KeyError as err:
            return f"Error: Contact not found"
        except ValueError as err:
            return f"Error: Invalid input"
        except IndexError as err:
            return f"Error: Invalid command format"
        except TypeError as err:
            return f"Error {err}"

        return result

    return wrapper


@input_error
def hello_user():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    if is_valid_phone_number(phone) and is_valid_name(name) and name not in phone_book:
        phone_book[name] = phone
        return f"Contact {name} with phone number {phone} added successfully"
    else:
        raise ValueError


@input_error
def change_contact(name, phone):
    if is_valid_phone_number(phone):
        for name_contact in phone_book.keys():
            if name_contact == name:
                phone_book[name_contact] = phone
                return f"Contact {name} has changed phone number {phone}"
    else:
        raise ValueError

@input_error
def phone_of_contact(name):
    if name in phone_book:
        return f"Phone number: {phone_book[name]}"
    else:
        return f"No such contact {name}"


@input_error
def show_all_contacts():
    result = "All contacts:"
    for name, phone in phone_book.items():
        result += f"\nName: {name}; Phone: {phone}"
    return result


@input_error
def bye_user():
    return "Good bye!"


OPERATIONS = {
    'hello': hello_user,
    'add': add_contact,
    'change': change_contact,
    'phone': phone_of_contact,
    'show all': show_all_contacts,
    'good bye': bye_user,
    'close': bye_user,
    'exit': bye_user,
}


def get_handler(operator):
    return OPERATIONS[operator]


def is_valid_phone_number(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    else:
        return False


def is_valid_name(name):
    if name.isalpha():
        return True
    else:
        return False


def parse_command(input_strig):
    input_list = input_strig.lower().split()
    if input_list[0] == 'show' and input_list[1] == 'all' and len(input_list) == 2:
        return input_strig.lower().strip(), []
    elif input_list[0] == 'good' and input_list[1] == 'bye' and len(input_list) == 2:
        return input_strig.lower().strip(), []
    else:
        return input_list[0], input_list[1:]


def main():
    while True:
        command = input("Enter a command: ").lower().strip()
        operator, args = parse_command(command)
        handler = get_handler(operator)
        print(handler(*args))

        if operator in {'good bye', 'close', 'exit'}:
            break


if __name__ == '__main__':
    main()