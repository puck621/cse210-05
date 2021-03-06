from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by winning each round- best of three rounds.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned. Inherits from Actor class.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        """Constructs the score"""
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.text = f"Score: {self._points}"
