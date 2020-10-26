import random


class Board:
    """A Board has size, an array of player's ships and an array of player's"""
    _boardSize = 0

    class Ship:
        """A Ship has coordinates of its cells."""

        def checkCoordinates(self, row, col, ships):

            if len(ships) > 0:
                for tempShip in ships:
                    for coordinates in tempShip.coordinates:
                        if row == coordinates[0] and col == coordinates[1]:
                            raise Exception(
                                'Ship cannot be placed on occupied cells.')
            if row < 0 or row > self.boardSize-1 or col < 0 or col > self.boardSize-1:
                raise Exception('Ship is not entirely inside of the board.')

            return True

        def __init__(self, size=1, row=-1, col=-1, direction='',
                     boardSize=6, ships=[]):

            self._boardSize = boardSize
            self._direction = direction
            self._coordinates = []
            tempCoordinates = []

            if direction == '':
                while True:
                    row = random.randint(0, boardSize-1)
                    col = random.randint(0, boardSize-1)
                    try:
                        self.checkCoordinates(row, col, ships)
                    except:
                        break
                    else:
                        self.coordinates.append((row, col))
                        break
            elif direction == 'row':
                for i in range(size):
                    if self.checkCoordinates(row, col+i, ships):
                        tempCoordinates.append((row, col + i))
            elif direction == 'column':
                for i in range(size):
                    if self.checkCoordinates(row, col+i, ships):
                        tempCoordinates.append((row + i, col))
            self.coordinates = tempCoordinates

        @property
        def coordinates(self):
            return self._coordinates

        @coordinates.setter
        def coordinates(self, coordinates):
            self._coordinates = coordinates

        @property
        def boardSize(self):
            return self._boardSize

        @property
        def direction(self):
            return self._direction

    def addShip(self, size=1, row=-1, col=-1,
                direction='', boardSize=6):
        """Adds a new Ship to the array of Ships and returns its coordinates as an array of tuples"""

        ship = self.Ship(size, row, col, direction,
                         boardSize, self.ships)
        self.ships.append(ship)
        return ship.coordinates

    def __init__(self, isEnemy=True, boardSize=6):
        self._boardSize = boardSize
        self._ships = []
        self._shots = [
            [0 for i in range(boardSize)]
            for i in range(boardSize)
        ]

        if isEnemy:
            for _ in range(4):
                self.addShip()
            for _ in range(2):
                self.addShip(2)
            self.addShip(3)

    @property
    def ships(self):
        return self._ships

    @property
    def shots(self):
        return self._shots

    @property
    def size(self):
        return self._boardSize
