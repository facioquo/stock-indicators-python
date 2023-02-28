---
title: Weighted Moving Average (WMA)
permalink: /indicators/Wma/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_wma**(*quotes, lookback_periods, candle_part=CandlePart.CLOSE*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.
| `candle_part` | CandlePart, *default CandlePart.CLOSE* | Specify candle part to evaluate.  See [CandlePart options](#candlepart-options) below.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

{% include candlepart-options.md %}

## Return

```python
WMAResults[WMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `WMAResults` is just a list of `WMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### WMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `wma` | float, Optional | Weighted moving average

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import CandlePart     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate 20-period WMA
results = indicators.get_wma(quotes, 20, CandlePart.CLOSE)
```

## About {{ page.title }}

[Weighted Moving Average](https://en.wikipedia.org/wiki/Moving_average#Weighted_moving_average) is the linear weighted average of `close` price over `N` lookback periods.  This also called Linear Weighted Moving Average (LWMA).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/227 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Wma.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Wma/Wma.Series.cs)
- [Python wrapper]({{site.sourceurl}}/wma.py)
