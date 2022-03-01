import sys
import time

from directions import Directions
from map import Map

except_message = "Tímto směrem jít nemůžeš"

y_coord = 0
x_coord = 0
position = Map.map[y_coord][x_coord]

intro = f"Zdravím, cizinče!\n" \
        f"Vítej na dobrodružné výpravě.\n" \
        f"Tvým úkolem je dostat se skrze hustý les bezpečně domů.\n" \
        f"Jdeme na to...\n\n"

for char in intro:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

while position.end is not True:
    directions = ""
    try:
        Map.map[y_coord + 1][x_coord]
        directions += Directions.EAST.value + " "
    except:
        pass
    try:
        Map.map[y_coord - 1][x_coord]
        directions += Directions.WEST.value + " "
    except:
        pass
    try:
        Map.map[y_coord][x_coord + 1]
        directions += Directions.NORTH.value + " "
    except:
        pass
    try:
        Map.map[y_coord][x_coord - 1]
        directions += Directions.SOUTH.value + " "
    except:
        pass

    print(f"{position.description} Můžeš jít na: {directions}")

    choice = input("Kterým směrem chceš jít? n- sever, e- východ, s- jih, w- západ")
    if choice.lower() == 'e':
        try:
            y_coord += 1
            position = Map.map[y_coord][x_coord]
        except:
            print(except_message)
    elif choice.lower() == 'w':
        try:
            y_coord -= 1
            position = Map.map[y_coord][x_coord]
        except:
            print(except_message)
    elif choice.lower() == 'n':
        try:
            x_coord += 1
            position = Map.map[y_coord][x_coord]
        except:
            print(except_message)
    elif choice.lower() == 's':
        try:
            x_coord -= 1
            position = Map.map[y_coord][x_coord]
        except:
            print(except_message)
    else:
        print("Zadej správný směr. n- sever, e- východ, s- jih, w- západ")

    if position.end:
        print(f"{position.description} Vyhrál jsi!")
