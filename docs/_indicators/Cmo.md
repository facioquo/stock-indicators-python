---
title: Chande Momentum Oscillator (CMO)
description: The Chande Momentum Oscillator is a momentum indicator depicting the weighted percent of higher prices in financial markets.
permalink: /indicators/Cmo/
type: oscillator
layout: indicator
---

# {{ page.title }}

><span class="indicator-syntax">**get_cmo**(*quotes, lookback_periods*)</span>

## Parameters

| name | type | notes
| -- | -- | --
| `quotes` | Iterable[Quote] | Iterable of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [See here]({{site.baseurl}}/guide/#using-pandasdataframe) for usage with pandas.DataFrame</span>
| `lookback_periods` | int | Number of periods (`N`) in the lookback window.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
CMOResults[CMOResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `CMOResults` is just a list of `CMOResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values for CMO since there's not enough data to calculate.

### CmoResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `cmo` | float, Optional | Chande Momentum Oscillator

### Utilities

- [.condense()]({{site.baseurl}}/utilities#condense)
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_historical_quotes("SPY")

results = indicators.get_cmo(quotes, lookback_periods)
```

## About {{ page.title }}

Created by Tushar Chande, the [Chande Momentum Oscillator](https://www.investopedia.com/terms/c/chandemomentumoscillator.asp) is a weighted percent of higher prices over a lookback window.
[[Discuss] &#128172;]({{site.dotnet.repo}}/discussions/892 "Community discussion about this indicator")

![chart for {{page.title}}]({{site.dotnet.charts}}/Cmo.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Cmo/Cmo.Series.cs)
- [Python wrapper]({{site.python.src}}/cmo.py)
