import os
import sys
import subprocess
Shooter = "Shooter"
Snake = "Snake"
Space = "Space"
src_str = "\src"
MenuStr = f"""
        1: {Shooter} Game  
        2: {Snake} Game 
        3: {Space} Game 
        4: Quit
        """
choices = [str(i) for i in range(1, 5)]


def main():
    default_dir =os.getcwd()
    while True:
        choice = menu()
        print(choice)
        if (not choice.isdigit() or (choice not in choices)):
            print("Invalid entry")
            continue
        elif (choice == "1"):
            os.chdir(default_dir + "\src\Shooter")
            subprocess.run("python main.py")
            os.chdir(default_dir)
            # bug
            #Shooter.main()
            saut()

        elif (choice == "2"):
            os.chdir(default_dir+"\src\Snake")
            subprocess.run("python main.py")
            os.chdir(default_dir)
            #snake.run()
            saut()
        elif (choice == "3"):
            os.chdir(default_dir + "\src\Space")
            subprocess.run("python main.py")
            os.chdir(default_dir)
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
