import pygame as py
from elements.Element import Element
from elements.ElementType import ElementType

class CellMatrix:
    def __init__(self,cellsize:int,screen,screen_size:list[int]) -> None:
        self.CellSize = cellsize
        self.Matrixsize = [screen_size[0]//cellsize,screen_size[1]//cellsize]
        self.Matrix = self.generateMatrix()


    def generateMatrix(self) -> list: #done in a odd way
        matrix = [['' for _ in range(self.Matrixsize[0])] for _ in range(self.Matrixsize[1])] 

        for y in range(self.Matrixsize[1]):
            for x in range(self.Matrixsize[0]):
                matrix[y][x] = ElementType.EMPTYCELL.MatrixCreateElement(x,y)

        return matrix
    
    def GetMatrix(self) -> list:
        return self.Matrix
