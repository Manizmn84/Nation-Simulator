from work_place import WorkPlace, Consts
import math

class Mine(WorkPlace):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self) -> None:
        self.capacity = int(pow(self.level,2))

    def calc_costs(self) -> int:
        return int(Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level)
