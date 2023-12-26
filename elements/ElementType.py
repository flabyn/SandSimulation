from enum import Enum

from elements.Element import Element
from elements.EmptyCell import EmptyCell
from elements.Sand import Sand

class ElementType(Enum):
    EMPTYCELL = 0
    SAND = 1

    @property
    def MatrixCreateElement(self,x:int=1,y:int=1) -> Element:
        match self:
            case ElementType.EMPTYCELL:
                cell = EmptyCell(x,y)
                return cell
            case ElementType.SAND:
                cell = Sand(x,y)
                return cell