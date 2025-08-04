from .work_place import WorkPlace, Consts
import math

class School(WorkPlace):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self) -> None:
        self.capacity = math.floor(pow(self.level,0.5))

    def calc_costs(self) -> int:
        return int(math.floor(pow(self.level,0.5)) * Consts.BASE_PLACE_COST)
