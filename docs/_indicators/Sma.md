---
title: Simple Moving Average (SMA)
permalink: /indicators/Sma/
type: moving-average
layout: indicator
---

# {{ page.title }}
<hr>

## **get_sma**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `lookback_periods` | int | Number of periods (`N`) in the lookback window.  Must be greater than 0.

<!-- | `candlePart` | CandlePart | Optional.  Specify the [OHLCV]({{site.baseurl}}/guide/#historical-quotes) candle part to evaluate.  See [CandlePart options](#candlepart-options) below.  Default is `CandlePart.Close` -->

### Historical quotes requirements

You must have at least `N` periods of `quotes`.

`quotes` is an `Iterable[Type[Quote]]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

<!-- 
### CandlePart options

| type | description
|-- |--
| `CandlePart.Open` | Use `Open` price
| `CandlePart.High` | Use `High` price
| `CandlePart.Low` | Use `Low` price
| `CandlePart.Close` | Use `Close` price (default)
| `CandlePart.Volume` | Use `Volume` -->

## Returns

```python
SMAResults[SMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### SMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime.datetime | Date
| `sma` | decimal.Decimal | Simple moving average

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate 20-period SMA
results = indicators.get_sma(quotes, 20)
```


<hr>
# Extended analysis

An extended variant of this indicator includes additional analysis.

## **get_sma_extended**(*quotes, lookback_periods*)
    
[[source]]({{site.sourceurl}}/sma.py)


## Returns

### SmaExtendedResult

| name | type | notes
| -- |-- |--
| `date` | datetime.datetime | Date
| `sma` | decimal.Decimal | Simple moving average
| `mad` | decimal.Decimal | Mean absolute deviation
| `mse` | decimal.Decimal | Mean square error
| `mape` | decimal.Decimal | Mean absolute percentage error

## Example

```python
# usage
results = indicators.get_sma_extended(quotes, lookbackPeriods)
```


## About: {{ page.title }}

[Simple Moving Average](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average) is the average price over a lookback window.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/240 "Community discussion about this indicator")

![image]({{site.charturl}}/Sma.png)

### Sources

- [C# core]({{site.base_sourceurl}}/s-z/Sma/Sma.cs)
- [Python wrapper]({{site.sourceurl}}/sma.py)
