import time
from datetime import date, datetime


class Person:  # Camel Case naming | Datatype Object

    # def __init__(self): # method overloading vs overriding
    #     pass

    def __init__(self, name=None, ):
        print("New Object")
        self.__name = name  # attribute public by default
        # self._dob = dob  # attribute # protected by convention
        # self.__smart = None  # attribute # private
        # self.hands = []  # attribute # mutable
        pass

    def __get_name(self):
        return self.__name

    def __set_name(self, name):
        if not name.strip():
            raise ValueError(f"Person attribute 'name' can not be empty.")  # clear messaging

        if self.__name is not None:
            raise ValueError(f"Person attribute 'name' is already provided.")

        self.__name = name

    name = property(
        fget=__get_name,
        fset=__set_name,
    )

    # def get_hands(self):
    #     return self.hands.copy()
    #
    # def get_age(self):  # action
    #     # logical error
    #     return f"{(date.today() - self.dob).days % 365} years and {(date.today() - self.dob) // 365} days"

    # def eat(self, food):  # action
    #     print(f"{self.name} is eating {food}....")
    #     time.sleep(5)
    #     print(f"{self.name} finished eating.")
    #     pass


if __name__ == '__main__':
    p1 = Person()
    # p1.name = "Karam"
    # p1.name = ""
    print(p1.name)

    p1.name = "Karam"
    print(p1.name)
    p1.name = "Ahmad"

    # p1.eat("Mansaf")
    # p1.eat("Knafa")

    # p1.set_name("")
    # print(p1.get_name())
    # p1.name = "Karam"
    # print(p1.name)

    # print(p1.get_age()) # --
    # print(p1.get_hands()) # --
    # print(p1.hands) # --

    # print(p1.smart) # --

    # p2 = Person(name="Rana", dob=date(2008, 4, 22))
    # p2.eat("Slata")
    # p2.eat("Qtaif")

    # print(isinstance(ahmad, object))
