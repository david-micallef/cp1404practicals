def main():
    calculate_question_one()
    calculate_question_two()
    calculate_question_three()
    calculate_question_four()

def calculate_question_one():
    out_file = open("name.txt", "w")
    username = (str(input("Please enter your name: ")))
    print (username, file=out_file)
    out_file.close()

def calculate_question_two():
    in_file = open("name.txt", "r")
    print("Your name is",in_file.read())
    in_file.close()

def calculate_question_three():
    add_numbers = 0
    number_file = open("numbers.txt", "r")
    number_list = number_file.readlines()
    for i in range(len(number_list)):
        add_numbers += int(number_list[i])
    print(add_numbers)
    number_file.close()

def calculate_question_four():
    extended_add_numbers = 0
    extend_file = open("extended.txt", "r")
    extend_list = extend_file.readlines()
    for i in range(len(extend_list)):
        extended_add_numbers += int(extend_list[i])
    print(extended_add_numbers)
    extend_file.close()

main()