from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=random.uniform(0,100)):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance_to_drive = random.uniform(0,100)
        if chance_to_drive > self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven

