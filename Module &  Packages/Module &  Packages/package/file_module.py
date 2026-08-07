def file_menu():

    while True:

        print("\n===== File Menu =====")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read From a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        ch = int(input("Enter Choice: "))

        match ch:

            case 1:
                filename = input("Enter File Name: ")

                with open(filename, "w") as f:
                    print("File Created Successfully")

            case 2:
                filename = input("Enter File Name: ")
                data = input("Enter Data: ")

                with open(filename, "w") as f:
                    f.write(data)

                print("Data Written Successfully")

            case 3:
                filename = input("Enter File Name: ")

                try:
                    with open(filename, "r") as f:
                        print("\nFile Content:")
                        print(f.read())

                except FileNotFoundError:
                    print("File Not Found")

            case 4:
                filename = input("Enter File Name: ")
                data = input("Enter Data: ")

                with open(filename, "a") as f:
                    f.write("\n" + data)

                print("Data Appended Successfully")

            case 5:
                break

            case _:
                print("Invalid Choice")