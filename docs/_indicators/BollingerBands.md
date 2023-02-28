---
title: Bollinger Bands&#174;
permalink: /indicators/BollingerBands/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_bollinger_bands**(*quotes, lookback_periods=20, standard_deviations=2*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 20* | Number of periods (`N`) for the center line moving average.  Must be greater than 1 to calculate; however we suggest a larger period for statistically appropriate sample size.
| `standard_deviations` | int, *default 2* | Width of bands.  Standard deviations (`D`) from the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
BollingerBandsResults[BollingerBandsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `BollingerBandsResults` is just a list of `BollingerBandsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### BollingerBandsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sma` | float, Optional | Simple moving average (SMA) of Close price (center line)
| `upper_band` | float, Optional | Upper line is `D` standard deviations above the SMA
| `lower_band` | float, Optional | Lower line is `D` standard deviations below the SMA
| `percent_b` | float, Optional | `%B` is the location within the bands.  `(Price-lower_band)/(upper_band-lower_band)`
| `z_score` | float, Optional | Z-Score of current Close price (number of standard deviations from mean)
| `width` | float, Optional | Width as percent of SMA price.  `(upper_band-lower_band)/sma`

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

# calculate BollingerBands(20, 2)
results = indicators.get_bollinger_bands(quotes, 20, 2)
```

## About {{ page.title }}

Created by John Bollinger, [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands) depict volatility as standard deviation boundary lines from a moving average of Close price.  Bollinger Bands&#174; is a registered trademark of John A. Bollinger.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/267 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/BollingerBands.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/BollingerBands/BollingerBands.Series.cs)
- [Python wrapper]({{site.sourceurl}}/bollinger_bands.py)
