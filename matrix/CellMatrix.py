import pygame as py

class CellMatrix:
    def __init__(self,cellsize:int,screen,screen_size:list[int]) -> None:
        self.CellSize = cellsize
        self.Matrixsize = [screen_size[0]//cellsize,screen_size[1]//cellsize]
        self.Matrix = self.generateMatrix()


    def generateMatrix(self) -> list:
        matrix = [[0 for _ in range(self.Matrixsize[0])] for _ in range(self.Matrixsize[1])] 
        return matrix
    
    def GetMatrix(self) -> list:
        return self.Matrix
