class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50


class WorkPlace:
    instances = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1 
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self) -> None:
        self.level += 1
        self.calc_capacity()

    def hire(self, person) -> None:
        if not (self.capacity > len(self.employees)) :
            raise WorkPlaceIsFull()
        person.work_place = self
        self.employees.append(person)

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -1 * self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        return sum([item.calc() for item in WorkPlace.instances])

