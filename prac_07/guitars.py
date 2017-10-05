from prac_07.guitar import Guitar

guitars = []
print("My guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    guitar_name = input("Name: ")
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010,1512.9))


for i in range(len(guitars)):
    if guitars[i].is_vintage():
        vintage = "(vintage)"
    else:
        vintage = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitars[i].name, guitars[i].year,guitars[i].cost, vintage))
