class Human:
    """
    Класс люди
    """
    __age: int
    name: str

    def __init__(self, name):
        if self.__validate_name(name):
            self.name = name
        self.__age = ""

    @classmethod
    def __validate_name(cls, name):  # Валидатор имени
        if isinstance(name, str):
            return True

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age

class Children(Human):
    """
    Класс дети
    """

    __mesto: bool

    def __init__(self, name):
        super().__init__(name)
        self.__mesto = False


class Autobus:

    salon = list()










nady = Human("Надя")
nady.set_age(32)

print(nady.get_age())