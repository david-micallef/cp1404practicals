from prac_08.taxi import Taxi


taxi_one = Taxi("Prius 1", 100)
taxi_one.drive(40)
current_fare = taxi_one.get_fare()
print(taxi_one)
print("Current taxi fare is: ${:.2f}".format(current_fare))
taxi_one.start_fare()
taxi_one.drive(100)
current_fare = taxi_one.get_fare()
print(taxi_one)
print("Current taxi fare is: ${:.2f}".format(current_fare))
