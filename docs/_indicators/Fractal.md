---
title: Williams Fractal
permalink: /indicators/Fractal/
type: price-pattern
layout: indicator
---

# {{ page.title }}
<hr>

## **get_fractal**(*quotes, window_span=2*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `window_span` | int, *default 2* | Evaluation window span width (`S`).  Must be at least 2.

<!-- | `endType` | EndType | Determines whether `Close` or `High/Low` are used to find end points.  See [EndType options](#endtype-options) below.  Default is `EndType.HighLow`. -->

The total evaluation window size is `2×S+1`, representing `±S` from the evalution date.

### Historical quotes requirements

You must have at least `2×S+1` periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Type[Quote]]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

<!-- ### EndType options

| type | description
|-- |--
| `EndType.Close` | Chevron point identified from `Close` price
| `EndType.HighLow` | Chevron point identified from `High` and `Low` price (default) -->

## Returns

```python
FractalResults[FractalResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first and last `S` periods in `quotes` are unable to be calculated since there's not enough prior/following data.

:paintbrush: **Repaint Warning**: this price pattern looks forward and backward in the historical quotes so it will never identify a `fractal` in the last `S` periods of `quotes`.  Fractals are retroactively identified.

### FractalResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `fractal_bear` | Decimal, Optional | Value indicates a **high** point; otherwise `None` is returned.
| `fractal_bull` | Decimal, Optional | Value indicates a **low** point; otherwise `None` is returned.

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate Fractal
results = indicators.get_fractal(quotes, 5)
```

## About: {{ page.title }}

Created by Larry Williams, [Fractal](https://www.investopedia.com/terms/f/fractal.asp) is a retrospective price pattern that identifies a central high or low point.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/255 "Community discussion about this indicator")

![image]({{site.charturl}}/Fractal.png)

### Sources

- [C# core]({{site.base_sourceurl}}/e-k/Fractal/Fractal.cs)
- [Python wrapper]({{site.sourceurl}}/fractal.py)
