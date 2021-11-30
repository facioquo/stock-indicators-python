---
title: Moving Average Convergence/Divergence (MACD)
permalink: /indicators/Macd/
type: price-trend
layout: indicator
---

# {{ page.title }}
<hr>

## **get_macd**(*quotes, fast_periods=12, slow_periods=26, signal_periods=9*)

[[source]]({{site.sourceurl}}/macd.py)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `fast_periods` | int, *default 12* | Number of periods (`F`) for the faster moving average.  Must be greater than 0.
| `slow_periods` | int, *default 26* | Number of periods (`S`) for the slower moving average.  Must be greater than `fast_periods`.
| `signal_periods` | int, *default 9* | Number of periods (`P`) for the moving average of MACD.  Must be greater than or equal to 0.

### Historical quotes requirements

You must have at least `2×(S+P)` or `S+P+100` worth of `quotes`, whichever is more.  Since this uses a smoothing technique, we recommend you use at least `S+P+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Type[Quote]]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
MACDResults[MACDResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `S-1` slow periods will have `None` values since there's not enough data to calculate.

:hourglass: **Convergence Warning**: The first `S+P+250` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### MacdResult

| name | type | notes
| -- |-- |--
| `date` | DateTime | Date
| `macd` | decimal | The MACD line is the difference between slow and fast moving averages (`macd = fast_ema - slow_ema`)
| `signal` | decimal | Moving average of the `macd` line
| `histogram` | decimal | Gap between of the `macd` and `Signal` line
| `fast_ema` | decimal | Fast Exponential Moving Average
| `slow_ema` | decimal | Slow Exponential Moving Average

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

# calculate MACD(12,26,9)
results = indicators.get_macd(12,26,9);
```

# About: {{ page.title }}

Created by Gerald Appel, [MACD](https://en.wikipedia.org/wiki/MACD) is a simple oscillator view of two converging/diverging exponential moving averages.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/248 "Community discussion about this indicator")

![image]({{site.charturl}}/Macd.png)
