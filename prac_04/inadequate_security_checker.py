
def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicoLEye',
                 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    enter_username = str(input("Enter username: "))
    if enter_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
