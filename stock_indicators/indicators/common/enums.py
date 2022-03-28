from stock_indicators._cslib import (
    CsCandlePart, CsSignal, CsEnum, CsBetaType, CsChandelierType, CsMaType,
    CsPivotPointType)
from stock_indicators.indicators.common._contrib.enum import ValueEnum


class BetaType(ValueEnum):
    STANDARD = CsBetaType.Standard
    UP = CsBetaType.Up
    DOWN = CsBetaType.Down
    ALL = CsBetaType.All


class ChandelierType(ValueEnum):
    LONG = CsChandelierType.Long
    SHORT = CsChandelierType.Short


class CandlePart(ValueEnum):
    OPEN = CsCandlePart.Open
    HIGH = CsCandlePart.High
    LOW = CsCandlePart.Low
    CLOSE = CsCandlePart.Close
    VOLUME = CsCandlePart.Volume
    

class MAType(ValueEnum):
    ALMA = CsMaType.ALMA
    DEMA = CsMaType.DEMA
    EPMA = CsMaType.EPMA
    EMA = CsMaType.EMA
    HMA = CsMaType.HMA
    KAMA = CsMaType.KAMA
    MAMA = CsMaType.MAMA
    SMA = CsMaType.SMA
    SMMA = CsMaType.SMMA
    TEMA = CsMaType.TEMA
    WMA = CsMaType.WMA


class PivotPointType(ValueEnum):
    STANDARD = CsPivotPointType.Standard
    CAMARILLA = CsPivotPointType.Camarilla
    DEMARK = CsPivotPointType.Demark
    FIBONACCI = CsPivotPointType.Fibonacci
    WOODIE = CsPivotPointType.Woodie


class Signal(ValueEnum):
    BULL_CONFIRMED = CsSignal.BullConfirmed
    BULL_SIGNAL = CsSignal.BullSignal
    BULL_BASIS = CsSignal.BullBasis
    NEUTRAL = CsSignal.Neutral
    NONE = CsEnum.Parse(CsSignal, "None")
    BEAR_BASIS = CsSignal.BearBasis
    BEAR_SIGNAL = CsSignal.BearSignal
    BEAR_CONFIRMED = CsSignal.BearConfirmed
