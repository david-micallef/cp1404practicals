from prac_08.unreliable_car import UnreliableCar


taxi_one = UnreliableCar("Prius 1", 100, 0)
taxi_one.drive(40)
print(taxi_one)

taxi_two = UnreliableCar("Prius 2", 100, 100)
taxi_two.drive(40)
print(taxi_two)
