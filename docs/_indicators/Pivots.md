---
title: Pivots
permalink: /indicators/Pivots/
type: price-pattern
layout: indicator
---

# {{ page.title }}

<hr>

## **get_pivots**(*quotes, left_span=2, right_span=2, max_trend_periods=20, end_type=EndType.HIGH_LOW*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `left_span` | int, *default 2* | Left evaluation window span width (`L`).  Must be at least 2.
| `right_span` | int, *default 2* | Right evaluation window span width (`R`).  Must be at least 2.
| `max_trend_periods` | int, *default 20* | Number of periods (`N`) in evaluation window.  Must be greater than `leftSpan`.
| `end_type` | EndType, *default EndType.HIGH_LOW* | Determines whether `close` or `high/low` are used to find end points.  See [EndType options](#endtype-options) below.

The total evaluation window size is `L+R+1`.

### Historical quotes requirements

You must have at least `L+R+1` periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### EndType options

```python
from stock_indicators.indicators.common.enums import EndType
```

| type | description
|-- |--
| `CLOSE` | Chevron point identified from `close` price
| `HIGH_LOW` | Chevron point identified from `high` and `low` price (default)

## Return

```python
PivotsResults[PivotsResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `PivotsResults` is just a list of `PivotsResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `L` and last `R` periods in `quotes` are unable to be calculated since there's not enough prior/following data.

> :paintbrush: **Repaint warning**: this price pattern looks forward and backward in the historical quotes so it will never identify a pivot in the last `R` periods of `quotes`.  Fractals are retroactively identified.

### PivotsResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `high_point` | Decimal, Optional | Value indicates a **high** point; otherwise `None` is returned.
| `low_point` | Decimal, Optional | Value indicates a **low** point; otherwise `None` is returned.
| `high_line` | Decimal, Optional | Drawn line between two high points in the `max_trend_periods`
| `low_line` | Decimal, Optional | Drawn line between two low points in the `max_trend_periods`
| `high_trend` | PivotTrend, Optional | Enum that represents higher high or lower high.  See [PivotTrend values](#pivottrend-values) below.
| `low_trend` | PivotTrend, Optional | Enum that represents higher low or lower low.  See [PivotTrend values](#pivottrend-values) below.

#### PivotTrend values

```python
from stock_indicators.indicators.common.enums import PivotTrend
```

| type | description
|-- |--
| `PivotTrend.HH` | Higher high
| `PivotTrend.LH` | Lower high
| `PivotTrend.HL` | Higher low
| `PivotTrend.LL` | Lower low

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import EndType     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate Pivots(2,2,20) using High/Low values
results = indicators.get_pivots(quotes, 2, 2, 20, EndType.HIGH_LOW);
```

## About {{ page.title }}

Pivots is an extended version of [Williams Fractal](../Fractal#content) that includes identification of Higher High, Lower Low, Higher Low, and Lower Low trends between pivots in a lookback window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/436 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Pivots.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/Pivots/Pivots.Series.cs)
- [Python wrapper]({{site.sourceurl}}/pivots.py)
