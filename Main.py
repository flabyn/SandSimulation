import pygame as py
from matrix.CellMatrix import CellMatrix
from elements.Element import Element
from elements.EmptyCell import EmptyCell

from pygame.locals import *
import time

WIDTH = 500
HEIGHT = 500
CELLSIZE = 50

user_holding_mouse = False

py.init()

screen=py.display.set_mode([WIDTH, HEIGHT])

def EventHandler():
    global user_holding_mouse
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
        
        if event.type == MOUSEBUTTONDOWN:
            user_holding_mouse = True
        if event.type == MOUSEBUTTONUP:
            user_holding_mouse = False

def Spawner(matrix:CellMatrix):
    if user_holding_mouse:
        print("here")
        position = py.mouse.get_pos()
        cellpos = (position[0]//CELLSIZE,position[1]//CELLSIZE)
        print(cellpos)
        matrix.RemoveAndSpawnElement(cellpos[0],cellpos[1])

def main_loop():
    matrix = CellMatrix(CELLSIZE,screen=screen,screen_size=[WIDTH,HEIGHT])
    while True:
        EventHandler()
        Spawner(matrix)

        #print(matrix.Matrix)
        element = matrix.GetElementAtIndex(x=2,y=3)

        print(element)
        #print(element.position)
        #print(element.colour)
        #print(isinstance(element,EmptyCell))

        matrix.DrawAll()
        py.display.flip() 
        time.sleep(0.3)

if __name__ == "__main__":
    main_loop()