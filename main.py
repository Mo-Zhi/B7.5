import PySimpleGUI as sg

sg.theme('DarkAmber')

class Board:
  
class Player:
    ships
    shots
def addShip(rowStart, colStart, rowEnd,colEnd):
    if rowStart != rowEnd and colStart != colEnd:
        sg.Popup('Diagonal ships are not allowed')
     elseif rowStart == rowEnd and colEnd-colStart>2 or
                 colStart == colEnd and rowEnd-rowStart>2
         sg.Popup('Ship is too big')
      


        