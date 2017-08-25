import random


def main():

    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for number in range(6):
            unique_number = (random.randint(1, 45))
            while unique_number in quick_pick:
                unique_number = (random.randint(1, 45))
            quick_pick.append(unique_number)
        quick_pick.sort()
        print_numbers(quick_pick)


def print_numbers(quick_pick):
    for i in range(6):
        print("{:>2}".format(quick_pick[i]), end=" ")
    print("")


main()