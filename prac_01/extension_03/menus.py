def main():
    username = str(input("Enter name: "))
    menu_choice = menu()
    display_menu_text(menu_choice, username)

def display_menu_text(menu_choice, username):
    while menu_choice != "Q":
        if menu_choice == "H":
            print("Hello", username)
        elif menu_choice == "G":
            print("Goodbye", username)
        else:
            print("Invalid choice")
        menu_choice = menu()
    print("Finished.")

def menu():
    menu_choice = str(input("(H)ello" + "\n" +
                     "(G)oodbye" + "\n" +
                     "(Q)uit" + "\n" + "\n" +
                    ">>> ")).upper()
    return(menu_choice)

main()