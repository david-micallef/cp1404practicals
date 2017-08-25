def main():
    loop_first()
    loop_second()
    loop_third()

def loop_first():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

def loop_second():
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()

def loop_third():
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

main()