from src.Position import Position

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'


class Rover:

    def __init__(self, position: Position):
        self._position: Position = position

    @property
    def position(self) -> Position:
        return self._position

    def move_forward(self):
        if self._position.direction == 'N':
            self._position = self._position.move_forward_x()
        elif self._position.direction == 'E':
            self._position = self._position.move_forward_y()
        elif self._position.direction == 'S':
            self._position = self._position.move_back_x()
        elif self._position.direction == 'W':
            self._position = self._position.move_back_y()

    def move_back(self):
        if self._position.direction == 'N':
            self._position = self._position.move_back_x()
        elif self._position.direction == 'E':
            self._position = self._position.move_back_y()
        elif self._position.direction == 'S':
            self._position = self._position.move_forward_x()
        elif self._position.direction == 'W':
            self._position = self._position.move_forward_y()

    def turn_right(self):
        if self._position.direction == 'N':
            new_direction = 'E'
        elif self._position.direction == 'E':
            new_direction = 'S'
        elif self._position.direction == 'S':
            new_direction = 'W'
        elif self._position.direction == 'W':
            new_direction = 'N'
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                new_direction,
                                self._position.world)
        self._position = new_position

    def turn_left(self):
        if self._position.direction == 'N':
            new_direction = 'W'
        elif self._position.direction == 'W':
            new_direction = 'S'
        elif self._position.direction == 'S':
            new_direction = 'E'
        elif self._position.direction == 'E':
            new_direction = 'N'
        new_position = Position(self._position.coordinates[0],
                                self._position.coordinates[1],
                                new_direction,
                                self._position.world)
        self._position = new_position

    def current_direction(self) -> str:
        return self._position.direction

    def current_coordinates(self) -> list:
        return self._position.coordinates

