from enum import Enum

from elements.Element import Element
from elements.EmptyCell import EmptyCell
from elements.Solid.moveableSolid.Sand import Sand
from elements.Solid.ImmovableSolid.Stone import Stone
from elements.Liquid.Water import Water
from elements.Gas.Steam import Steam
from elements.Gas.Smoke import Smoke
from elements.Solid.moveableSolid.Coal import Coal
from elements.Gas.Fire import Fire
from elements.Solid.ImmovableSolid.Wood import Wood

class ElementType(Enum):
    EMPTYCELL = 0
    SAND = 1
    STONE = 2
    WOOD = 3
    COAL = 4
    WATER = 5
    STEAM = 6
    SMOKE = 7
    FIRE = 8

    def MatrixCreateElement(self,x:int=1,y:int=1) -> Element:
        match self:
            case ElementType.EMPTYCELL:
                cell = EmptyCell(x,y)
                return cell
            case ElementType.SAND:
                cell = Sand(x,y)
                return cell 
            case ElementType.STONE:
                cell = Stone(x,y)
                return cell
            case ElementType.WOOD:
                cell = Wood(x,y)
                return cell
            case ElementType.COAL:
                cell = Coal(x,y)
                return cell
            case ElementType.WATER:
                cell = Water(x,y)
                return cell
            case ElementType.STEAM:
                cell = Steam(x,y)
                return cell
            case ElementType.SMOKE:
                cell = Smoke(x,y)
                return cell
            case ElementType.FIRE:
                cell = Fire(x,y)
                return cell
                