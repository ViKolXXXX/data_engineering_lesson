class Human:

    def __init__(self, name: str, age: int):
        self.__name = self.validate_value(name, str)
        self.__age = self.validate_value(age, str)

        self.__age = age

    @classmethod
    def validate_value(cls, v_value, v_type: type):  # Валидатор значений
        if isinstance(v_value, v_type):
            return v_value
        else:
            return "Задано не верно"

    def human_info(self):
        return self.__name + ": " + str(self.__age)


class Rota:
    __humans = list()

    def add_human(self, humans: list):
        self.__humans = self.__humans + humans




class Polk:
    __roti = list()

    def add_roti(self, roti: list):
        self.__roti = self.__roti + roti
