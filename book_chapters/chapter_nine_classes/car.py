# describe car class with odometr

class Car:

    def __init__(self, name, year, colour):
        self.name = name
        self.year = year
        self.colour = colour
        self.odometer = 0

    def describe_car(self):
        return f"{self.name} {self.year} {self.colour} {self.odometer} km"

    def update_odometer(self, miliage):
        if miliage >= self.odometer:
            self.odometer = miliage

    def increment_odometer(self, miliage):
        self.odometer += miliage


new_car = Car('Opel', 1998, 'Red')
print(new_car.odometer)
new_car.update_odometer(500)
print(new_car.odometer)
new_car.increment_odometer(37)
print(new_car.odometer)