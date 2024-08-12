
from accessify import private, protected

class Autobus:

    passagirs = list()

    # def __init__(self):
    #
    #     # self.passagir.append("Миша")

    def add_pasagira(self, passagir):
        self.passagirs.append(passagir)


    def delete_passagir_lubova(self):

        if len(self.passagirs) != 0:
            self.passagirs.pop(-1)
        else:
            print("Пассажиров нет")

    def delete_passagir(self, passagir):
        self.passagirs.remove(passagir)


    def __str__(self):
        return str(self.passagirs)

class Children:

    name: str
    pologenie: bool

    def __init__(self, name):
        self.name = name
        self.pologenie = 0

    def __str__(self):
        return str(self.name) + str(self.pologenie)

    def pologenie_children(self):
        return self.pologenie==0

df = Children("Vfvfv")


print(getattr(df, "name"))

#
school_bus = Autobus()
school_bus.delete_passagir_lubova()

#
# l = list()
#
# masha = Children("Маша")
#
# l.append(masha)
#
# for i in l:
#
#     j = i.pologenie_children()
#     print(j)