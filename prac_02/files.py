def main():
    write_name_to_file()
    read_name_from_file()
    add_numbers_from_file()
    add_any_numbers_from_file()


def write_name_to_file():
    out_file = open("name.txt", "w")
    username = (str(input("Please enter your name: ")))
    print(username, file=out_file)
    out_file.close()


def read_name_from_file():
    in_file = open("name.txt", "r")
    print("Your name is", in_file.read())
    in_file.close()


def add_numbers_from_file():
    add_numbers = 0
    in_file = open("numbers.txt", "r")
    number_list = in_file.readlines()
    for i in range(len(number_list)):
        add_numbers += int(number_list[i])
    print(add_numbers)
    in_file.close()


def add_any_numbers_from_file():
    extended_add_numbers = 0
    in_file = open("extended.txt", "r")
    extend_list = in_file.readlines()
    for i in range(len(extend_list)):
        extended_add_numbers += int(extend_list[i])
    print(extended_add_numbers)
    in_file.close()

main()
