---
title: Parabolic SAR
permalink: /indicators/ParabolicSar/
type: stop-and-reverse
layout: indicator
---

# {{ page.title }}

<hr>

## **get_parabolic_sar**(*quotes, acceleration_step=0.02, max_acceleration_factor=0.2*)

### More overloaded interfaces

**get_parabolic_sar**(quotes, acceleration_step, max_acceleration_factor, initial_factor)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `acceleration_step` | float, *default 0.02* | Incremental step size for the Acceleration Factor.  Must be greater than 0.
| `max_acceleration_factor` | float, *default 0.2* | Maximum factor limit.  Must be greater than `acceleration_step`.
| `initial_factor` | float | Initial Acceleration Factor.  Must be greater than 0.  Default is `acceleration_step`.

### Historical quotes requirements

You must have at least two historical quotes to cover the warmup periods; however, we recommend at least 100 data points.  Initial Parabolic SAR values prior to the first reversal are not accurate and are excluded from the results.  Therefore, provide sufficient quotes to capture prior trend reversals, before your intended usage period.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
ParabolicSARResults[ParabolicSARResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ParabolicSARResults` is just a list of `ParabolicSARResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first trend will have `None` values since it is not accurate and based on an initial guess.

### ParabolicSARResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sar` | float, Optional | Stop and Reverse value
| `is_reversal` | bool, Optional | Indicates a trend reversal

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

# calculate ParabolicSar(0.02,0.2)
results = indicators.get_parabolic_sar(quotes, 0.02, 0.2)
```

## About {{ page.title }}

Created by J. Welles Wilder, [Parabolic SAR](https://en.wikipedia.org/wiki/Parabolic_SAR) (stop and reverse) is a price-time based indicator used to determine trend direction and reversals.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/245 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ParabolicSar.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/ParabolicSar/ParabolicSar.Series.cs)
- [Python wrapper]({{site.sourceurl}}/parabolic_sar.py)
