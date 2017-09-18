from prac_07.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print("My guitar: {0}, first made in {1}.".format(name, year))

print(Guitar(name, year, cost))

guitar_gibson = Guitar(name, year, cost)

guitar_another = Guitar(name="Another Guitar", year=2012)

print(guitar_gibson.name, "get_age() - Expected 95. Got", guitar_gibson.get_age())
print(guitar_another.name, "get_age() - Expected 5. Got", guitar_another.get_age())

print(guitar_gibson.name, "is_vintage() - Expected True. Got", guitar_gibson.is_vintage())
print(guitar_another.name, "is_vintage() - Expected False. Got", guitar_another.is_vintage())