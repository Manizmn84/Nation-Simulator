import math


class Consts:
    BASE_PRICE = {'worker': 1200, 'teacher': 1500, 'engineer': 2000}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {
    'worker': {
        'mine': 800,
        'company': 500,
        'school': 300
    },
    'teacher': {
        'mine': 300,
        'school': 1200
    },
    'engineer': {
        'mine': 1000,
        'company': 2000  
    }
}

    MIN_AGE = 15
    AGE_MUL = 10

class Person:
    instances = []

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income: int) -> float:
        return income * math.pow(self.level * self.work_place.level, 0.5)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self) -> float:
        income = self.calc_income()
        life_cost = self.calc_life_cost()
        adjusted_income = self.do_level(income)
        return adjusted_income - life_cost

    def get_job(self) -> str:
        return self.job

    def upgrade(self) -> None:
        self.level += 1

    @staticmethod
    def calc_all() -> float:
        return sum([item.calc() for item in Person.instances])
