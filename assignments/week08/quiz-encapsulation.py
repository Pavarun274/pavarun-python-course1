"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    
    def __init__(self, x=0, y=0):
        self.__length = x
        self.__width = y

    def getArea(self):
        area = self.__length * self.__width
        return f"Area is {area}"

    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        print(f"Perimeter is {perimeter}")

    def isSquare(self):
        if self.__length == self.__width:
            return "The rectangle is square"
        else:
            return "The rectangle is not square"

rect = Rectangle(5,5)
print(rect.getArea())
rect.getPerimeter()
print(rect.isSquare())