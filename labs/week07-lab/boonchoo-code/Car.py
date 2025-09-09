class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    vehicle_type = "Car"
    
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, distance):
        """Method to update mileage"""
        self.mileage += distance
        return f"Drove {distance} km. Total mileage: {self.mileage} km"
    
    def get_info(self):
        """Method to get car information"""
        return f"{self.year} {self.brand} {self.model} - Mileage: {self.mileage} km"
    
    @classmethod
    def get_vehicle_type(cls):
        """Class method to access class attributes"""
        return cls.vehicle_type

# Creating instances
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Accessing class attributes
print(f"All cars have {Car.wheels} wheels") # All cars have 4 wheels
print(f"Vehicle type: {Car.get_vehicle_type()}") # Vehicle type: Car

# Accessing instance attributes
print(car1.get_info()) # 2022 Toyota Camry - Mileage: 0 km
print(car2.get_info()) # 2021 Honda Civic - Mileage: 0 km

# Using methods
print(car1.drive(100)) # Drove 100 km. Total mileage: 100 km
print(car2.drive(250)) # Drove 250 km. Total mileage: 250 km

print(car1.drive(20)) # Drove 20 km. Total mileage: 120 km
print(car2.drive(20)) # Drove 20 km. Total mileage: 270 km