class Rectangle:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def can_fit_inside(self, square):
        if self.width <= square.side and self.height <= square.side:
            return True
        # if orientation change to 90
        if self.height <= square.side and self.width <= square.side:
            return True

        return False

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square:
    def __init__(self, side: int):
        self.side = side

    def area(self) -> int:
        return self.side * self.side

    def __str__(self):
        return f"Square(side={self.side})"


# Creating objects
rectangle1 = Rectangle(4, 5)
square1 = Square(5)

# Printing areas
print("Area of the rectangle:", rectangle1.area())
print("Area of the square:", square1.area())

# Checking if the rectangle can fit inside the square
can_fit = rectangle1.can_fit_inside(square1)
print(f"Can the rectangle fit inside the square? {'Yes' if can_fit else 'No'}")

# Printing the objects
print(rectangle1)
print(square1)
