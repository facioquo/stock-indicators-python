---
title: Pivot Points
permalink: /indicators/PivotPoints/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_pivot_points**(*quotes, window_size, point_type=PivotPointType.STANDARD*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `window_size` | PeriodSize | Size of the lookback window. See [PeriodSize options](#periodsize-options-for-window_size) below.
| `point_type` | PivotPointType, *default PivotPointType.STANDARD* | Type of Pivot Point. See [PivotPointType options](#pivotpointtype-options) below.

### Historical quotes requirements

You must have at least `2` windows of `quotes` to cover the warmup periods.  For example, if you specify a `WEEK` window size, you need at least 14 calendar days of `quotes`.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### PeriodSize options (for `window_size`)

```python
from stock_indicators.indicators.common.enums import PeriodSize
```

| type | description
|-- |--
| `PeriodSize.MONTH` | Use the prior month's data to calculate current month's Pivot Points
| `PeriodSize.WEEK` | [..] weekly
| `PeriodSize.DAY` | [..] daily.  Commonly used for intraday data.
| `PeriodSize.ONEHOUR` | [..] hourly

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
PivotPointsResults[PivotPointsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `PivotPointsResults` is just a list of `PivotPointsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first window will have `None` values since there's not enough data to calculate.

> :warning: **Warning**: The second window may be inaccurate if the first window contains incomplete data.  For example, this can occur if you specify a `Month` window size and only provide 45 calendar days (1.5 months) of `quotes`.
>
> :paintbrush: **Repaint warning**: the last window will be repainted if it does not contain a full window of data.

### PivotPointsResult

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
from stock_indicators import PeriodSize, PivotPointType      # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate Woodie-style month-based Pivot Points
results = indicators.get_pivot_points(quotes, PeriodSize.MONTH, PivotPointType.WOODIE);
```

## About {{ page.title }}

[Pivot Points](https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis)) depict support and resistance levels, based on the prior lookback window.  You can specify window size (e.g. month, week, day, etc).
See also the alternative [Rolling Pivot Points](../RollingPivots#content) variant for a modern update that uses a rolling window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/274 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/PivotPoints.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/PivotPoints/PivotPoints.Series.cs)
- [Python wrapper]({{site.sourceurl}}/pivot_points.py)
