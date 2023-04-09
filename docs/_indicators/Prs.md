---
title: Price Relative Strength (PRS)
permalink: /indicators/Prs/
type: price-characteristic
layout: indicator
---

# {{ page.title }}

<hr>

## **get_prs**(*eval_history, base_history, lookback_periods=None, sma_periods=None*)

## Parameters

| name | type | notes
| -- |-- |--
| `eval_history` | Iterable[Quote] | Historical quotes for evaluation.  You must have the same number of periods as `base_history`. <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `base_history` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `lookback_periods` | int, Optional | Number of periods (`N`) to lookback to compute % difference.  Must be greater than 0 if specified or `None`.
| `sma_periods` | int, Optional | Number of periods (`S`) in the SMA lookback period for `prs`.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `base_history` to calculate `prs_percent` if `lookback_periods` is specified; otherwise, you must specify at least `S+1` periods.  More than the minimum is typically specified.  For this indicator, the elements must match (e.g. the `n`th elements must be the same date).  An `Exception` will be thrown for mismatch dates.  Historical price quotes should have a consistent frequency (day, hour, minute, etc).

`base_history` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
PRSResults[PRSResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `PRSResults` is just a list of `PRSResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The `N` periods will have `None` values for `prs_percent` and the first `S-1` periods will have `None` values for `sma` since there's not enough data to calculate.

### PRSResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `prs` | float, Optional | Price Relative Strength compares `eval_history` to `base_history`
| `prs_sma` | float, Optional | Moving Average (SMA) of PRS over `S` periods
| `prs_percent` | float, Optional | Percent change difference between `eval_history` and `base_history` over `N` periods

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
history_SPX = get_history_from_feed("SPX")
history_TSLA = get_history_from_feed("TSLA")

# Calculate 14-period PRS
results = indicators.get_prs(history_SPX, history_TSLA, 14)
```

## About {{ page.title }}

[Price Relative Strength (PRS)](https://en.wikipedia.org/wiki/Relative_strength), also called Comparative Relative Strength, shows the ratio of two quote histories, based on Close price.  It is often used to compare against a market index or sector ETF.  When using the optional `lookback_periods`, this also returns relative percent change over the specified periods.  This is not the same as the more prevalent [Relative Strength Index (RSI)](../Rsi#content).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/243 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Prs.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Prs/Prs.Series.cs)
- [Python wrapper]({{site.sourceurl}}/prs.py)
