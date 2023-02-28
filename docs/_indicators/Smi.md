---
title: Stochastic Momentum Index (SMI)
permalink: /indicators/Smi/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_smi**(*quotes, lookback_periods, first_smooth_periods, second_smooth_periods, signal_periods=3*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Lookback period (`N`) for the stochastic.  Must be greater than 0.
| `first_smooth_periods` | int | First smoothing factor lookback.  Must be greater than 0.
| `second_smooth_periods` | int | Second smoothing factor lookback.  Must be greater than 0.
| `signal_periods` | int, *default 3* | EMA of SMI lookback periods.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the convergence periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
SMIResults[SMIResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `SMIResults` is just a list of `SMIResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` SMI values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### SMIResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `smi` | float, Optional | Stochastic Momentum Index (SMI)
| `signal` | float, Optional | Signal line: an Exponential Moving Average (EMA) of SMI

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

# Calculate SMI(14,20,5,3)
results = indicators.get_smi(quotes, 14, 20, 5, 3)
```

## About {{ page.title }}

Created by William Blau, the Stochastic Momentum Index (SMI) is a double-smoothed variant of the [Stochastic Oscillator](../Stoch/#content) on a scale from -100 to 100.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/625 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Smi.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Smi/Smi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/smi.py)
