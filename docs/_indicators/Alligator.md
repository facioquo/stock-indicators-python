---
title: Williams Alligator
permalink: /indicators/Alligator/
type: price-trend
layout: indicator
---

# {{ page.title }}
<hr>

## **get_alligator**(*quotes*)

## Parameters

| name | type | notes
| -- | -- | --
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).

### Historical quotes requirements

You must have at least 115 periods of `quotes`. Since this uses a smoothing technique, we recommend you use at least 265 data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Type[Quote]]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### Internal parameters

This indicator uses fixed interal parameters for the three moving averages of median price `(H+L)/2`.

| SMMA | Lookback | Offset
| -- |-- |--
| Jaw | 13 | 8
| Teeth | 8 | 5
| Lips | 5 | 3

## Returns

```python
AlligatorResults[AlligatorResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first 10-20 periods will have `None` values since there's not enough data to calculate.

:hourglass: **Convergence Warning**: The first 150 periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### AlligatorResult

| name | type | notes
| -- |-- |--
| `date` | datetime.datetime | Date
| `jaw` | decimal.Decimal | Alligator's Jaw
| `teeth` | decimal.Decimal | Alligator's Teeth
| `lips` | decimal.Decimal | Alligator's Lips

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

# calculate the Williams Alligator
results = indicators.get_alligator(quotes)
```

## About: {{ page.title }}

Created by Bill Williams, Alligator is a depiction of three smoothed moving averages of median price, showing chart patterns that compared to an alligator's feeding habits when describing market movement. The moving averages are known as the Jaw, Teeth, and Lips, which are calculated using specific lookback and offset periods.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/385 "Community discussion about this indicator")

![image]({{site.charturl}}/Alligator.png)

### Sources

 - [C# core]({{site.base_sourceurl}}/a-d/Alligator/Alligator.cs)
 - [Python wrapper]({{site.sourceurl}}/alligator.py)
