import random


class Board:
    """A Board has size, an array of player's ships and an array of player's"""
    _boardSize = 0

    class Ship:
        """A Ship has coordinates of its cells."""

        def __init__(self, row, col, size, direction='row'):

            self._coordinates = []
            if direction == 'row':
                for i in range(size):
                    self._coordinates.append((row, col + i))
            elif direction == 'column':
                for i in range(size):
                    self._coordinates.append((row + i, col))

        @property
        def coordinates(self):
            return self._coordinates

    def checkCoordinates(self, size, row, col, direction):
        for tempShip in self.ships:
            for coordinates in tempShip.coordinates:
                if row == coordinates[0] and col == coordinates[1]:
                    return True
        if row < 0 or row > self.size or col < 0 or col > self.size:
            return True

        return False

    def addShip(self, size=1, row=-1, col=-1, direction='row'):
        """Adds new Ship to the array of Ships"""
        if row == col == -1:
            while True:
                row = random.randint(0, self._boardSize-1)
                col = random.randint(0, self._boardSize-1)
                if self.checkCoordinates(size, row, col, direction):
                    continue
                break
        if self.checkCoordinates(size, row, col, direction):
            raise Exception("Invalid cell")
        ship = self.Ship(row, col, size, direction)
        self.ships.append(ship)
        return ship.coordinates

    def __init__(self, isEnemy=True, boardSize=6):
        self._boardSize = boardSize
        self._ships = []
        self._shots = [[0 for i in range(boardSize)]
                       for i in range(boardSize)]

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
