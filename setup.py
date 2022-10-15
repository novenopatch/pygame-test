import sys

from src.shooter import main as shooter

MenuStr = """
        1: Shooter Game  
        2: Snake Game 
        3: Space Game 
        4: Quit
        """
choices = [str(i) for i in range(1, 5)]


def main():
    while True:
        choice = menu()
        print(choice)
        if (not choice.isdigit() or (choice not in choices)):
            print("Invalid entry")
            continue
        elif (choice == "1"):
            # bug
            shooter.main()
            saut()

        elif (choice == "2"):
            saut()
        elif (choice == "3"):
            saut()
        elif (choice == "4"):
            quit()
            sys.exit()


def menu():
    print(MenuStr)
    return input("������ Your Choice : ")


def saut():
    print("_" * 50)


def quit():
    print("À Bientot !")


if __name__ == '__main__':
    main()
