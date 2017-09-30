from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


Taxi.price_per_km = 1.20
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
total_bill = 0
print("Let's drive!")
print("q)uit, c)hoose taxi, d)rive")
menu_choice = str(input(">>> ").lower())
while menu_choice != "q":
    if menu_choice == "c":
        print("Taxis available:")
        for i,taxi in enumerate(taxis):
            print("{} - {}".format(i,taxi))
        taxi_choice = int(input("Choose taxi: "))
        print("Bill to date: ${:.2f}".format(total_bill))
    elif menu_choice == "d":
        taxis[taxi_choice].start_fare()
        distance_to_travel = int(input("Drive how far? "))
        taxis[taxi_choice].drive(distance_to_travel)
        current_fare = taxis[taxi_choice].get_fare()
        total_bill += current_fare
        print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, current_fare))
        print("Bill to date: ${:.2f}".format(total_bill))
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = str(input(">>> ").lower())
print("Total trip cost: ${:.2f}".format(total_bill))
print("Taxis are now: ")
for i, taxi in enumerate(taxis):
    print("{} - {}".format(i, taxi))


