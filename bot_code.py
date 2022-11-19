import user_dict_class as AB

ADRESS_BOOK = AB.AddressBook()


def get_handler(operator: str):
    return OPERATIONS[operator]


def input_error(func) -> str:
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
            for iter in ADRESS_BOOK.data.keys():
                print(f'{iter}:{ADRESS_BOOK.data.get(iter).show_rec()}')

        if len(result) > 1:
            print(result[1])


def parser(user_in: str) -> list:
    """analiz user input

    Args:
        user_in (str): user input

    Returns:
        list: 0 - command to while 1 - text for print
    """
    unk_com = True
    for iter in OPERATIONS.keys():
        if user_in.startswith(iter):
            unk_com = False
            return get_handler(iter)(user_in)
    if unk_com:
        return ['', 'I don\'t undestand you']


@input_error
def todo_add(user_in: str) -> list:
    """add new contact
    """
    result = user_in.split(' ')
    if len(result) < 3:
        return ['', 'you need use \' \' to separate']
    record = AB.Record(result[1])
    record.phone_add(result[2])
    ADRESS_BOOK.record_add(record)
    return ['', 'Added']


@input_error
def todo_change(user_in: str) -> list:
    """change phone finded by name
    """
    result = user_in.split(' ')
    if len(result) < 3:
        return ['', 'you need use \' \' to separate']
    record = ADRESS_BOOK.record_find(result[1])
    if record == None:
        return ['', f'can\'t find rec with name {result[1]}']
    record.phone_change(result[2])

    return ['', 'Changed']


@input_error
def todo_delete(user_in: str) -> list:
    """delete phone finded by name
    """
    result = user_in.split(' ')
    if len(result) < 2:
        return ['', 'you need use \' \' to separate']
    record = ADRESS_BOOK.record_find(result[1])
    if record == None:
        return ['', f'can\'t find rec with name {result[1]}']
    record.phone_delete()

    return ['', 'Deleted']


def todo_hello(user_in: str) -> list:
    return ['', 'How can I help you?']


def todo_exit(user_in: str) -> list:
    return ['break', 'Good bye!']


def todo_show(user_in: str) -> list:
    if len(ADRESS_BOOK.data):
        return ['print', 'end of adress book']
    else:
        return ['print', 'adress book is empty']


@input_error
def todo_phone(user_in: str) -> str:
    """find by key
    """
    result = user_in.split(' ')
    if len(result) < 2:
        return ['', 'you need use \' \' to separate']
    return ['', ADRESS_BOOK.record_find(result[1]).show_rec()]


OPERATIONS = {
    'add': todo_add,
    'change': todo_change,
    'phone': todo_phone,
    'hello': todo_hello,
    'exit': todo_exit,
    'good bye': todo_exit,
    'close': todo_exit,
    'show all': todo_show,
    'delete': todo_delete
}

if __name__ == '__main__':
    main()
