---
title: Exponential Moving Average (EMA)
permalink: /indicators/Ema/
type: moving-average
layout: indicator
---

# {{ page.title }}
<hr>

## **get_ema**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.

<!-- | `candlePart` | CandlePart | Optional.  Specify the [OHLCV]({{site.baseurl}}/guide/#historical-quotes) candle part to evaluate.  See [CandlePart options](#candlepart-options) below.  Default is `CandlePart.Close` -->

### Historical quotes requirements

You must have at least `2×N` or `N+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

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
EMAResults[EMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

:hourglass: **Convergence Warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### EMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `ema` | Decimal, Optional | Exponential moving average

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

# calculate 20-period EMA
results = indicators.get_ema(quotes, 20)
```

### About: {{ page.title }}

[Exponentially weighted moving average](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average) price over a lookback window.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/256 "Community discussion about this indicator")

![image]({{site.charturl}}/Ema.png)

EMA is shown as the solid line above.  Double EMA (dashed line) and Triple EMA (dotted line) are also shown here for comparison.

#### Sources

- [C# core]({{site.base_sourceurl}}/e-k/Ema/Ema.cs)
- [Python wrapper]({{site.sourceurl}}/ema.py)
