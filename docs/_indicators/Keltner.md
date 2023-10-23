---
title: Keltner Channels
permalink: /indicators/Keltner/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_keltner**(*quotes, ema_periods=20, multiplier=2.0, atr_periods=10*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `ema_periods` | int, *default 20* | Number of lookback periods (`E`) for the center line moving average.  Must be greater than 1 to calculate.
| `multiplier` | float, *default 2.0* | ATR Multiplier. Must be greater than 0.
| `atr_periods` | int, *default 10* | Number of lookback periods (`A`) for the Average True Range.  Must be greater than 1 to calculate.

### Historical quotes requirements

You must have at least `2×N` or `N+100` periods of `quotes`, whichever is more, where `N` is the greater of `E` or `A` periods, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
KeltnerResults[KeltnerResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `KeltnerResults` is just a list of `KeltnerResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N+250` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### KeltnerResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `upper_band` | float, Optional | Upper band of Keltner Channel
| `center_line` | float, Optional | EMA of Close price
| `lower_band` | float, Optional | Lower band of Keltner Channel
| `width` | float, Optional | Width as percent of Centerline price.  `(upper_band-lower_band)/center_line`

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

# Calculate Keltner(20)
results = indicators.get_keltner(quotes, 20,2.0,10)
```

## About {{ page.title }}

Created by Chester W. Keltner, [Keltner Channels](https://en.wikipedia.org/wiki/Keltner_channel) are based on an EMA centerline and ATR band widths.  See also [STARC Bands](../StarcBands#content) for an SMA centerline equivalent.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/249 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Keltner.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Keltner/Keltner.Series.cs)
- [Python wrapper]({{site.sourceurl}}/keltner.py)
