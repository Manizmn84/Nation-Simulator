from person import Person , Consts 
import math

class Engineer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__( name, age)
        self.job = "engineer"

    def get_price(self) -> int:
        return math.floor(Consts.BASE_PRICE["engineer"] * math.pow(Consts.MIN_AGE / self.age,0.5))

    def calc_life_cost(self) -> int:
        return math.floor(Consts.BASE_COST["engineer"] * math.pow(self.age/Consts.MIN_AGE , 0.5))

    def calc_income(self) -> int:
        return math.floor(Consts.BASE_INCOME["engineer"][self.work_place.get_expertise()] * math.pow(Consts.MIN_AGE/self.age , 0.5))