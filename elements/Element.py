class Element:
    def __init__(self,x:int,y:int) -> None:
        self.position = [x,y]
        self.colour = (100,100,100)
        self.velocity = (0,0)

        self.viscosity = 1.0
    
    def step(self,matrix):
        pass
    
    def handleVelocity(self,matrix):
        matrix.SwapElementsAtIndex(self.position[0],self.position[1],self.position[0]+self.velocity[0],self.position[1]+self.velocity[1])