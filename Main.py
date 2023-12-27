import pygame as py
from matrix.CellMatrix import CellMatrix
from elements.Element import Element
from elements.EmptyCell import EmptyCell

from pygame.locals import *
import time

WIDTH = 500
HEIGHT = 500
CELLSIZE = 5
FPS = 100


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
        position = py.mouse.get_pos()
        cellpos = (position[0]//CELLSIZE,position[1]//CELLSIZE)
        matrix.RemoveAndSpawnElement(cellpos[0],cellpos[1])

def main_loop():
    matrix = CellMatrix(CELLSIZE,screen=screen,screen_size=[WIDTH,HEIGHT])
    while True:
        start = time.time()
        screen.fill((0,0,0))

        EventHandler()
        Spawner(matrix)

        #print(matrix.Matrix)
        #element = matrix.GetElementAtIndex(x=2,y=3)

        #print(element)
        #print(element.position)
        #print(element.colour)
        #print(isinstance(element,EmptyCell))

        matrix.DrawAndStepAll()
        end = time.time()
        total_time = end-start
        font = py.font.Font(None, 24)
        text = font.render(f"Fps:{round(1/max(total_time,1/FPS))}", True, (100, 100, 100))
        screen.blit(text, (10,10))
        py.display.flip() 
        time.sleep(max(0,(1/FPS)-total_time))

if __name__ == "__main__":
    main_loop()