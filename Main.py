import pygame as py
from matrix.CellMatrix import CellMatrix
from elements.Element import Element
from elements.EmptyCell import EmptyCell

import time

WIDTH = 500
HEIGHT = 500

py.init()

screen=py.display.set_mode([WIDTH, HEIGHT])


def main_loop():
    matrix = CellMatrix(50,screen=screen,screen_size=[WIDTH,HEIGHT])
    while True:

        #print(matrix.Matrix)
        element = matrix.GetElementAtIndex(x=2,y=3)

        print(element)
        print(element.position)
        print(element.colour)
        print(isinstance(element,EmptyCell))

        matrix.DrawAll()
        py.display.flip() 
        time.sleep(200)

if __name__ == "__main__":
    main_loop()