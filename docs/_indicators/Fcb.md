---
title: Fractal Chaos Bands (FCB)
permalink: /indicators/Fcb/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_fcb**(*quotes, window_span=2*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `window_span` | int | Fractal evaluation window span width (`S`).  Must be at least 2.  Default is 2.

The total evaluation window size is `2×S+1`, representing `±S` from the evaluation date.  See [Williams Fractal](../Fractal#content) for more information about Fractals and `window_span`.

### Historical quotes requirements

You must have at least `2×S+1` periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
FCBResults[FCBResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `FCBResults` is just a list of `FCBResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The periods before the first fractal are `None` since they cannot be calculated.

### FCBResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `upper_band` | Decimal, Optional | FCB upper band
| `lower_band` | Decimal, Optional | FCB lower band

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

# Calculate Fcb(14)
results = indicators.get_fcb(quotes, 14)
```

## About {{ page.title }}

Created by Edward William Dreiss, Fractal Chaos Bands outline high and low price channels to depict broad less-chaotic price movements.  FCB is a channelized depiction of [Williams Fractal](../Fractal#content).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/347 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Fcb.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Fcb/Fcb.Series.cs)
- [Python wrapper]({{site.sourceurl}}/fcb.py)
