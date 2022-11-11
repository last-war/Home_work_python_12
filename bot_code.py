ADRESS_BOOK = dict()


def format_phone_number(func: function) -> str:
    def inner(phone):
        phone = func(phone)
        return ('+' if len(phone) == 12 else '+38')+phone

    return inner


def get_handler(operator: str) -> function:
    return OPERATIONS[operator]


def input_error(func: function) -> str:
    """for error in user input
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{func.__name__} wrong name of contact"
        except ValueError:
            return f"{func.__name__} wrong value"
        except IndexError:
            return f"{func.__name__} wrong index"
        except TypeError:
            return f"{func.__name__} wrong data types. enter numeric"
    return inner


def main() -> None:
    """all input-output block
    """
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


def param_control(user_in, num_param):
    # don't used
    result = user_in.split(' ')
    if len(result) < num_param:
        return ['', 'you need use \' \' to separate']


def parser(user_in: str) -> list:
    """analiz user input

    Args:
        user_in (str): user input

    Returns:
        list: 0 - command to while 1 - text for print
    """
    # разобрать ввод вернуть 0-дествие 1-text
    if user_in == '.':
        return ['break']

    elif user_in in ['good bye', 'close', 'exit']:
        return ['break', 'Good bye!']

    elif user_in == 'hello':
        return ['', 'How can I help you?']

    elif user_in[0:5] == 'phone':
        result = user_in.split(' ')
        if len(result) < 2:
            return ['', 'you need use \' \' to separate']
        return ['', get_handler('phone')(result[1])]

    elif user_in[0:6] == 'change':
        result = user_in.split(' ')
        if len(result) < 3:
            return ['', 'you need use \' \' to separate']
        return ['', get_handler('change')(result[1], result[2])]

    elif user_in[0:3] == 'add':
        result = user_in.split(' ')
        if len(result) < 3:
            return ['', 'you need use \' \' to separate']
        return ['', get_handler('add')(result[1], result[2])]

    elif user_in == 'show all':
        if len(ADRESS_BOOK):
            return ['print', 'end of adress book']
        else:
            return ['print', 'adress book is empty']
    else:
        return ['', 'I don\'t undestand you']


@format_phone_number
def sanitize_phone_number(phone: str) -> str:
    new_phone = (
        phone.strip().removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


@input_error
def todo_add(name: str, phone: str) -> str:
    """add new contact
    """
    ADRESS_BOOK[name] = sanitize_phone_number(phone)
    return 'Added'


@input_error
def todo_change(name: str, phone: str) -> str:
    """change phone fined by name
    """
    ADRESS_BOOK[name] = sanitize_phone_number(phone)
    return 'Changed'


@input_error
def todo_phone(name: str) -> str:
    """find by key
    """
    return ADRESS_BOOK[name]


OPERATIONS = {
    'add': todo_add,
    'change': todo_change,
    'phone': todo_phone
}

if __name__ == '__main__':
    main()
