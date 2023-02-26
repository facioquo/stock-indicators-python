---
title: Relative Strength Index (RSI)
permalink: /indicators/Rsi/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_rsi**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) in the lookback period.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `10×N` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
RSIResults[RSIResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `RSIResults` is just a list of `RSIResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `10×N` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### RSIResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `rsi` | float, Optional | RSI over prior `N` lookback periods

### Utilities

- ~~[.to_quotes()]({{site.baseurl}}/utilities#convert-to-quotes)~~ <code style='color: #d32f2f; important'>[deprecated]</code>
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate RSI(14)
results = indicators.get_rsi(quotes, 14)
```

## About {{ page.title }}

Created by J. Welles Wilder, the [Relative Strength Index](https://en.wikipedia.org/wiki/Relative_strength_index) measures strength of the winning/losing streak over `N` lookback periods on a scale of 0 to 100, to depict overbought and oversold conditions.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/224 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Rsi.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Rsi/Rsi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/rsi.py)
