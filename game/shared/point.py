class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __eq__(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __mod__(self, other):
        """Gets the remainder of this Point divided by the given one.

        Args:
            other (Point): The Point to compare.

        Returns:
            Point: A new Point that is the remainder.
        """
        return Point(self.x % other.x, self.y % other.y)

    def scale(self, factor: int):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.

        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __floordiv__(self, other):
        return Point(int(self.x // other), int(self.y // other))
