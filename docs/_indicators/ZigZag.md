---
title: Zig Zag
permalink: /indicators/ZigZag/
type: price-transform
layout: indicator
---

# {{ page.title }}

<hr>

## **get_zig_zag**(*quotes, end_type=EndType.CLOSE, percent_change=5*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `end_type` | EndType, *default EndType.CLOSE* | Determines whether `close` or `high/low` are used to measure percent change.  See [EndType options](#endtype-options) below.
| `percent_change` | float,  *default 5* | Percent change required to establish a line endpoint.  Example: 3.5% would be entered as 3.5 (not 0.035).  Must be greater than 0.  Typical values range from 3 to 10.

### Historical quotes requirements

You must have at least two periods of `quotes` to cover the warmup periods, but notably more is needed to be useful.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### EndType options

```python
from stock_indicators.indicators.common.enums import EndType
```

| type | description
|-- |--
| `EndType.CLOSE` | Percent change measured from `close` price (default)
| `EndType.HIGH_LOW` | Percent change measured from `high` and `low` price

## Returns

```python
ZigZagResults[ZigZagResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ZigZagResults` is just a list of `ZigZagResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- If you do not supply enough points to cover the percent change, there will be no Zig Zag points or lines.
- The first line segment starts after the first confirmed point; ZigZag values before the first confirmed point will be `None`.
- The last line segment is an approximation as the direction is indeterminate.

> :warning: **Warning**: depending on the specified `endType`, the indicator cannot be initialized if the first `Quote` in `quotes` has a `High`,`Low`, or `Close` value of 0 (zero).
>
> :paintbrush: **Repaint warning**: the last line segment will always be redrawn back to the last known pivot.  Do not attempt to calculate incremental values since previous values may change based on newer quotes.

### ZigZagResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `zig_zag` | Decimal, Optional | Zig Zag line for `percent_change`
| `point_type` | str, Optional | Zig Zag endpoint type (`H` for high point, `L` for low point)
| `retrace_high` | Decimal, Optional | Retrace line for high points
| `retrace_low` | Decimal, Optional | Retrace line for low points

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

# Calculate 3% change ZIGZAG
results = indicators.get_zig_zag(quotes, EndType.CLOSE, 3);
```

## About {{ page.title }}

[Zig Zag](https://school.stockcharts.com/doku.php?id=technical_indicators:zigzag) is a price chart overlay that simplifies the up and down movements and transitions based on a percent change smoothing threshold.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/226 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ZigZag.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/ZigZag/ZigZag.Series.cs)
- [Python wrapper]({{site.sourceurl}}/zig_zag.py)
