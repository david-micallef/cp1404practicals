import random

NUMBER_OF_QUICK_PICKS = 6
MAX_NUMBER = 45
MIN_NUMBER = 1


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for number in range(NUMBER_OF_QUICK_PICKS):
            unique_number = (random.randint(MIN_NUMBER, MAX_NUMBER))
            while unique_number in quick_pick:
                unique_number = (random.randint(MIN_NUMBER, MAX_NUMBER))
            quick_pick.append(unique_number)
        quick_pick.sort()
        print_numbers(quick_pick)


def print_numbers(quick_pick):
    for i in range(NUMBER_OF_QUICK_PICKS):
        print("{:>2}".format(quick_pick[i]), end=" ")
    print("")


main()
