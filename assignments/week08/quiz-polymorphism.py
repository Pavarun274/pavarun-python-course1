"""
Demonstrate polymorphism by creating:
 
    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""
 
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
 
 
class Fish(Animal):
    def move(self):
        return "Fish swims"
 
 
class Bird(Animal):
    def move(self):
        return "Bird flies"
 
 
class Dog(Animal):
    def move(self):
        return "Dog runs"
 
 
def perform_move(animal: Animal):
    """Call the move method of any Animal instance"""
    return animal.move()
 
 
if __name__ == "__main__":
    animals = [Fish(), Bird(), Dog()]
    for a in animals:
        print(perform_move(a))
