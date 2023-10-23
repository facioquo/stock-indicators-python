---
title: Elder-ray Index
description: Elder-ray Index with Bull and Bear Power
permalink: /indicators/ElderRay/
type: price-trend
layout: indicator
---

# {{ page.title }}

<hr>

## **get_elder_ray**(*quotes, lookback_periods=13*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 13*  | Number of periods (`N`) for the underlying EMA evaluation.  Must be greater than 0.

### Historical quotes requirements

You must have at least `2×N` or `N+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
ElderRayResults[ElderRayResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ElderRayResults` is just a list of `ElderRayResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` indicator values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ElderRayResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `ema` | float, Optional | Exponential moving average of Close price
| `bull_power` | float, Optional | Bull Power
| `bear_power` | float, Optional | Bear Power

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

# calculate ElderRay(13)
results = indicators.get_elder_ray(quotes, 13)
```

## About {{ page.title }}

Created by Alexander Elder, the [Elder-ray Index](https://www.investopedia.com/terms/e/elderray.asp), also known as Bull and Bear Power, depicts buying and selling pressure.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/378 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ElderRay.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/ElderRay/ElderRay.Series.cs)
- [Python wrapper]({{site.sourceurl}}/elder_ray.py)
