from user_dict_class import Record, AddressBook

ADRESS_BOOK = AddressBook()


def get_handler(operator: str):
    return OPERATIONS[operator]


def input_error(func) -> str:
    """for error in user input
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"wrong name of contact"
        except ValueError:
            return f"wrong value"
        except IndexError:
            return f"wrong index"
        except TypeError:
            return f"wrong data types. enter numeric"
    return inner


def main() -> None:
    """all input-output block
    """
    while True:
        result = parser(input('wait command: ').lower().strip())
        if result == 'exit':
            print('Good bye!')
            break
        else:
            print(result)


def parser(user_in: str) -> str:
    """analiz user input
    Args:
        user_in (str): user input
    Returns:
        str: text for print
    """
    unk_com = True
    for iter in OPERATIONS.keys():
        if user_in.startswith(iter):
            unk_com = False
            return get_handler(iter)(user_in)
    if unk_com:
        return 'I don\'t undestand you'


@input_error
def todo_add(user_in: str) -> str:
    """add new contact
    """
    result = user_in.split(' ')
    if len(result) < 3:
        return 'you need use \' \' to separate'
    record = Record(result[1])
    record.phone_add(result[2])
    ADRESS_BOOK.record_add(record)
    return 'Added'


@input_error
def todo_change(user_in: str) -> str:
    """change phone finded by name
    """
    result = user_in.split(' ')
    if len(result) < 4:
        return 'you need use \' \' to separate'

    record = ADRESS_BOOK.record_find(result[1])
    if record is None:
        return f'can\'t find rec with name {result[1]}'
    record.phone_change(result[2], result[3])

    return 'Changed'


@input_error
def todo_delete_rec(user_in: str) -> str:
    result = user_in.split(' ')
    if len(result) < 3:
        return 'you need use \' \' to separate'

    record = ADRESS_BOOK.record_find(result[2])
    if record is None:
        return f'can\'t find rec with name {result[2]}'
    ADRESS_BOOK.record_delete(result[2])

    return 'deleted record'


@input_error
def todo_delete_phone(user_in: str) -> str:
    result = user_in.split(' ')
    if len(result) < 4:
        return 'you need use \' \' to separate'

    record = ADRESS_BOOK.record_find(result[2])
    if record is None:
        return f'can\'t find rec with name {result[2]}'
    record.phone_delete(result[3])

    return 'deleted phone'


def todo_hello(user_in: str) -> str:
    return 'How can I help you?'


def todo_exit(user_in: str) -> str:
    return 'exit'


def todo_show(user_in: str) -> str:
    return ADRESS_BOOK.print_AB()


@input_error
def todo_phone(user_in: str) -> str:
    """find by key
    """
    result = user_in.split(' ')
    if len(result) < 2:
        return 'you need use \' \' to separate'
    record = ADRESS_BOOK.record_find(result[1])
    if record is None:
        return f'can\'t find rec with name {result[1]}'

    return f'{record.name.value} \nphone: {record.show_rec()}'


OPERATIONS = {
    'add': todo_add,
    'change': todo_change,
    'phone': todo_phone,
    'hello': todo_hello,
    'exit': todo_exit,
    'good bye': todo_exit,
    'close': todo_exit,
    'show all': todo_show,
    'delete id': todo_delete_rec,
    'delete phone': todo_delete_phone,
}

if __name__ == '__main__':
    main()
