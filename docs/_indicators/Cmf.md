---
title: Chaikin Money Flow (CMF)
permalink: /indicators/Cmf/
type: volume-based
layout: indicator
---

# {{ page.title }}

><span class="indicator-syntax">**get_cmf**(*quotes, lookback_periods=20*)</span>

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [See here]({{site.baseurl}}/guide/#using-pandasdataframe) for usage with pandas.DataFrame</span>
| `lookback_periods` | int, *default 20* | Number of periods (`N`) in the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
CMFResults[CMFResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `CMFResults` is just a list of `CMFResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### CmfResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `money_flow_multiplier` | float, Optional | Money Flow Multiplier
| `money_flow_volume` | float, Optional | Money Flow Volume
| `cmf` | float, Optional | Chaikin Money Flow = SMA of MFV

>&#128681; **Warning**: absolute values in MFV and CMF are somewhat meaningless.  Use with caution.

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

# Calculate 20-period CMF
results = indicators.get_cmf(quotes, 20)
```

## About {{ page.title }}

Created by Marc Chaikin, [Chaikin Money Flow](https://en.wikipedia.org/wiki/Chaikin_Analytics#Chaikin_Money_Flow) is the simple moving average of the Money Flow Volume.
[[Discuss] &#128172;]({{site.dotnet.repo}}/discussions/261 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Cmf.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Cmf/Cmf.Series.cs)
- [Python wrapper]({{site.python.src}}/cmf.py)
