import pygame as py
from elements.Element import Element
from elements.ElementType import ElementType
from elements.EmptyCell import EmptyCell

class CellMatrix:
    def __init__(self,cellsize:int,screen,screen_size:list[int]) -> None:
        self.screen = screen
        self.CellSize = cellsize
        self.Matrixsize = [screen_size[0]//cellsize,screen_size[1]//cellsize]
        self.Matrix = self.generateMatrix()


    def generateMatrix(self) -> list: #done in a odd way
        matrix = [['' for _ in range(self.Matrixsize[0])] for _ in range(self.Matrixsize[1])] 

        for y in range(self.Matrixsize[1]):
            for x in range(self.Matrixsize[0]):
                matrix[y][x] = ElementType.EMPTYCELL.MatrixCreateElement(x,y)

        return matrix
    
    @property
    def GetMatrix(self) -> list:
        return self.Matrix
    
    def GetElementAtIndex(self,x:int,y:int):
        return self.Matrix[y][x]
    
    def SetElementAtIndex(self,x:int,y:int,element:Element):
        self.Matrix[y][x] = element

    def DrawAll(self):
        for y in self.Matrix:
            for x in y:
                element = x
                if isinstance(element,EmptyCell):
                    continue
                position = element.position
                py.draw.rect(self.screen,element.colour,(position[0]*self.CellSize,position[1]*self.CellSize,self.CellSize,self.CellSize))
                #py.draw.rect(self.screen,element.colour,(position[0]*self.CellSize,10,10,10))
    
    def RemoveAndSpawnElement(self,x:int,y:int):
        element = ElementType.SAND.MatrixCreateElement(x,y)
        self.SetElementAtIndex(x,y,element)
