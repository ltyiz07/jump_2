import time


if __name__ == "__main__":
    current_floor = int(input("current floor?"))
    selected_floors = []

    while True:
        floor = input("select floor")
        if floor.isnumeric():
            selected_floors.append(int(floor))
        else:
            break

    selected_floors.sort()
    lower_floors = [i for i in selected_floors if current_floor > i]
    higher_floors = [i for i in selected_floors if current_floor < i]
    if higher_floors > lower_floors:
        print("Elevators going up.")
        for i in higher_floors:
            time.sleep(1)
            print("foor ", i)
    elif lower_count <= higher_count:
        print("Elevators going down.")
        for i in lower_floors:
            time.sleep(1)
            print("foor ", i)

    
