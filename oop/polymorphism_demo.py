import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Represents a circle shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage for demonstration:
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(10, 2),
        Circle(7)
    ]

    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")
