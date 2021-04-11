def revert(model, kilometers):
    mileage_of_cars[model] -= kilometers
    if mileage_of_cars[model] < 10000:
        mileage_of_cars[model] = 10000
    else:
        print(f"{model} mileage decreased by {kilometers} kilometers")


def refuel(model, fuel):
    if fuel_of_cars[model] < 75:
        fuel_of_cars[model] += fuel
        if fuel_of_cars[model] > 75:
            diff = fuel_of_cars[model] - 75
            current_liters = fuel - diff
            fuel_of_cars[model] = 75
            print(f"{model} refueled with {current_liters} liters")
        else:
            print(f"{model} refueled with {fuel} liters")


def drive(model, distance, fuel):
    if fuel_of_cars[model] < fuel:
        print("Not enough fuel to make that ride")
    else:
        print(f"{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        fuel_of_cars[model] -= fuel
        mileage_of_cars[model] += distance
    if mileage_of_cars[model] > 100000:
        print(f"Time to sell the {model}!")
        del mileage_of_cars[model]
        del fuel_of_cars[model]


def add_car(model, mileage, fuel):
    if model not in mileage_of_cars:
        fuel_of_cars[model] = 0
        mileage_of_cars[model] = 0
    fuel_of_cars[model] += fuel
    mileage_of_cars[model] += mileage


n = int(input())
mileage_of_cars = {}
fuel_of_cars = {}

for _ in range(n):
    car, current_mileage, current_fuel = input().split("|")
    add_car(car, int(current_mileage), int(current_fuel))

while True:
    command = input()
    if command == "Stop":
        break
    tokens = command.split(" : ")
    if tokens[0] == "Drive":
        drive(tokens[1], int(tokens[2]), int(tokens[3]))
    elif tokens[0] == "Refuel":
        refuel(tokens[1], int(tokens[2]))
    elif tokens[0] == "Revert":
        revert(tokens[1], int(tokens[2]))

sorted_by_mileage_cars = sorted(mileage_of_cars.items(), key=lambda x: (-x[1], x[0]))

for car, mileage in sorted_by_mileage_cars:
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel_of_cars[car]} lt.")