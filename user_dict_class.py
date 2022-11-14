
class UserDict:
    pass


class AddressBook(UserDict):

    data = dict()

    def record_add(self, cur_rec):
        self.data.update({cur_rec.name.value: cur_rec})

    def record_delete(self, cur_rec):
        pass  # TODO


class Record:
    name = Name()
    list_phone = []

    def phone_add(self):
        pass  # TODO

    def phone_change(self):
        pass  # TODO

    def phone_delete(self):
        pass  # TODO


class Field:
    field_description = "General"

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value


class Phone(Field):
    field_description = "Phone"
    pass  # TODO


class Name(Field):
    field_description = "Name"
    pass  # TODO
