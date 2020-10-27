from PySimpleGUI import PySimpleGUI as sg
from Board import Board

sg.theme('DarkAmber')

boardSize = 6
player = Board(False)
enemy = Board()
leftText = [
    [sg.Text('TEXT', key='-TEXT-SHIPS-')]
]
leftBoard = [
    [sg.Button(size=(1, 1), key=f'-SHIP{i}{j}-')
     for j in range(boardSize)] for i in range(boardSize)
]
leftColumn = leftText + leftBoard
rightText = [
    [sg.Text('TEXT', key='-TEXT-SHOTS-')]
]
rightBoard = [
    [sg.Button(size=(1, 1), key=f'-SHOT{i}{j}-')
     for j in range(boardSize)] for i in range(boardSize)
]
rightColumn = rightText + rightBoard
layout = [
    [sg.Column(leftColumn),
     sg.VerticalSeparator(),
     sg.Column(rightColumn)]
]
window = sg.Window('Sea Battle', layout)


def updateButton(event, buttonColor=('black', 'black'), isDisabled=True):

    if buttonColor == None:
        window[event].update(disabled=isDisabled)
    else:
        window[event].update(disabled=isDisabled, button_color=buttonColor)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    elif event[1:5] == 'SHIP':
        row = int(event[5])
        col = int(event[6])
        shipsAmount = len(player.ships)

        if shipsAmount < 4:
            try:
                player.addShip(1, row, col, 'row')
            except Exception as e:
                sg.popup(str(e))
            else:
                updateButton(event)

        elif shipsAmount < 6:
            try:
                coordinates = player.addShip(2, row, col, 'row')
            except Exception as e:
                sg.popup(str(e))
            else:
                for i in range(len(coordinates)):
                    updateButton(event[:5] + str(coordinates[i][0]) + str(
                        coordinates[i][1]) + '-')

        elif shipsAmount == 6:
            try:
                coordinates = player.addShip(3, row, col, 'row')
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

    elif event[1:5] == 'SHOT':
        row, col = int(event[5]), int(event[6])
        cellIsOccupied = False
        for tempShip in enemy.ships:
            if cellIsOccupied:
                break
            for coordinates in tempShip.coordinates:
                if row == coordinates[0] and col == coordinates[1]:
                    cellIsOccupied = True
                    enemy.occupiedCells = -1
                    break

        if cellIsOccupied:
            updateButton(event, ('grey', 'grey'), True)
        else:
            updateButton(event, ('white', 'white'), True)

        if enemy.occupiedCells == 0:
            sg.popup('Enemy has no ships left, you win')


window.close()
