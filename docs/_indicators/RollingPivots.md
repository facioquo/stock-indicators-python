---
title: Rolling Pivot Points
permalink: /indicators/RollingPivots/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_rolling_pivots**(*quotes, window_periods, offset_periods, point_type=PivotPointType.STANDARD*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `window_periods` | int | Number of periods (`W`) in the evaluation window.  Must be greater than 0 to calculate; but is typically specified in the 5-20 range.
| `offset_periods` | int | Number of periods (`F`) to offset the window from the current period.  Must be greater than or equal to 0 and is typically less than or equal to `W`.
| `point_type` | PivotPointType, *default PivotPointType.STANDARD* | Type of Pivot Point. See [PivotPointType options](#pivotpointtype-options) below.

For example, a window of 8 with an offset of 4 would evaluate quotes like: `W W W W W W W W F F  F F C`, where `W` is the window included in the Pivot Point calculation, and `F` is the distance from the current evaluation position `C`.  A `quotes` with daily bars using `W/F` values of `20/10` would most closely match the `month` variant of the traditional [Pivot Points](../PivotPoints#content) indicator.

### Historical quotes requirements

You must have at least `W+F` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### PivotPointType options

```python
from stock_indicators.indicators.common.enums import PivotPointType
```

| type | description
|-- |--
| `PivotPointType.STANDARD` | Floor Trading (default)
| `PivotPointType.CAMARILLA` | Camarilla
| `PivotPointType.DEMARK` | Demark
| `PivotPointType.FIBONACCI` | Fibonacci
| `PivotPointType.WOODIE` | Woodie

## Return

```python
RollingPivotsResults[RollingPivotsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `RollingPivotsResults` is just a list of `RollingPivotsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `W+F-1` periods will have `None` values since there's not enough data to calculate.

### RollingPivotsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `r3` | Decimal, Optional | Resistance level 3
| `r2` | Decimal, Optional | Resistance level 2
| `r1` | Decimal, Optional | Resistance level 1
| `pp` | Decimal, Optional | Pivot Point
| `s1` | Decimal, Optional | Support level 1
| `s2` | Decimal, Optional | Support level 2
| `s3` | Decimal, Optional | Support level 3

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import PivotPointType     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate Woodie-style 14 period Rolling Pivot Points
results = indicators.get_rolling_pivots(quotes, 14, 0, PivotPointType.Woodie);
```

## About {{ page.title }}

Created by Dave Skender, Rolling Pivot Points is a modern update to traditional fixed calendar window [Pivot Points](../PivotPoints#content).  It depicts support and resistance levels, based on a defined *rolling* window and offset.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/274 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/RollingPivots.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/RollingPivots/RollingPivots.Series.cs)
- [Python wrapper]({{site.sourceurl}}/rolling_pivots.py)
