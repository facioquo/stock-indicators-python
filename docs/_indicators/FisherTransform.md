---
title: Ehlers Fisher Transform
permalink: /indicators/FisherTransform/
type: price-transform
layout: indicator
---

# {{ page.title }}

<hr>

## **get_fisher_transform**(*quotes, lookback_periods=10*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 10* | Number of periods (`N`) in the lookback window.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
FisherTransformResults[FisherTransformResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `FisherTransformResults` is just a list of `FisherTransformResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.

> :hourglass: **Convergence warning**: The first `N+15` warmup periods will have unusable decreasing magnitude, convergence-related precision errors that can be as high as ~25% deviation in earlier indicator values.

### FisherTransformResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `fisher` | float, Optional | Fisher Transform
| `trigger` | float, Optional | FT offset by one period

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

For pruning of warmup periods, we recommend using the following guidelines:

```python
indicators.get_fisher_transform(quotes, lookback_periods)
  .remove_warmup_periods(lookback_periods + 15)
```

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate 10-period FisherTransform
results = indicators.get_fisher_transform(quotes, 10)
```

## About {{ page.title }}

Created by John Ehlers, the [Fisher Transform](https://www.investopedia.com/terms/f/fisher-transform.asp) converts prices into a Gaussian normal distribution.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/409 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/FisherTransform.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/FisherTransform/FisherTransform.Series.cs)
- [Python wrapper]({{site.sourceurl}}/fisher_transform.py)
