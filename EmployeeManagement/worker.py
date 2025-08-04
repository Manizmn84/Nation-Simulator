from person import Person , Consts 
import math

class Worker(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name , age)
        self.job = "worker"

    def get_price(self) -> int:
        return math.floor(Consts.BASE_PRICE["worker"] * Consts.MIN_AGE / self.age)

    def calc_life_cost(self) -> int:
        return math.floor(Consts.BASE_COST["worker"] * self.age / Consts.MIN_AGE)

    def calc_income(self) -> int:
        return math.floor(Consts.BASE_INCOME["worker"][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age)