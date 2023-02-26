---
title: STARC Bands
permalink: /indicators/StarcBands/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_starc_bands**(*quotes, sma_periods=20, multiplier=2.0, atr_periods=10*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `sma_periods` | int, *default 20* | Number of lookback periods (`S`) for the center line moving average.  Must be greater than 1 to calculate and is typically between 5 and 10.
| `multiplier` | float, *default 2.0* | ATR Multiplier. Must be greater than 0.  Default is 2.
| `atr_periods` | int, *default 10* | Number of lookback periods (`A`) for the Average True Range.  Must be greater than 1 to calculate and is typically the same value as `sma_periods`.  Default is 10.

### Historical quotes requirements

You must have at least `S` or `A+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `A+150` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
STARCBandsResults[STARCBandsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `STARCBandsResults` is just a list of `STARCBandsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate, where `N` is the greater of `S` or `A`.

> :hourglass: **Convergence warning**: The first `A+150` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### STARCBandsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `upper_band` | float, Optional | Upper STARC band
| `center_line` | float, Optional | SMA of Close price
| `lower_band` | float, Optional | Lower STARC band

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

# Calculate StarcBands(20)
results = indicators.get_starc_bands(quotes, 20, 2.0, 10)
```

## About {{ page.title }}

Created by Manning Stoller, [Stoller Average Range Channel (STARC) Bands](https://www.investopedia.com/terms/s/starc.asp), are based on an SMA centerline and ATR band widths.  See also [Keltner Channels](../Keltner#content) for an EMA centerline equivalent.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/292 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/StarcBands.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/StarcBands/StarcBands.Series.cs)
- [Python wrapper]({{site.sourceurl}}/starc_bands.py)
