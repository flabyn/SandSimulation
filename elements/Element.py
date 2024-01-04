import random
from elements.ElementTypeShh import ElementType

class Element:
    def __init__(self,x:int,y:int) -> None:
        self.position = [x,y]
        self.colour = (100,100,100)
        self.origanlColour = self.colour
        self.health = 100
        self.velocity = (0,0)
        self.terminal_velocity = 10
        self.friction = 0.001
        self.friction_count = 0
        self.temp = 1
        self.flameresistance = 0
        self.burnrate = 10
        self.fireSpreadRate = 0.2
        self.isIgnited = False
        self.isfreefalling = True
        self.movedthisframe = False
        self.movedlastframe = True


        self.viscosity = 1.0
    def step(self,matrix):
        pass
    
    def handleVelocity(self, matrix, stopingElement):
        #vel = (0,1)
        if self.velocity[1] > 0:
            matrix.SwapElementsAtIndex(self.position,(self.position[0],self.position[1]+self.checkDownVelocityPositions(matrix,stopingElement)))
        elif abs(self.velocity[0]) > 0:
            dir = 0
            if self.velocity[0] > 0: dir = 1
            else: dir = -1
            matrix.SwapElementsAtIndex(self.position,(self.position[0]+self.checkSideVelocityPositions(matrix,stopingElement,dir),self.position[1]))

    def handleVelocityMultiStops(self, matrix, stopingElement1, stopingElement2):
        if self.velocity[1] > 0:
            num = min(self.checkDownVelocityPositions(matrix,stopingElement1),self.checkDownVelocityPositions(matrix,stopingElement2))
            matrix.SwapElementsAtIndex(self.position,(self.position[0],self.position[1]+num))
        elif abs(self.velocity[0]) > 0:
            dir = 0
            if self.velocity[0] > 0: dir = 1
            else: dir = -1
            matrix.SwapElementsAtIndex(self.position,(self.position[0]+self.checkSideVelocityPositions(matrix,stopingElement1,dir),self.position[1]))

    def handleVertVelocity(self, matrix, stopingElement):
        matrix.SwapElementsAtIndex(self.position,(self.position[0],self.position[1]+self.checkDownVelocityPositions(matrix,stopingElement)))

    def handleHorzVelocity(self, matrix, stopingElement):
        if abs(self.velocity[0]) > 0:
            dir = 0
            if self.velocity[0] > 0: dir = 1
            else: dir = -1
            matrix.SwapElementsAtIndex(self.position,(self.position[0]+self.checkSideVelocityPositions(matrix,stopingElement,dir),self.position[1]))

    def checkDownVelocityPositions(self,matrix,stopingElement):
        for i in range(1,self.velocity[1]+1):
            if i + self.position[1] >= matrix.Matrixsize[1]:
                self.velocity = ((self.velocity[1]//4)*random.randint(-1,1),0)
                return i-1
            if isinstance(matrix.GetElementAtIndex(self.position[0],self.position[1]+i),stopingElement):
                dir = -1 if random.random() > 0.5 else 1
                self.velocity = (self.velocity[0]+((self.velocity[1]//4)*dir),0)
                return i-1
        return self.velocity[1]

    def checkSideVelocityPositions(self,matrix,stopingElement,direction:int):
        if self.position[0]+(1*direction) <= 0 or self.position[0]+(1*direction) >= matrix.Matrixsize[0]:
            self.velocity = (0,0)
            return 0
        if isinstance(matrix.GetElementAtIndex(self.position[0]+(1*direction),self.position[1]),stopingElement):
            ele=matrix.GetElementAtIndex(self.position[0]+(1*direction),self.position[1])
            if abs(ele.velocity[0]) + abs(self.velocity[0]) != abs(ele.velocity[0] + self.velocity[0]):
                ele.velocity = (ele.velocity[0]*-1,ele.velocity[1])
                self.velocity = (self.velocity[0]*-1,self.velocity[1])
            #wait untill open space
            self.friction_count += 1
            if self.friction_count >= 100:
                self.velocity = (0,0)
            return 0
        
        if random.random() < self.friction:
            self.velocity = (self.velocity[0]-(1*direction),self.velocity[1])
        return 1*direction

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

    def reciveHeat(self,heat,matrix):
        return None

    def spreadHeat(self,matrix):
        if self.position[1] == 0 or self.position[1] >= matrix.Matrixsize[1]-1:
            return
        if self.position[0] == 0 or self.position[0] >= matrix.Matrixsize[0]-1:
            return

        matrix.GetElementAtIndex(self.position[0]+1,self.position[1]+1).reciveHeat(self.temp,matrix)
        matrix.GetElementAtIndex(self.position[0],self.position[1]+1).reciveHeat(self.temp,matrix)
        matrix.GetElementAtIndex(self.position[0]-1,self.position[1]+1).reciveHeat(self.temp,matrix)

        matrix.GetElementAtIndex(self.position[0]+1,self.position[1]).reciveHeat(self.temp,matrix)
        matrix.GetElementAtIndex(self.position[0]-1,self.position[1]).reciveHeat(self.temp,matrix)

        matrix.GetElementAtIndex(self.position[0]+1,self.position[1]-1).reciveHeat(self.temp,matrix)
        matrix.GetElementAtIndex(self.position[0],self.position[1]-1).reciveHeat(self.temp,matrix)
        matrix.GetElementAtIndex(self.position[0]-1,self.position[1]-1).reciveHeat(self.temp,matrix)


    def lifeStep(self,matrix):
        return None

    def Ignited(self,matrix):
        self.health -= self.burnrate
        if self.health <= 0:
            self.Death(matrix)
        
        self.colour = self.RandomColour((150,random.randrange(10,150,30),10),10)
        if random.random() < self.flameresistance/8:
            self.isIgnited = False
            self.colour = self.DarkenColour(self.origanlColour)
        if surrounded:=matrix.Surrounded(self.position):
            if random.random() < self.flameresistance/2:
                self.isIgnited = False
                self.colour = self.DarkenColour(self.origanlColour)
        if not surrounded:
            if random.random() < self.fireSpreadRate:
                vaildpositions = matrix.getSurroundingElements(self.position)
                pos = random.choice(vaildpositions)
                matrix.DieAndReplace((self.position[0]+pos[0],self.position[1]+pos[1]),ElementType.FIRE)
            elif random.random() < self.fireSpreadRate/5:
                self.spreadHeat(matrix)



    def Death(self,matrix):
        matrix.CellDie(self.position)

    def RandomColour(self,colour,ColourVariation = 30) -> tuple:
        rand = (random.random()-0.5)*ColourVariation
        R = min(max(colour[0] + (rand),0),255)
        G = min(max(colour[1] + (rand),0),255)
        B = min(max(colour[2] + (rand),0),255)
        return (R,G,B)
    
    def DarkenColour(self,colour,Darkness = 50) -> tuple:
        R = max(colour[0]-Darkness,0)
        G = max(colour[1]-Darkness,0)
        B = max(colour[2]-Darkness,0)
        return (R,G,B)
