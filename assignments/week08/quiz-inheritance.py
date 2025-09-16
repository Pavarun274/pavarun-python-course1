""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, door):
        super().__init__(brand, model, year)
        self.number_of_door = door

    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nNumber of door: {self.number_of_door}"


myCar = Car("Toyota", "Crown", 2025, 4)
print(myCar.get_info())