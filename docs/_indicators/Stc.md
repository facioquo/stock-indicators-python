---
title: Schaff Trend Cycle
permalink: /indicators/Stc/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_stc**(*quotes, cycle_periods=10, fast_periods=23, slow_periods=50*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `cycle_periods` | int, *default 10* | Number of periods (`C`) for the Trend Cycle.  Must be greater than or equal to 0.
| `fast_periods` | int, *default 23* | Number of periods (`F`) for the faster moving average.  Must be greater than 0.
| `slow_periods` | int, *default 50* | Number of periods (`S`) for the slower moving average.  Must be greater than `fast_periods`.

### Historical quotes requirements

You must have at least `2×(S+C)` or `S+C+100` worth of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `S+C+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
STCResults[STCResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `STCResults` is just a list of `STCResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `S+C` slow periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `S+C+250` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### STCResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `stc` | float, Optional | Schaff Trend Cycle

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

# Calculate STC(12,26,9)
results = indicators.get_stc(quotes, 10, 23, 50)
```

## About {{ page.title }}

Created by Doug Schaff, [Schaff Trend Cycle](https://www.investopedia.com/articles/forex/10/schaff-trend-cycle-indicator.asp) is a stochastic oscillator view of two converging/diverging exponential moving averages (a.k.a MACD).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/570 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Stc.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Stc/Stc.Series.cs)
- [Python wrapper]({{site.sourceurl}}/stc.py)
