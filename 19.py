class Vehicle:
    total_rented = 0   # class variable

    def __init__(self, name):
        self.name = name

    def rent(self, days):
        pass


class Car(Vehicle):
    rate = 1000

    def rent(self, days):
        Vehicle.total_rented += 1
        return days * Car.rate


class Bike(Vehicle):
    rate = 300

    def rent(self, days):
        Vehicle.total_rented += 1
        return days * Bike.rate


class Truck(Vehicle):
    rate = 2000

    def rent(self, days):
        Vehicle.total_rented += 1
        return days * Truck.rate


# Example
c = Car("Sedan")
b = Bike("Yamaha")
t = Truck("Tata")

print("Car Rent:", c.rent(3))
print("Bike Rent:", b.rent(2))
print("Truck Rent:", t.rent(1))

print("Total Vehicles Rented:", Vehicle.total_rented)