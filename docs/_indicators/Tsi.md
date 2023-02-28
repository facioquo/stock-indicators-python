---
title: True Strength Index (TSI)
permalink: /indicators/Tsi/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_tsi**(*quotes, lookback_periods=25,smooth_periods=13, signal_periods=7*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 25* | Number of periods (`N`) for the first EMA.  Must be greater than 0.
| `smooth_periods` | int, *default 13* | Number of periods (`M`) for the second smoothing.  Must be greater than 0.
| `signal_periods` | int, *default 7* | Number of periods (`S`) in the TSI moving average.  Must be greater than or equal to 0.

### Historical quotes requirements

You must have at least `N+M+100` periods of `quotes` to cover the convergence periods.  Since this uses a two EMA smoothing techniques, we recommend you use at least `N+M+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
TSIResults[TSIResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `TSIResults` is just a list of `TSIResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N+M-1` periods will have `None` values since there's not enough data to calculate.
- `signal` will be `None` for all periods if `signal_periods=0`.

> :hourglass: **Convergence warning**: The first `N+M+250` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### TSIResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `tsi` | float, Optional | True Strength Index
| `signal` | float, Optional | Signal line (EMA of TSI)

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

# Calculate 20-period TSI
results = indicators.get_tsi(quotes, 25, 13, 7)
```

## About {{ page.title }}

Created by William Blau, the [True Strength Index](https://en.wikipedia.org/wiki/True_strength_index) is a momentum oscillator that depicts trends in price changes.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/300 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Tsi.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Tsi/Tsi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/tsi.py)
