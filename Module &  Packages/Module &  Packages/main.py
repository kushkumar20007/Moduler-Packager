from package.datetime_module import datetime_menu
from package.math_module import math_menu
from package.random_module import random_menu
from package.uuid_module import uuid_menu
from package.file_module import file_menu
from package.explore_module import explore_menu


def main():
    while True:
        print("\nWelcome to the Multi Utility Toolkit")
        print("1. Datetime and Time Operations  ")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. UUID")
        print("5. File Operators")
        print("6. Explore Module Attributes ")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                datetime_menu()
            case 2:
                math_menu()
            case 3:
                random_menu()
            case 4:
                uuid_menu()
            case 5:
                file_menu()
            case 6:
                explore_menu()
            case 7:
                print("Thank You")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
