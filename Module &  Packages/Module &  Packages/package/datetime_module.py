from datetime import datetime
import time

def datetime_menu():

    while True:

        print("\nDate & Time Menu")
        print("1.Display Current Date and Time")
        print("2. Calculate difference between two dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to main menu")

        ch = int(input("Enter yourchoice: "))

        match ch:

            case 1:
                print("Current Date & Time:", datetime.now())

            case 2:
                d1 = input("Enter First Date (YYYY-MM-DD): ")
                d2 = input("Enter Second Date (YYYY-MM-DD): ")

                date1 = datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.strptime(d2, "%Y-%m-%d")

                print("Difference:", abs((date2 - date1).days), "days")

            case 3:
                print(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

            case 4:
                input("Press ENTER to Start Stopwatch...")
                start = time.time()

                input("Press ENTER to Stop Stopwatch...")
                end = time.time()

                print("Elapsed Time:", round(end - start, 2), "seconds")

            case 5:
                sec = int(input("Enter countdown time (seconds): "))

                while sec > 0:
                    print("Time Left:", sec, "seconds")
                    time.sleep(1)
                    sec -= 1

                print("Time's Up!")

            case 6:
                break

            case _:
                print("Invalid Choice")