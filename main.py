import PySimpleGUI as sg

sg.theme('DarkAmber')

class Player:
  
    class Board:
        dimensions
        ships
        shots

        def __init__(self, dimensions=6):
            self.dimensions = dimensions
            shots = [[ 0 for i in range(dimensions)] for i in range(dimensions)]

        def checkCoordinates(size, row, col, direction='row'):
           if direction == 'row':
               for i in range(col):
                   if 
        
        def addShip(size, row, col, direction='row')
            if shots[row][col]:

            else:
                ship = Ship(size, row, col, direction)
                ships.extend(ship.coordinates)
        
        class Ship:
            coordinates

            def __init__(self, size, row, col, direction):
                if direction == 'row':
                    for i in range(size):
                        coordinates.append((row, col + i))
                elif direction == 'col':
                    for i in range(size):
                        coordinates.append((row + i, col))

    

        