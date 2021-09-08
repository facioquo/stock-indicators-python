from enum import IntEnum
from SkenderStockIndicators._cslib import CsCandlePart

class CandlePart(IntEnum):
    OPEN = CsCandlePart.Open
    HIGH = CsCandlePart.High
    LOW = CsCandlePart.Low
    CLOSE = CsCandlePart.Close
    VOLUME = CsCandlePart.Volume