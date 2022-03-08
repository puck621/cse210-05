import constants
from game.shared.color import Color
from game.shared.point import Point


class Actor:
    """A visible, moveable thing that participates in the game. 

    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        text (string): The text to display
        font_size (int): The font size to use.
        color (Color): The color of the text.
        position (Point): The screen coordinates.
        velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self.text = ""
        self.font_size = 15
        self.color = Color(255, 255, 255)
        self.position = Point(0, 0)
        self.velocity = Point(0, 0)

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        self.position = (self.position + self.velocity) % Point(constants.MAX_X, constants.MAX_Y)

    def set_color(self, color):
        """Updates the color to the given one.

        Args:
            color (Color): The given color.
        """
        self.color = color

    def set_position(self, position):
        """Updates the position to the given one.

        Args:
            position (Point): The given position.
        """
        self.position = position

    def set_font_size(self, font_size):
        """Updates the font size to the given one.

        Args:
            font_size (int): The given font size.
        """
        self.font_size = font_size

    def set_text(self, text):
        """Updates the text to the given value.

        Args:
            text (string): The given value.
        """
        self.text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.

        Args:
            velocity (Point): The given velocity.
        """
        self.velocity = velocity
