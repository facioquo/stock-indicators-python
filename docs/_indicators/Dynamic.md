---
title: McGinley Dynamic
description: Created by John R. McGinley, the McGinley Dynamic is a more responsive variant of exponential moving average.
permalink: /indicators/Dynamic/
type: moving-average
layout: indicator
---

# {{ page.title }}

><span class="indicator-syntax">**get_dynamic**(*quotes, lookback_periods, k_factor=0.6*)</span>

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [See here]({{site.baseurl}}/guide/#using-pandasdataframe) for usage with pandas.DataFrame</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.
| `k_factor` | float, *default 0.6* | Range adjustment factor (`K`).  Must be greater than 0.

### Historical quotes requirements

You must have at least `2` periods of `quotes`, to cover the initialization periods.  Since this uses a smoothing technique, we recommend you use at least `4×N` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### Pro tips

> Use a `k_factor` value of `1` if you do not want to adjust the `N` value.
>
> McGinley suggests that using a `K` value of 60% (0.6) allows you to use a `N` equivalent to other moving averages.  For example, DYNAMIC(20,0.6) is comparable to EMA(20); conversely, DYNAMIC(20,1) uses the raw 1:1 `N` value and is not equivalent.

## Returns

```python
DynamicResults[DynamicResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `DynamicResults` is just a list of `DynamicResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first period will have a `None` value since there's not enough data to calculate.

>&#9886; **Convergence warning**: The first `4×N` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### DynamicResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `dynamic` | float, Optional | McGinley Dynamic

### Utilities

- [.condense()]({{site.baseurl}}/utilities#condense)
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_historical_quotes("SPY")

# calculate 14-period McGinley Dynamic
results = indicators.get_dynamic(quotes, 14)
```

## About {{ page.title }}

Created by John R. McGinley, the [McGinley Dynamic](https://www.investopedia.com/terms/m/mcginley-dynamic.asp) is a more responsive variant of exponential moving average.
[[Discuss] &#128172;]({{site.dotnet.repo}}/discussions/866 "Community discussion about this indicator")

![chart for {{page.title}}]({{site.dotnet.charts}}/Dynamic.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Dynamic/Dynamic.Series.cs)
- [Python wrapper]({{site.python.src}}/dynamic.py)
