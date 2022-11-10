ADRESS_BOOK = dict()


def format_phone_number(func):
    def inner(phone):
        phone = func(phone)
        return ('+' if len(phone) == 12 else '+38')+phone

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip().removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            return f"{func.__name__} wrong name of contact"
        except ValueError:
            return f"{func.__name__} wrong value"
        except IndexError:
            return f"{func.__name__} wrong index"
        except TypeError:
            return f"{func.__name__} wrong data types. enter numeric"
    return inner


# разобрать ввод вернуть 0-дествие 1-text  2-логин 3-номер
# @input_error
def parser(user_in):
    if user_in == '.':
        return ['break']

    elif user_in in ['good bye', 'close', 'exit']:
        return ['break', 'Good bye!']

    elif user_in == 'hello':
        return ['hello', 'How can I help you?']

    elif user_in[0:5] == 'phone':
        result = user_in.split(' ')
        return ['', get_handler('phone')(result[1])]

    elif user_in[0:6] == 'change':
        result = user_in.split(' ')
        return ['', get_handler('change')(result[1], result[2])]

    elif user_in[0:3] == 'add':
        result = user_in.split(' ')
        return ['', get_handler('add')(result[1], result[2])]

    elif user_in == 'show all':
        if len(ADRESS_BOOK):
            return ['print', 'end of adress book']
        else:
            return ['print', 'adress book is empty']
    else:
        return ['', 'I don\'t undestand you']


@input_error
def todo_phone(name):
    return ADRESS_BOOK[name]


@input_error
def todo_add(name, phone):
    ADRESS_BOOK[name] = sanitize_phone_number(phone)
    return 'Added'


@input_error
def todo_change(name, phone):
    ADRESS_BOOK[name] = sanitize_phone_number(phone)
    return 'Changed'


OPERATIONS = {
    'add': todo_add,
    'change': todo_change,
    'phone': todo_phone
}


def get_handler(operator):
    return OPERATIONS[operator]


def main():
    while True:
        result = parser(input('wait command: ').lower().strip())
        #0 - command
        #1 - text
        if result[0] == 'break':
            if len(result) > 1:
                print(result[1])
            break
        elif result[0] == 'print':
            for iter in ADRESS_BOOK.keys():
                print(f'{iter}:{ADRESS_BOOK.get(iter)}')

        if len(result) > 1:
            print(result[1])


if __name__ == '__main__':
    main()
