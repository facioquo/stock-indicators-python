---
title: Klinger Volume Oscillator
permalink: /indicators/Kvo/
type: volume-based
layout: indicator
---

# {{ page.title }}

<hr>

## **get_kvo**(*quotes, fast_periods=34, slow_periods=55, signal_periods=13*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `fast_periods` | int, *default 34* | Number of lookback periods (`F`) for the short-term EMA.  Must be greater than 2.
| `slow_periods` | int, *default 55* | Number of lookback periods (`L`) for the long-term EMA.  Must be greater than `F`.
| `signal_periods` | int, *default 13* | Number of lookback periods for the signal line.  Must be greater than 0.

### Historical quotes requirements

You must have at least `L+100` periods of `quotes` to cover the warmup periods.  Since this uses a smoothing technique, we recommend you use at least `L+150` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
KVOResults[KVOResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `KVOResults` is just a list of `KVOResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `L+1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `L+150` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### KVOResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `oscillator` | float, Optional | Klinger Oscillator
| `signal` | float, Optional | EMA of Klinger Oscillator (signal line)

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

# Calculate Klinger(34,55,13)
results = indicators.get_kvo(quotes, 34, 55, 13)
```

## About {{ page.title }}

Created by Stephen Klinger, the [Klinger Volume Oscillator](https://www.investopedia.com/terms/k/klingeroscillator.asp) depicts volume-based trend reversal and divergence between short and long-term money flow.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/446 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Kvo.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Kvo/Kvo.Series.cs)
- [Python wrapper]({{site.sourceurl}}/kvo.py)
