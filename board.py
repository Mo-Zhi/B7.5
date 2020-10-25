import random


class Board:

    class Ship:

        def __init__(self, row, col, size, direction='row'):
            """Contains coordinates of cells it occupies and adds a new ship to the array of ships."""
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

    def addShip(self, size=1, row=-1, col=-1, direction='row'):

        if row == col == -1:
            row = random.randint(0, self._boardSize-1)
            col = random.randint(0, self._boardSize - 1)
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
