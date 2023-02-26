---
title: Correlation Coefficient
description: Correlation Coefficient and R-Squared (Coefficient of Determination)
permalink: /indicators/Correlation/
type: numerical-analysis
layout: indicator
---

# {{ page.title }}

<hr>

## **get_correlation**(*quotes_a, quotes_b, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes_a` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `quotes_b` | Iterable[Quote] | Historical quotes (B) must have at least the same matching date elements of `quotes_a`.
| `lookback_periods` | int | Number of periods (`N`) in the lookback period.  Must be greater than 0 to calculate; however we suggest a larger period for statistically appropriate sample size.

### Historical quotes requirements

You must have at least `N` periods for both versions of `quotes` to cover the warmup periods.  Mismatch histories will produce a `InvalidQuotesException`.  Historical price quotes should have a consistent frequency (day, hour, minute, etc).

`quotes_a` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
CorrelationResults[CorrelationResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `CorrelationResults` is just a list of `CorrelationResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### CorrelationResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `variance_a` | float, Optional | Variance of A based on `N` lookback periods
| `variance_b` | float, Optional | Variance of B based on `N` lookback periods
| `covariance` | float, Optional | Covariance of A+B based on `N` lookback periods
| `correlation` | float, Optional | Correlation `R` based on `N` lookback periods
| `r_squared` | float, Optional | R-Squared (R&sup2;), aka Coefficient of Determination.  Simple linear regression models is used (square of Correlation).

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes_spx = get_history_from_feed("SPX")
quotes_tsla = get_history_from_feed("TSLA")

# Calculate 20-period Correlation
results = indicators.get_correlation(quotes_spx, quotes_tsla, 20)
```

## About {{ page.title }}

[Correlation Coefficient](https://en.wikipedia.org/wiki/Correlation_coefficient) between two quote histories, based on Close price.  R-Squared (R&sup2;), Variance, and Covariance are also output.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/259 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Correlation.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Correlation/Correlation.Series.cs)
- [Python wrapper]({{site.sourceurl}}/correlation.py)
