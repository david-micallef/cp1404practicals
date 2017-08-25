""" David """


def main():
    username = get_name()
    frequency = int(input("Enter the frequency at which each letter is display: "))
    print_name(username, frequency)


def print_name(username, frequency):
    for i in range(0, len(username), frequency):
        print(username[i], end="")


def get_name():
    username = str(input("Enter username: "))
    while username is "":
        print("No username entered.")
        username = str(input("Enter username: "))
    return username

main()
