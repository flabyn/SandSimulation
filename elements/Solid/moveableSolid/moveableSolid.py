import random
from elements.Solid.Solid import Solid
from elements.EmptyCell import EmptyCell
from elements.Liquid.Liquid import Liquid
class MoveableSolid(Solid):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
    
    def step(self,matrix):
        if self.position[1] == matrix.Matrixsize[1]-1:
            return
        #1 fall if air below
        if self.checkBelow(matrix):
            self.isfreefalling = True
            self.movedthisframe = True
            self.handleVelocity(matrix,Solid)
            self.makeNaboursFreefall(matrix)
            return
        #2 check diagonals
        digon = False
        if self.isfreefalling:
            digon = self.checkDiagonals(matrix)
            if digon:
                self.movedthisframe = True
                self.makeNaboursFreefall(matrix)
            
        if abs(self.velocity[0]) > 0 and not digon:
            self.movedthisframe = True
            self.handleHorzVelocity(matrix,Solid)
            self.makeNaboursFreefall(matrix)

        if not self.movedlastframe:
            self.isfreefalling = False
        

        self.movedlastframe = True if self.movedthisframe else False
        self.movedthisframe = False

    def checkBelow(self,matrix):
        if not isinstance(matrix.GetElementAtIndex(self.position[0],self.position[1]+1),Solid):
            self.velocity = (self.velocity[0],min(self.velocity[1]+1,self.terminal_velocity))
            #self.handleVelocity(matrix,Solid)
            return True
        return False
    def checkDiagonals(self,matrix):
        valid_positions = []
        if self.position[0] < matrix.Matrixsize[0]-1:
            if isinstance(matrix.GetElementAtIndex(self.position[0]+1,self.position[1]+1),EmptyCell):
                valid_positions.append((self.position[0]+1,self.position[1]+1))
        if self.position[0] > 0:
            if isinstance(matrix.GetElementAtIndex(self.position[0]-1,self.position[1]+1),EmptyCell):
                valid_positions.append((self.position[0]-1,self.position[1]+1))
        if len(valid_positions)>0:
            matrix.SwapElementsAtIndex(self.position,random.choice(valid_positions))
            return True
        return False

    def makeNaboursFreefall(self,matrix):
        if self.position[0]-1 <= 0 or self.position[0]+1 >= matrix.Matrixsize[0]:
            return
        if isinstance(ele:=matrix.GetElementAtIndex(self.position[0]+1,self.position[1]),MoveableSolid):
            if random.random() > ele.friction:
                ele.isfreefalling = True
                ele.movedlastframe = True
                ele.movedthisframe = True
        if isinstance(ele:=matrix.GetElementAtIndex(self.position[0]-1,self.position[1]),MoveableSolid):
            if random.random() > ele.friction:
                ele.isfreefalling = True
                ele.movedlastframe = True
                ele.movedthisframe = True