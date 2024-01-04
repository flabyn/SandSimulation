import pygame as py
import random
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
    
    def DrawAll(self):
        for y in self.Matrix:
            for x in y:
                element = x
                if isinstance(element,EmptyCell):
                    continue
                position = element.position
                py.draw.rect(self.screen,element.colour,(position[0]*self.CellSize,position[1]*self.CellSize,self.CellSize,self.CellSize))
    
    def StepAll(self):
        for y in reversed(self.Matrix):
            row = y.copy()
            random.shuffle(row) #shuffles each row
            for x in row:
                x.step(self)
                #if random.random() < 0.3: #30% change
                    #x.TransferTemp(self)
    
    def DrawAndStepAll(self):
        self.StepAll()
        self.DrawAll()
    

    @property
    def GetMatrix(self) -> list:
        return self.Matrix
    
    def GetElementAtIndex(self,x:int,y:int) -> Element:
        return self.Matrix[y][x]
    
    def SetElementAtIndex(self,x:int,y:int,element:Element) -> None:
        self.Matrix[y][x] = element
    
    def RemoveAndSpawnElement(self,x:int,y:int,element_type:ElementType) -> None:
        element = element_type.MatrixCreateElement(x,y)
        self.SetElementAtIndex(x,y,element)

    def SwapElementsAtIndex(self, pos1,pos2):
        element1 = self.GetElementAtIndex(pos1[0],pos1[1])
        element2 = self.GetElementAtIndex(pos2[0],pos2[1])

        element1.position = [pos2[0],pos2[1]]
        element2.position = [pos1[0],pos1[1]]

        self.SetElementAtIndex(pos1[0],pos1[1],element2)
        self.SetElementAtIndex(pos2[0],pos2[1],element1)

    def DieAndReplace(self,pos,new_element):
        element = ElementType(new_element.value).MatrixCreateElement(pos[0],pos[1])
        self.SetElementAtIndex(pos[0],pos[1],element)
    
    def CellDie(self,pos):
        self.SetElementAtIndex(pos[0],pos[1],ElementType.EMPTYCELL.MatrixCreateElement())

    def Surrounded(self,pos) -> bool:
        if pos[1] == 0 or pos[1] >= self.Matrixsize[1]-1:
            return True
        if pos[0] == 0 or pos[0] >= self.Matrixsize[0]-1:
            return True
        for y in range(-1,2,1):
            for x in range(-1,2,1):
                if isinstance(self.GetElementAtIndex(x+pos[0],y+pos[1]),EmptyCell):
                    return False
        return True
    
    def getSurroundingElements(self,pos,element = EmptyCell) -> list:
        if pos[1] == 0 or pos[1] >= self.Matrixsize[1]-1:
            return True
        if pos[0] == 0 or pos[0] >= self.Matrixsize[0]-1:
            return True
        elements = []
        for y in range(-1,2,1):
            for x in range(-1,2,1):
                if isinstance(self.GetElementAtIndex(x+pos[0],y+pos[1]),element):
                    elements.append((x,y))
        return elements
