from game.casting.actor import Actor


class Cycle(Actor):
    """
    The responsibility of Cycle is to move itself.

    Attributes:
      segments: length of the cycle
        
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._segments = []
        # self._prepare_body()

    def get_segments(self):
        """Fetches the number of segments of a cycle """
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.velocity
            trailing.velocity = velocity
        self.grow_tail(1)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Adds to the length of the cycle at a steady rate"""
        for _ in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.velocity
            offset =  - velocity
            position = tail.position + offset

            segment = Actor(text="#", color=self._segments[0].color, position=position, velocity=velocity)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Changes direction a cycle is moving by change velocity"""
        self._segments[0].velocity = velocity
    
    def prepare_body(self, position, velocity, color):
        """Provides all information about cycle for other functions"""
        segment = Actor(text="8", color=color, position=position, velocity=velocity)
        self._segments.append(segment)
