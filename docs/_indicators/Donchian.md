---
title: Donchian Channels
description: Donchian Channels (Price Channels)
permalink: /indicators/Donchian/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_donchian**(*quotes, lookback_periods=20*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 20* | Number of periods (`N`) for lookback period.  Must be greater than 0 to calculate; however we suggest a larger value for an appropriate sample size.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
DonchianResults[DonchianResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `DonchianResults` is just a list of `DonchianResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values since there's not enough data to calculate.

### DonchianResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `upper_band` | Decimal, Optional | Upper line is the highest High over `N` periods
| `center_line` | Decimal, Optional | Simple average of Upper and Lower bands
| `lower_band` | Decimal, Optional | Lower line is the lowest Low over `N` periods
| `width` | Decimal, Optional | Width as percent of Centerline price.  `(upper_band-lower_band)/center_line`

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

# calculate Donchian(20)
results = indicators.get_donchian(quotes, 20)
```

## About {{ page.title }}

Created by Richard Donchian, [Donchian Channels](https://en.wikipedia.org/wiki/Donchian_channel), also called Price Channels, are derived from highest High and lowest Low values over a lookback window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/257 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Donchian.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Donchian/Donchian.Series.cs)
- [Python wrapper]({{site.sourceurl}}/donchian.py)
