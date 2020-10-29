from PySimpleGUI import PySimpleGUI as sg
from Player import Player
import random

sg.theme('DarkAmber')
boardSize = 6
player = Player(False)
enemy = Player()

buttonDirection = [sg.Text('Direction:', key='-TEXT-DIRECTION-'),
                   sg.Button('Row', key='-DIRECTION-')]
leftBoard = [
    [sg.Button(size=(1, 1), key=f'-SHIP{i}{j}-')
     for j in range(boardSize)] for i in range(boardSize)
]
rightBoard = [
    [sg.Button(size=(1, 1), key=f'-SHOT{i}{j}-', disabled=True)
     for j in range(boardSize)] for i in range(boardSize)
]
layout = [
    buttonDirection,
    [sg.Column(leftBoard),
     sg.VerticalSeparator(),
     sg.Column(rightBoard)]
]
window = sg.Window('Sea Battle', layout)


def updateButton(event, buttonColor=('black', 'black'), isDisabled=True):
    """Changes state of the button: color and/or is it disabled"""
    if buttonColor == None:
        window[event].update(disabled=isDisabled)
    else:
        window[event].update(disabled=isDisabled, button_color=buttonColor)


def makeAShot(oneBeingShot, event=None):
    """Handles effects of shots"""
#   If the event is 'None' then the one shooting is the computer,
#       so the coordinates of the shot will be random. If they are duplicates,
#       they are picked again
    if event == None:
        while True:
            wasShotBefore = False
            row, col = random.randint(
                0, boardSize - 1), random.randint(0, boardSize - 1)
            if len(oneBeingShot.shots) > 0:
                for shot in oneBeingShot.shots:
                    if row == shot[0] and col == shot[1]:
                        wasShotBefore = True
                        break
            if not wasShotBefore:
                break
        oneBeingShot.shots.append((row, col))
        event = '-SHIP'+str(row)+str(col)+'-'
    else:
        row, col = int(event[5]), int(event[6])

#   If the cell is occupied, change it to grey
#       If not, change it to white
    cellIsOccupied = False
    for ship in oneBeingShot.ships:
        if cellIsOccupied:
            break
        for coordinates in ship.coordinates:
            if row == coordinates[0] and col == coordinates[1]:
                cellIsOccupied = True
                oneBeingShot.occupiedCells = -1
                break
    if cellIsOccupied:
        updateButton(event, ('grey', 'grey'), True)
    else:
        updateButton(event, ('white', 'white'), True)

#   If some player has no ships left, game is over
#       and all buttons are disabled
    if oneBeingShot.occupiedCells == 0:
        if oneBeingShot.isEnemy:
            sg.popup('Enemy has no ships left, you win')
        else:
            sg.popup('You have no ships left, you lost')

        for i in range(boardSize):
            for j in range(boardSize):
                updateButton(f'-SHOT{i}{j}-', None, True)


# event handler
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

#   If button on top is pressed
    elif event == '-DIRECTION-':
        player.changeDirection()
        window[event].update(player.direction)

#   If a button on the left board is pressed
    elif event[1:5] == 'SHIP':
        row = int(event[5])
        col = int(event[6])
        shipsAmount = len(player.ships)

#       Adding ships based on how many ships you already have
        if shipsAmount < 4:
            try:
                player.addShip(1, row, col)
            except Exception as e:
                sg.popup(str(e))
            else:
                updateButton(event)
        elif shipsAmount < 6:
            try:
                coordinates = player.addShip(2, row, col)
            except Exception as e:
                sg.popup(str(e))
            else:
                for i in range(len(coordinates)):
                    updateButton(event[:5] + str(coordinates[i][0]) + str(
                        coordinates[i][1]) + '-')
        elif shipsAmount == 6:
            try:
                coordinates = player.addShip(3, row, col)
            except Exception as e:
                sg.popup(str(e))
            else:
                for i in range(len(coordinates)):
                    updateButton(event[:5] + str(coordinates[i][0]) + str(
                        coordinates[i][1]) + '-')
                for i in range(boardSize):
                    for j in range(boardSize):
                        updateButton(f'-SHIP{i}{j}-', None, True)
                        updateButton(f'-SHOT{i}{j}-', None, False)

    # If a button on the right board is pressed
    elif event[1:5] == 'SHOT':
        makeAShot(enemy, event)
        makeAShot(player)


window.close()
