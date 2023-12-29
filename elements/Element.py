import random
class Element:
    def __init__(self,x:int,y:int) -> None:
        self.position = [x,y]
        self.colour = (100,100,100)
        self.velocity = (0,0)
        self.temp = 1

        self.viscosity = 1.0
    
    def step(self,matrix):
        pass
    
    def handleVelocity(self,matrix):
        matrix.SwapElementsAtIndex(self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])
    
    def TransferTemp(self,matrix):
        if self.position[1] == 0 or self.position[1] >= matrix.Matrixsize[1]-1:
            return
        if self.position[0] == 0 or self.position[0] >= matrix.Matrixsize[0]-1:
            return

        e1 = matrix.GetElementAtIndex(self.position[0],self.position[1]-1)
        e2 = matrix.GetElementAtIndex(self.position[0],self.position[1]+1)
        e3 = matrix.GetElementAtIndex(self.position[0]-1,self.position[1])
        e4 = matrix.GetElementAtIndex(self.position[0]+1,self.position[1])
    
        avg_temp = int((e1.temp + e2.temp + e3.temp + e4.temp + self.temp)/5)

        e1.temp = avg_temp
        e2.temp = avg_temp
        e3.temp = avg_temp
        e4.temp = avg_temp
        self.temp = avg_temp

    def RandomColour(self,colour):
        rand = (random.random()-0.5)*30
        R = min(max(colour[0] + (rand),0),255)
        G = min(max(colour[1] + (rand),0),255)
        B = min(max(colour[2] + (rand),0),255)
        return (R,G,B)
