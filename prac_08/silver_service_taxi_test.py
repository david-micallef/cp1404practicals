from prac_08.silver_service_taxi import SilverServiceTaxi

test = SilverServiceTaxi("Hummer", 200, 2)
test.start_fare()
test.drive(18)
check = test.get_fare()
print(test)
print("${:.2f}".format(check))

test.start_fare()
test.drive(100)
check = test.get_fare()
print(test)
print("${:.2f}".format(check))