LOWER = 33
UPPER = 127

def main():
    for i in range(LOWER, UPPER):
        print("{:>3} {}".format(i,chr(i)))
    entered_character = str(input("Enter a character: "))
    print("The ASCII code for {0} is {1}".format(entered_character,ord(entered_character)))
    entered_number = int(input("Enter a number between {0} and {1}: ".format(LOWER, UPPER)))
    print("The character for {0} is {1}".format(entered_number,chr(entered_number)))

main()