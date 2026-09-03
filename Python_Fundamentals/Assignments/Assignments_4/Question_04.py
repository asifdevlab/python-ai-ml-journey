# Q4. Create a class Shape with a method area().
#    Subclasses: Circle, Rectangle, Triangle
#    Override the area() method in each subclass.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# --- Example Usage ---
circle1 = Circle(5)
rectangle1 = Rectangle(10, 4)
triangle1 = Triangle(6, 3)

print("Area of Circle:", circle1.area())
print("Area of Rectangle:", rectangle1.area())
print("Area of Triangle:",triangle1.area())