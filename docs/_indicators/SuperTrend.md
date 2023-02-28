---
title: SuperTrend
permalink: /indicators/SuperTrend/
type: price-trend
layout: indicator
---

# {{ page.title }}

<hr>

## **get_super_trend**(*quotes, lookback_periods=10, multiplier=3*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 10* | Number of periods (`N`) for the ATR evaluation.  Must be greater than 1 and is usually set between 7 and 14.
| `multiplier` | float, *default 3* | Multiplier sets the ATR band width.  Must be greater than 0 and is usually set around 2 to 3.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the warmup periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` periods prior to the intended usage date for optimal precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
SuperTrendResults[SuperTrendResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `SuperTrendResults` is just a list of `SuperTrendResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` SuperTrend values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: the line segment before the first reversal and the first `N+100` periods are unreliable due to an initial guess of trend direction and precision convergence for the underlying ATR values.

### SuperTrendResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `super_trend` | Decimal, Optional | SuperTrend line contains both Upper and Lower segments
| `upper_band` | Decimal, Optional | Upper band only (bearish/red)
| `lower_band` | Decimal, Optional | Lower band only (bullish/green)

`upper_band` and `lower_band` values are provided to differentiate bullish vs bearish trends and to clearly demark trend reversal.  `super_trend` is the contiguous combination of both upper and lower line data.

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

# calculate SuperTrend(14,3)
results = indicators.get_super_trend(quotes, 14, 3)
```

## About {{ page.title }}

Created by Oliver Seban, the SuperTrend indicator attempts to determine the primary trend of Close prices by using [Average True Range (ATR)](../Atr#content) band thresholds.
It can indicate a buy/sell signal or a trailing stop when the trend changes.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/235 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/SuperTrend.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/SuperTrend/SuperTrend.Series.cs)
- [Python wrapper]({{site.sourceurl}}/super_trend.py)
