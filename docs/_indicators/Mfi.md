---
title: Money Flow Index (MFI)
permalink: /indicators/Mfi/
type: volume-based
layout: indicator
---

# {{ page.title }}

<hr>

## **get_mfi**(*quotes, lookback_periods=14*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 14* | Number of periods (`N`) in the lookback period.  Must be greater than 1.

### Historical quotes requirements

You must have at least `N+1` historical quotes to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
MFIResults[MFIResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `MFIResults` is just a list of `MFIResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` MFI values since they cannot be calculated.

### MFIResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `mfi` | float, Optional | Money Flow Index

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

# Calculate
results = indicators.get_mfi(quotes, 14)
```

## About {{ page.title }}

Created by Quong and Soudack, the [Money Flow Index](https://en.wikipedia.org/wiki/Money_flow_index) is a price-volume oscillator that shows buying and selling momentum.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/247 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Mfi.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Mfi/Mfi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/mfi.py)
