---
title: Arnaud Legoux Moving Average (ALMA)
permalink: /indicators/Alma/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_alma**(*quotes, lookback_periods=9, offset=0.85, sigma=6*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 9* | Number of periods (`N`) in the moving average.  Must be greater than 1, but is typically in the 5-20 range.
| `offset` | float, *default 0.85* | Adjusts smoothness versus responsiveness on a scale from 0 to 1; where 1 is max responsiveness.
| `sigma` | float, *default 6* | Defines the width of the Gaussian [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution).  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
ALMAResults[ALMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ALMAResults` is just a list of `ALMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### ALMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `alma` | float, Optional | Arnaud Legoux Moving Average

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

# calculate Alma
results = indicators.get_alma(quotes, 10, 0.5, 6)
```

### About {{ page.title }}

Created by Arnaud Legoux and Dimitrios Kouzis-Loukas, [ALMA]({{site.dotnet.repo}}/files/5654531/ALMA-Arnaud-Legoux-Moving-Average.pdf) is a Gaussian distribution weighted moving average of Close price over a lookback window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/209 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Alma.png)

#### Sources

- [C# core]({{site.dotnet.src}}/a-d/Alma/Alma.Series.cs)
- [Python wrapper]({{site.sourceurl}}/alma.py)
