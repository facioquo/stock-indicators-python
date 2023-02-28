---
title: Williams Fractal
permalink: /indicators/Fractal/
type: price-pattern
layout: indicator
---

# {{ page.title }}

<hr>

## **get_fractal**(*quotes, window_span=2, end_type = EndType.HIGH_LOW*)

### More overloaded interfaces

**get_fractal**(quotes, left_span, right_span, end_type)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `window_span` | int, *default 2* | Evaluation window span width (`S`).  Must be at least 2.
| `end_type` | EndType | Determines whether `close` or `high/low` are used to find end points.  See [EndType options](#endtype-options) below.  Default is `EndType.HIGH_LOW`.

The total evaluation window size is `2×S+1`, representing `±S` from the evaluation date.

### Historical quotes requirements

You must have at least `2×S+1` periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### EndType options

```python
from stock_indicators.indicators.common.enums import EndType
```

| type | description
|-- |--
| `CLOSE` | Chevron point identified from `close` price
| `HIGH_LOW` | Chevron point identified from `high` and `low` price (default)

## Returns

```python
FractalResults[FractalResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `FractalResults` is just a list of `FractalResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first and last `S` periods in `quotes` are unable to be calculated since there's not enough prior/following data.

> :paintbrush: **Repaint warning**: this price pattern uses future bars and will never identify a `fractal` in the last `S` periods of `quotes`.  Fractals are retroactively identified.

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

## About {{ page.title }}

Created by Larry Williams, [Fractal](https://www.investopedia.com/terms/f/fractal.asp) is a retrospective price pattern that identifies a central high or low point.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/255 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Fractal.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/Fractal/Fractal.Series.cs)
- [Python wrapper]({{site.sourceurl}}/fractal.py)
