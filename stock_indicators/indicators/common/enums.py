from stock_indicators._cslib import CsCandlePart
from stock_indicators.indicators.common._contrib.enum import ValueEnum

class CandlePart(ValueEnum):
    OPEN = CsCandlePart.Open
    HIGH = CsCandlePart.High
    LOW = CsCandlePart.Low
    CLOSE = CsCandlePart.Close
    VOLUME = CsCandlePart.Volume
