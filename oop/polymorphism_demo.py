import math

class Shape:
    """
    Base class for different shapes.
    Provides a template for the area method that must be overridden by derived classes.
    """
    def area(self):
        raise NotImplementedError("The area method must be overridden by subclasses")

class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    Attributes:
        length: The length of the rectangle.
        width: The width of the rectangle.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.
        Formula: length × width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle.
    Attributes:
        radius: The radius of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Formula: π × radius²
        """
        return math.pi * self.radius ** 2

def main():
    # Creating instances of Rectangle and Circle
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrating polymorphism by calling the area method
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
