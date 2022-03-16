from stock_indicators._cslib import CsCandlePart, CsSignal, CsEnum
from stock_indicators.indicators.common._contrib.enum import ValueEnum


class CandlePart(ValueEnum):
    OPEN = CsCandlePart.Open
    HIGH = CsCandlePart.High
    LOW = CsCandlePart.Low
    CLOSE = CsCandlePart.Close
    VOLUME = CsCandlePart.Volume


class Signal(ValueEnum):
    BULL_CONFIRMED = CsSignal.BullConfirmed
    BULL_SIGNAL = CsSignal.BullSignal
    BULL_BASIS = CsSignal.BullBasis
    NEUTRAL = CsSignal.Neutral
    NONE = CsEnum.Parse(CsSignal, "None")
    BEAR_BASIS = CsSignal.BearBasis
    BEAR_SIGNAL = CsSignal.BearSignal
    BEAR_CONFIRMED = CsSignal.BearConfirmed
