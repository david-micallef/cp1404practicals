from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


Taxi.price_per_km = 1.20


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = str(input(">>> ").lower())
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            taxi_information(taxis)
            taxi_choice = int(input("Choose taxi: "))
            print("Bill to date: ${:.2f}".format(total_bill))
        elif menu_choice == "d":
            current_taxi = taxis[taxi_choice]
            current_taxi.start_fare()
            distance_to_travel = int(input("Drive how far? "))
            current_taxi.drive(distance_to_travel)
            current_fare = current_taxi.get_fare()
            total_bill += current_fare
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_fare))
            print("Bill to date: ${:.2f}".format(total_bill))
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = str(input(">>> ").lower())
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: ")
    taxi_information(taxis)


def taxi_information(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

main()
