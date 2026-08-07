import math

def math_menu():

    while True:

        print("\n===== Math Menu =====")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        ch = int(input("Enter Choice: "))

        match ch:

            case 1:
                n = int(input("Enter Number: "))
                print("Factorial =", math.factorial(n))

            case 2:
                p = float(input("Enter Principal Amount: "))
                r = float(input("Enter Rate (%): "))
                t = float(input("Enter Time (Years): "))

                ci = p * ((1 + r / 100) ** t)
                print("Compound Interest Amount =", round(ci, 2))

            case 3:
                angle = float(input("Enter Angle (Degree): "))

                print("Sin =", math.sin(math.radians(angle)))
                print("Cos =", math.cos(math.radians(angle)))
                print("Tan =", math.tan(math.radians(angle)))

            case 4:
                print("\n1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                shape = int(input("Choose Shape: "))

                match shape:

                    case 1:
                        r = float(input("Enter Radius: "))
                        print("Area =", math.pi * r * r)

                    case 2:
                        l = float(input("Enter Length: "))
                        b = float(input("Enter Breadth: "))
                        print("Area =", l * b)

                    case 3:
                        b = float(input("Enter Base: "))
                        h = float(input("Enter Height: "))
                        print("Area =", 0.5 * b * h)

                    case _:
                        print("Invalid Shape")

            case 5:
                break

            case _:
                print("Invalid Choice")