---
title: Slope and Linear Regression
permalink: /indicators/Slope/
type: numerical-analysis
layout: indicator
---

# {{ page.title }}

<hr>

## **get_slope**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) for the linear regression.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
SlopeResults[SlopeResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `SlopeResults` is just a list of `SlopeResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values for `slope` since there's not enough data to calculate.

> :paintbrush: **Repaint Warning**: the `line` will be continuously repainted since it is based on the last quote and lookback period.

### SlopeResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `slope` | float, Optional | Slope `m` of the best-fit line of Close price
| `intercept` | float, Optional | Y-Intercept `b` of the best-fit line
| `stdev` | float, Optional | Standard Deviation of Close price over `N` lookback periods
| `r_squared` | float, Optional | R-Squared (R&sup2;), aka Coefficient of Determination
| `line` | Decimal, Optional | Best-fit line `y` over the last 'N' periods (i.e. `y=mx+b` using last period values)

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

# calculate 20-period Slope
results = indicators.get_slope(quotes, 20)
```

## About {{ page.title }}

[Slope of the best fit line](https://school.stockcharts.com/doku.php?id=technical_indicators:slope) is determined by an [ordinary least-squares simple linear regression](https://en.wikipedia.org/wiki/Simple_linear_regression) on Close price.  It can be used to help identify trend strength and direction.  Standard Deviation, R&sup2;, and a best-fit `Line` (for last lookback segment) are also output.  See also [Standard Deviation Channels](../StdDevChannels#content) for an alternative depiction.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/241 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Slope.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Slope/Slope.Series.cs)
- [Python wrapper]({{site.sourceurl}}/slope.py)
