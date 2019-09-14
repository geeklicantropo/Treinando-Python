import converters
import utils
import random
from ecommerce import shipping
from pathlib import Path


'''comand = ""
has_stopped = 0
has_started = 0

while True:
    comand = input("> ").lower()
    if comand == "start" and has_started == 0:
        print("Car started.")
        has_started = 1
        has_stopped = 0
    elif comand == "start" and has_started ==1:
        print("Car already started!!!")
    elif comand == "stop" and has_stopped == 0:
        print("Car stopped.")
        has_stopped = 1
        has_started = 0
    elif comand == "stop" and has_stopped == 1:
        print("Car has already stopped!!!")
    elif comand == "help":
        print("""
            start - to start the car
            stop - to stop the car
            quit - to quit
        """)
    elif comand == "quit":
        break
    else:
        print("Sorry, i don't understand that.")

print(converters.kgs_to_lbs(115))

numbers = [10, 6, 25, 1, 7, 8]
max = utils.find_max(numbers)
print(max)

#shipping.calc_shipping()

class Dice:
    def rool(self):
        first = random.randint(10,18)
        second = random.randint(10,18)
        third = random.randint(10, 18)
        fourth = random.randint(10, 18)
        fifth = random.randint(10, 18)
        sixth = random.randint(10, 18)
        return (first, second, third, fourth, fifth, sixth)


dice = Dice()
print(dice.rool())'''

path = Path()
for file in path.glob('*.py'):
    print(file)
