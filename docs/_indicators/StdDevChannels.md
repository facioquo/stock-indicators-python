---
title: Standard Deviation Channels
permalink: /indicators/StdDevChannels/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_stdev_channels**(*quotes, lookback_periods=20, standard_deviations=2*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, Optional, *default 20*  | Size (`N`) of the evaluation window.  Must be `None` or greater than 1 to calculate.  A `None` value will produce a full `quotes` evaluation window ([see below](#alternative-depiction-for-full-quotes-variant)).
| `standard_deviations` | int, *default 2*  | Width of bands.  Standard deviations (`D`) from the regression line.  Must be greater than 0.  Default is 2.

### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
StdevChannelsResults[StdevChannelsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `StdevChannelsResults` is just a list of `StdevChannelsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- Up to `N-1` periods will have `None` values since there's not enough data to calculate.

> :paintbrush: **Repaint warning**: Historical results are a function of the current period window position and will fluctuate over time.  Recommended for visualization; not recommended for backtesting.

### StdevChannelsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `center_line` | float, Optional | Linear regression line (center line)
| `upper_channel` | float, Optional | Upper line is `D` standard deviations above the center line
| `lower_channel` | float, Optional | Lower line is `D` standard deviations below the center line
| `break_point` | bool | Helper information.  Indicates first point in new window.

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

# calculate StdDevChannels(20,2)
results = indicators.get_stdev_channels(quotes, 20,2)
```

## Alternative depiction for full quotes variant

If you specify `None` for the `lookback_periods`, you will get a regression line over the entire provided `quotes`.

![image]({{site.dotnet.charts}}/StdDevChannelsFull.png)

## About {{ page.title }}

Standard Deviation Channels are based on an linear regression centerline and standard deviations band widths.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/368 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/StdDevChannels.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/StdDevChannels/StdDevChannels.Series.cs)
- [Python wrapper]({{site.sourceurl}}/stdev_channels.py)
