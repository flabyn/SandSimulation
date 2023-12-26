import pygame as py
from matrix.CellMatrix import CellMatrix
from elements.Element import Element

import time

WIDTH = 500
HEIGHT = 500

py.init()

screen=py.display.set_mode([WIDTH, HEIGHT])


def main_loop():
    matrix = CellMatrix(50,screen=screen,screen_size=[WIDTH,HEIGHT])
    matrix.Matrix[1][0] = 1
    while True:

        print(matrix.GetMatrix())




        time.sleep(2)
        py.display.flip()

if __name__ == "__main__":
    main_loop()