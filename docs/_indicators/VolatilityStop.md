---
title: Volatility Stop
permalink: /indicators/VolatilityStop/
type: stop-and-reverse
layout: indicator
---

# {{ page.title }}

<hr>

## **get_volatility_stop**(*quotes, lookback_periods=7, multiplier=3*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 7* | Number of periods (`N`) ATR lookback window.  Must be greater than 1.
| `multiplier` | float, *default 3* | ATR multiplier for the offset.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the convergence periods.  Since the underlying ATR uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.  Initial values prior to the first reversal are not accurate and are excluded from the results.  Therefore, provide sufficient quotes to capture prior trend reversals.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
VolatilityStopResults[VolatilityStopResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `VolatilityStopResults` is just a list of `VolatilityStopResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first trend will have `None` values since it is not accurate and based on an initial guess.

:hourglass: **Convergence Warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### VolatilityStopResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sar` | float, Optional | Stop and Reverse value contains both Upper and Lower segments
| `is_stop` | bool, Optional | Indicates a trend reversal
| `upper_band` | float, Optional | Upper band only (bearish/red)
| `lower_band` | float, Optional | Lower band only (bullish/green)

`upper_band` and `lower_band` values are provided to differentiate bullish vs bearish trends and to clearly demark trend reversal.  `sar` is the contiguous combination of both upper and lower line data.

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

# Calculate VolatilityStop(20,2.5)
results = indicators.get_volatility_stop(quotes, 20, 2.5)
```

## About {{ page.title }}

Created by J. Welles Wilder, [Volatility Stop](https://archive.org/details/newconceptsintec00wild), also known his Volatility System, is an [ATR](../Atr/) based indicator used to determine trend direction, stops, and reversals.  It is similar to Wilder's [Parabolic SAR](../ParabolicSar/#content) and [SuperTrend](../SuperTrend/#content).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/564 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/VolatilityStop.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/VolatilityStop/VolatilityStop.Series.cs)
- [Python wrapper]({{site.sourceurl}}/volatility_stop.py)
