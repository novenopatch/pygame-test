import os
import sys
import subprocess
Shooter = "Shooter"
Snake = "Snake"
Space = "Space"
Flappy = "Flappy bird"
src_str = "\src"
MenuStr = f"""
        1: {Shooter} Game  
        2: {Snake} Game 
        3: {Space} Game 
        4: {Flappy}
        5: Quit
        """
choices = [str(i) for i in range(1, 6)]
default_dir =os.getcwd()

def main():

    while True:
        choice = menu()
        print(choice)
        if (not choice.isdigit() or (choice not in choices)):
            print("Invalid entry")
            continue
        elif (choice == "1"):
            os.chdir(default_dir + "\src\Shooter")
            run_main()

        elif (choice == "2"):
            os.chdir(default_dir+"\src\Snake")
            run_main()
        elif (choice == "3"):
            os.chdir(default_dir + "\src\Space")
            run_main()
        elif (choice == "4"):
            os.chdir(default_dir + "\src\Flappy_bird")
            run_main()
        elif (choice == "5"):
            quit()
            sys.exit()

def run_main():
    subprocess.run("python main.py")
    os.chdir(default_dir)
    saut()
def menu():
    print(MenuStr)
    return input("������ Your Choice : ")


def saut():
    print("_" * 50)


def quit():
    print("À Bientot !")


if __name__ == '__main__':
    main()
