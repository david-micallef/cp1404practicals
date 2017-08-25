import math

def main():
    x_value = int(input("Enter x value: "))
    y_value = int(input("Enter y value: "))
    menu_choice = menu()
    while menu_choice != 4:
        if menu_choice == 1:
            even_sequence(x_value, y_value)
            menu_choice = menu()
        elif menu_choice == 2:
            odd_sequence(x_value, y_value)
            menu_choice = menu()
        elif menu_choice == 3:
            squares_sequence(x_value, y_value)
            menu_choice = menu()
    print("You have exited the program.")

def even_sequence(x_value, y_value):
    for i in range (x_value, y_value):
        if i % 2 == 0:
            print(i, end=", ")

def menu():
    menu_choice = int(input("\n" + "Press (1) to show the even numbers from x to y: " + "\n" +
                            "Press (2) to show the odd numbers from x to y: " + "\n" +
                            "Press (3) to show the squares from x to y: " + "\n" +
                            "Press (4) to exit the program." + "\n"))
    return menu_choice

def odd_sequence(x_value, y_value):
    for i in range (x_value, y_value):
        if i % 2 == 1:
            print (i, end= ", ")

def squares_sequence(x_value, y_value):
    for i in range(x_value, y_value):
        if math.sqrt(i) % 1 == 0:
            print (i, end= ", ")

main()