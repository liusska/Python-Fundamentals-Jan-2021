def drive(name, current_distance, current_fuel):
    car = [c for c in cars if c.name == name][0]
    if car. fuel < current_fuel:
        print("Not enough fuel to make that ride")
    else:
        car.fuel -= current_fuel
        car.mileage += current_distance
        print(f"{name} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
    if car.mileage > 100000:
        cars.remove(car)
        print(f"Time to sell the {name}!")


def refuel(name, current_fuel):
    car = [c for c in cars if c.name == name][0]
    new_fuel = 0
    if car.fuel < 75:
        car.fuel += current_fuel
        if car.fuel <= 75:
            new_fuel = current_fuel
        else:
            temp = car.fuel - 75
            new_fuel = current_fuel - temp
            car.fuel = 75
    print(f"{name} refueled with {new_fuel} liters")


def revert(name, kilometers):
    car = [c for c in cars if c.name == name][0]
    car.mileage -= kilometers
    if car.mileage < 10000:
        car.mileage = 10000
    else:
        print(f"{name} mileage decreased by {kilometers} kilometers")


class Car:
    def __init__(self, name, mileage, fuel):
        self.name = name
        self.mileage = mileage
        self.fuel = fuel

    def __repr__(self):
        return f"{self.name} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."


cars = []
n = int(input())
for _ in range(n):
    data = input().split("|")
    car_name = data[0]
    car_mileage = int(data[1])
    car_fuel = int(data[2])
    car = Car(car_name, car_mileage, car_fuel)
    cars.append(car)

while True:
    command = input()
    if command == "Stop":
        break
    tokens = command.split(" : ")
    if tokens[0] == "Drive":
        car = tokens[1]
        distance = int(tokens[2])
        fuel = int(tokens[3])
        drive(car, distance, fuel)
    elif tokens[0] == "Refuel":
        car = tokens[1]
        fuel = int(tokens[2])
        refuel(car, fuel)
    elif tokens[0] == "Revert":
        car = tokens[1]
        distance = int(tokens[2])
        revert(car, distance)


sorted_cars = sorted(cars, key=lambda c: (-c.mileage, c.name))

for car in sorted_cars:
    print(car)