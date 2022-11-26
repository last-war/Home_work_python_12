from datetime import datetime
from collections import UserDict


class AddressBook(UserDict):

    def record_add(self, cur_rec):

        old_rec = self.record_find(cur_rec.name.value)
        if old_rec is None:
            self.data[cur_rec.name.value] = cur_rec
        else:
            old_rec.phones.append(cur_rec.phones[0])

    def record_find(self, key: str):
        if self.data.get(key):
            return self.data.get(key)
        return None

    def print_AB(self):
        # TODO
        res_str = ''
        for rec_key in self.data:
            rec = self.data.get(rec_key)
            res_str += f'{str(rec.name)}:{rec.name.value} \nphone: {rec.show_rec()}'
        return res_str

    def record_delete(self, key):
        del self.data[key]

    def iterator(self, rec_num=3):
        res_str = ''
        iter = 0

        for record in self.data.values():
            res_str += f'{record.show_rec()}/n'
            iter += 1

            if iter == rec_num:
                yield res_rec
                res_rec = ''
                iter = 0

        if res_rec:
            yield res_rec


class Record:

    def __init__(self, value):
        self.name = Name(value)
        self.phones = []
        self.birthday = None

    def birthday_add(self, value):
        self.birthday = Birthday(value)

    def day_to_birthday(self):
        if not self.birthday:
            raise ValueError('contact haven\'t birthday info')
        return (self.birthday.value - datetime.today()).days

    def phone_add(self, value):
        self.phones.append(Phone(value))

    def phone_change(self, value_old, value_new):
        try:
            self.phones.remove(self.phone_find(value_old))
        except:
            raise ValueError('Wrong old phone')
        self.phones.append(Phone(value_new))

    def phone_delete(self, value):
        try:
            self.phones.remove(self.phone_find(value))
        except:
            raise ValueError('Wrong old phone')

    def phone_find(self, key: str):
        for phone in self.phones:
            if phone.value == key:
                return phone

    def show_rec(self):
        res_str = ''
        for iter in self.phones:
            res_str += f'\n{iter.value}'
        if self.birthday:
            res_str += f'\n{str(self.birthday)}:{self.birthday.value}'
        return res_str


class Field:
    field_description = "General"

    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self) -> str:
        return f'{self.field_description}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    field_description = "Phone"

    @Field.value.setter
    def value(self, value: str):
        value = (value.strip().removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace("-", "")
                 .replace(" ", ""))
        if not value.isnumeric():
            raise TypeError('Wrong phones.')
        self._value = value


class Name(Field):
    field_description = "Name"

    @Field.value.setter
    def value(self, value: str):
        if value.isnumeric():
            raise KeyError('Wrong Name.')
        self._value = value


class Birthday(Field):
    field_description = "Birthday"

    @Field.value.setter
    def value(self, value):
        try:
            self._value = datetime.strptime(value, '%Y-%m-%d').date()
        except:
            raise ValueError("Birthday must be format YYYY-m-d")
