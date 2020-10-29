import random


class Player:
    """A Player contains all information about his side of the game"""
    _boardSize = 0

    class Ship:
        """A Ship has coordinates of its cells."""

        def checkCoordinates(self, row, col, ships):
            """Checks if a ship can be placed on this cell"""
            if len(ships) > 0:
                for ship in ships:
                    for coordinates in ship.coordinates:
                        if row == coordinates[0] and col == coordinates[1]:
                            raise Exception(
                                'A ship cannot be placed on occupied cells.')
                        if (row == coordinates[0] and abs(col - coordinates[1]) < 2) or (abs(row-coordinates[0]) < 2 and col == coordinates[1]):
                            raise Exception('Other ship is too close')
            if row < 0 or row > self.boardSize-1 or col < 0 or col > self.boardSize-1:
                raise Exception(
                    'The ship is not entirely inside of the board.')

            return True

        def __init__(self, size=1, row=-1, col=-1, direction='',
                     boardSize=6, ships=[]):

            self._boardSize = boardSize
            self._direction = direction
            self._coordinates = []
            tempCoordinates = []

#           Picking random coordinates and the direction if it is enemy's ship
            if direction == '':
                while True:
                    row = random.randint(0, boardSize-1)
                    col = random.randint(0, boardSize-1)
                    try:
                        self.checkCoordinates(row, col, ships)
                    except:
                        continue
                    else:
                        if random.randint(0, 1) == 0:
                            direction = 'Row'
                        else:
                            direction = 'Column'
                        break
            if direction == 'Row':
                for i in range(size):
                    if self.checkCoordinates(row, col+i, ships):
                        tempCoordinates.append((row, col + i))
            elif direction == 'Column':
                for i in range(size):
                    if self.checkCoordinates(row + i, col, ships):
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

    def addShip(self, size=1, row=-1, col=-1, boardSize=6):
        """Adds a new ship to the array of player's ships and returns its coordinates as an array of tuples"""

        ship = self.Ship(size, row, col, self.direction,
                         boardSize, self.ships)
        self.ships.append(ship)
        return ship.coordinates

    def changeDirection(self):
        '''Changes direction from \'Row\' to \'Column\''''
        if self._direction == 'Row':
            self._direction = 'Column'
        else:
            self._direction = 'Row'

    def __init__(self, isEnemy=True, boardSize=6):
        self._boardSize = boardSize
        self._occupiedCells = 11
        self._isEnemy = isEnemy
        self._direction = 'Row'
        self._ships = []
        self._shots = []

        if isEnemy:
            self._direction = ''
            while True:
                try:
                    for _ in range(4):
                        self.addShip()
                    for _ in range(2):
                        self.addShip(2)
                    self.addShip(3)
                except:
                    self.ships.clear()
                    continue
                else:
                    break

    @property
    def ships(self):
        return self._ships

    @property
    def direction(self):
        return self._direction

    @property
    def isEnemy(self):
        return self._isEnemy

    @property
    def shots(self):
        return self._shots

    @property
    def size(self):
        return self._boardSize

    @property
    def occupiedCells(self):
        return self._occupiedCells

    @occupiedCells.setter
    def occupiedCells(self, value):
        self._occupiedCells += value
