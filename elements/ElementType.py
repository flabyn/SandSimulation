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

class ElementType(Enum):
    EMPTYCELL = 0
    SAND = 1
    STONE = 2
    COAL = 3
    WATER = 4
    STEAM = 5
    SMOKE = 6
    FIRE = 7

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
                