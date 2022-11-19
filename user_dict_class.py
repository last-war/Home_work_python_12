class UserDict:
    pass


class AddressBook(UserDict):

    data = dict()

    def record_add(self, cur_rec):
        old_rec = self.record_find(cur_rec.name.value)
        if old_rec != None:
            old_rec.list_phone.append(cur_rec.list_phone[0])
        else:
            self.data.update({cur_rec.name.value: cur_rec})

    def record_find(self, key: str):
        if key in self.data.keys():
            return self.data.get(key)
        return None


class Record:

    def __init__(self, value):
        self.name = Name(value)
        self.list_phone = []

    def phone_add(self, clean_phone):
        self.list_phone.append(Phone(clean_phone))

    def phone_change(self, clean_phone):
        self.list_phone = []
        self.list_phone.append(Phone(clean_phone))

    def phone_delete(self):
        self.list_phone = []

    def show_rec(self):
        res_str = []
        for iter in self.list_phone:
            res_str.append(iter.value)
        return ",".join(res_str)


class Field:
    field_description = "General"

    def __init__(self, value):
        self.value = value
        self.validate(value)

    # додаткові перевірки
    def validate(self, value):
        self.value = value


class Phone(Field):

    field_description = "Phone"

    def validate(self, phone: str):
        new_phone = (
            phone.strip().removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        self.value = new_phone


class Name(Field):
    field_description = "Name"
