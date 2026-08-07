import random
import string

def random_menu():

    while True:

        print("\n===== Random Menu =====")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Random OTP")
        print("4. Generate Random Password")
        print("5. Back to Main Menu")

        ch = int(input("Enter Choice: "))

        match ch:

            case 1:
                print("Random Number:", random.randint(1, 100))

            case 2:
                size = int(input("How many numbers in the list? "))
                random_list = []

                for i in range(size):
                    random_list.append(random.randint(1, 100))

                print("Random List:", random_list)

            case 3:
                otp = random.randint(1000, 9999)
                print("OTP:", otp)

            case 4:
                length = int(input("Enter Password Length: "))

                chars = string.ascii_letters + string.digits

                password = ""

                for i in range(length):
                    password += random.choice(chars)

                print("Password:", password)

            case 5:
                break

            case _:
                print("Invalid Choice")