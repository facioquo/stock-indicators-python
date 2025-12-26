---
title: ATR Trailing Stop
description: Created by Welles Wilder, the ATR Trailing Stop indicator attempts to determine the primary trend of financial market prices by using Average True Range (ATR) band thresholds.  It can indicate a buy/sell signal or a trailing stop when the trend changes.
permalink: /indicators/AtrStop/
type: price-trend
layout: indicator
---

# {{ page.title }}

><span class="indicator-syntax">**get_atr_stop**(*quotes, lookback_periods=21, multiplier=3, end_type=EndType.CLOSE*)</span>

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [See here]({{site.baseurl}}/guide/#using-pandasdataframe) for usage with pandas.DataFrame</span>
| `lookback_periods` | int, *default 21* | Number of periods (`N`) for the ATR evaluation.  Must be greater than 1.
| `multiplier` | float, *default 3* | Multiplier sets the ATR band width.  Must be greater than 0 and is usually set around 2 to 3.
| `end_type` | EndType, *default EndType.Close* | Determines whether `Close` or `High/Low` is used as basis for stop offset.  See [EndType options](#endtype-options) below.

### Historical quotes requirements

You must have at least `N+100` periods of `quotes` to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+250` periods prior to the intended usage date for optimal precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### EndType options

```python
from stock_indicators.indicators.common.enums import EndType
```

| type | description
|-- |--
| `CLOSE` | Stop offset from `Close` price (default)
| `HIGH_LOW` | Stop offset from `High` or `Low` price

## Returns

```python
AtrStopResults[AtrStopResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `AtrStopResults` is just a list of `AtrStopResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` AtrStop values since there's not enough data to calculate.

>&#9886; **Convergence warning**: the line segment before the first reversal and the first `N+100` periods are unreliable due to an initial guess of trend direction and precision convergence for the underlying ATR values.

### AtrStopResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `atr_stop` | Decimal, Optional  | ATR Trailing Stop line contains both Upper and Lower segments
| `buy_stop` | Decimal, Optional  | Upper band only (green)
| `sell_stop` | Decimal, Optional  | Lower band only (red)

`buy_stop` and `sell_stop` values are provided to differentiate buy vs sell stop lines and to clearly demark trend reversal.  `atr_stop` is the contiguous combination of both upper and lower line data.

### Utilities

- [.condense()]({{site.baseurl}}/utilities#condense)
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_historical_quotes("SPY")

# calculate 21-period ATR Stop
results = indicators.get_atr_stop(quotes)
```

## About {{ page.title }}

Created by Welles Wilder, the ATR Trailing Stop indicator attempts to determine the primary trend of Close prices by using [Average True Range (ATR)]({{site.baseurl}}/indicators/Atr/#content) band thresholds.  It can indicate a buy/sell signal or a trailing stop when the trend changes.
[[Discuss] &#128172;]({{site.dotnet.repo}}/discussions/724 "Community discussion about this indicator")

![chart for {{page.title}}]({{site.dotnet.charts}}/AtrStop.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/AtrStop/AtrStop.Series.cs)
- [Python wrapper]({{site.python.src}}/atr_stop.py)
