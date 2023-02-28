---
title: Williams Alligator
permalink: /indicators/Alligator/
type: price-trend
layout: indicator
---

# {{ page.title }}

<hr>

## **get_alligator**(*quotes, jaw_periods==13, jaw_offset=8, teeth_periods=8, teeth_offset=5, lips_periods=5, lips_offset=3*)

## Parameters

| name | type | notes
| -- | -- | --
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `jaw_periods` | int, *default 13* | Number of periods (`JP`) for the Jaw moving average.  Must be greater than `teeth_periods`.
| `jaw_offset` | int, *default 8* | Number of periods (`JO`) for the Jaw offset.  Must be greater than 0.
| `teeth_periods` | int, *default 8* | Number of periods (`TP`) for the Teeth moving average.  Must be greater than `lips_periods`.
| `teeth_offset` | int, *default 5* | Number of periods (`TO`) for the Teeth offset.  Must be greater than 0.
| `lips_periods` | int, *default 5* | Number of periods (`LP`) for the Lips moving average.  Must be greater than 0.
| `lips_offset` | int, *default 3* | Number of periods (`LO`) for the Lips offset.  Must be greater than 0.

### Historical quotes requirements

You must have at least 115 periods of `quotes`. Since this uses a smoothing technique, we recommend you use at least 265 data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
AlligatorResults[AlligatorResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `AlligatorResults` is just a list of `AlligatorResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first 10-20 periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `JP+JO+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### AlligatorResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `jaw` | float, Optional | Alligator's Jaw
| `teeth` | float, Optional | Alligator's Teeth
| `lips` | float, Optional | Alligator's Lips

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

## About {{ page.title }}

Created by Bill Williams, Alligator is a depiction of three smoothed moving averages of median price, showing chart patterns that compared to an alligator's feeding habits when describing market movement. The moving averages are known as the Jaw, Teeth, and Lips, which are calculated using specific lookback and offset periods.  See also the [Gator Oscillator](../Gator#content).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/385 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Alligator.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Alligator/Alligator.Series.cs)
- [Python wrapper]({{site.sourceurl}}/alligator.py)
