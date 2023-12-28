import pygame as py
from matrix.CellMatrix import CellMatrix
from elements.Element import Element
from elements.EmptyCell import EmptyCell
from elements.ElementType import ElementType

from pygame.locals import *
import time

WIDTH = 500
HEIGHT = 500
CELLSIZE = 5
FPS = 100

game_paused = False
frame_step = False

py.init()

screen=py.display.set_mode([WIDTH, HEIGHT])

class Spawner:
    def __init__(self) -> None:
        self.brushsize = 1
        self.element = 1
        self.user_holding_mouse = False

    def step(self,matrix):
        if self.user_holding_mouse:

            element = ElementType(self.element)

            position = py.mouse.get_pos()
            for y in range(self.brushsize):
                y_pos = y+(position[1]//CELLSIZE)
                if y_pos<0 or y_pos>(HEIGHT//CELLSIZE-1):
                    continue
                for x in range(self.brushsize):
                    x_pos = x+(position[0]//CELLSIZE)
                    if x_pos<0 or x_pos>(WIDTH//CELLSIZE-1):
                        continue
                    cellpos = (x_pos,y_pos)
                    matrix.RemoveAndSpawnElement(cellpos[0],cellpos[1],element)


def EventHandler(spawner:Spawner):
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
        
        if event.type == MOUSEBUTTONDOWN:
            spawner.user_holding_mouse = True
        if event.type == MOUSEBUTTONUP:
            spawner.user_holding_mouse = False
        if event.type == MOUSEWHEEL: #up = +y down = -y
            spawner.brushsize = max(spawner.brushsize+event.y,1)
        if event.type == KEYDOWN:
            if event.key == 32:#space bar 
                global game_paused
                game_paused = True if game_paused==False else False
            if event.key == 102:# f
                global frame_step
                frame_step = True
            if event.key == 45:#-
                spawner.element = max(0,spawner.element-1)
            if event.key == 61:#+
                spawner.element += 1
            if event.key >= 48 and event.key <= 57:
                spawner.element = int(event.unicode)
            

def HUD(total_time:float,spawner:Spawner):
    font = py.font.Font(None, 24)
    text = font.render(f"Fps:{round(1/max(total_time,1/FPS))}", True, (100, 100, 100))
    screen.blit(text, (10,10))

    text = font.render(f"Element: {ElementType(spawner.element).name}", True, (100, 100, 100))
    screen.blit(text, (10,30))

    py.display.flip() 


def main_loop():
    global frame_step
    spawner = Spawner()
    matrix = CellMatrix(CELLSIZE,screen=screen,screen_size=[WIDTH,HEIGHT])

    def main_loop_logic():
            matrix.DrawAndStepAll()

    while True:
        start = time.time()
        screen.fill((0,0,0))

        EventHandler(spawner)
        spawner.step(matrix)
        if not game_paused:
            main_loop_logic()
        elif frame_step:
            main_loop_logic()
            frame_step = False
        else:
            matrix.DrawAll()
        
        end = time.time()
        total_time = end-start

        HUD(total_time,spawner)
        time.sleep(max(0,(1/FPS)-total_time))
        



if __name__ == "__main__":
    main_loop()