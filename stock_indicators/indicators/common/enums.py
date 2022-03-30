from stock_indicators._cslib import (
    CsCandlePart, CsSignal, CsEnum, CsBetaType, CsChandelierType, CsMaType,
    CsPivotPointType, CsPeriodSize, CsEndType, CsPivotTrend)
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


class EndType(ValueEnum):
    CLOSE = CsEndType.Close
    HIGH_LOW = CsEndType.HighLow


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


class PeriodSize(ValueEnum):
    MONTH = CsPeriodSize.Month
    WEEK = CsPeriodSize.Week
    DAY = CsPeriodSize.Day
    FOUR_HOURS = CsPeriodSize.FourHours
    TWO_HOURS = CsPeriodSize.TwoHours
    ONE_HOUR = CsPeriodSize.OneHour
    THIRTY_MINUTES = CsPeriodSize.ThirtyMinutes
    FIFTEEN_MINUTES = CsPeriodSize.FifteenMinutes
    FIVE_MINUTES = CsPeriodSize.FiveMinutes
    THREE_MINUTES = CsPeriodSize.ThreeMinutes
    TWO_MINUTES = CsPeriodSize.TwoMinutes
    ONE_MINUTE = CsPeriodSize.OneMinute


class PivotPointType(ValueEnum):
    STANDARD = CsPivotPointType.Standard
    CAMARILLA = CsPivotPointType.Camarilla
    DEMARK = CsPivotPointType.Demark
    FIBONACCI = CsPivotPointType.Fibonacci
    WOODIE = CsPivotPointType.Woodie


class PivotTrend(ValueEnum):
    HH = CsPivotTrend.HH
    LH = CsPivotTrend.LH
    HL = CsPivotTrend.HL
    LL = CsPivotTrend.LL


class Signal(ValueEnum):
    BULL_CONFIRMED = CsSignal.BullConfirmed
    BULL_SIGNAL = CsSignal.BullSignal
    BULL_BASIS = CsSignal.BullBasis
    NEUTRAL = CsSignal.Neutral
    NONE = CsEnum.Parse(CsSignal, "None")
    BEAR_BASIS = CsSignal.BearBasis
    BEAR_SIGNAL = CsSignal.BearSignal
    BEAR_CONFIRMED = CsSignal.BearConfirmed
