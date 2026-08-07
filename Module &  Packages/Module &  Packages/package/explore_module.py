import math
import random
import uuid
from datetime import datetime

def explore_menu():

    name=input("Enter module name: ")

    match name:

        case "math":
            print(dir(math))

        case "random":
            print(dir(random))

        case "uuid":
            print(dir(uuid))

        case "datetime":
            print(dir(datetime))

        case _:
            print("Module not available")