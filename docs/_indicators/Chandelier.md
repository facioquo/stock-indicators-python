---
title: Chandelier Exit
permalink: /indicators/Chandelier/
type: stop-and-reverse
layout: indicator
---

# {{ page.title }}

<hr>

## **get_chandelier**(*quotes, lookback_periods=22, multiplier=3.0, chandelier_type=ChandelierType.LONG*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int, *default 22* | Number of periods (`N`) for the lookback evaluation.
| `multiplier` | float, *default 3.0* | Multiplier number must be a positive value.
| `chandelier_type` | ChandelierType, *default ChandelierType.LONG* | Direction of exit.  See [ChandelierType options](#chandeliertype-options) below.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### ChandelierType options

```python
from stock_indicators.indicators.common.enums import ChandelierType
```

| type | description
|-- |--
| `LONG` | Intended as stop loss value for long positions. (default)
| `SHORT` | Intended as stop loss value for short positions.

## Return

```python
ChandelierResults[ChandelierResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ChandelierResults` is just a list of `ChandelierResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` Chandelier values since there's not enough data to calculate.

### ChandelierResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `chandelier_exit` | float, Optional | Exit line

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import ChandelierType     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate Chandelier(22,3)
results = indicators.get_chandelier(quotes, 22, 3, ChandelierType.LONG)
```

## About {{ page.title }}

Created by Charles Le Beau, the [Chandelier Exit](https://school.stockcharts.com/doku.php?id=technical_indicators:chandelier_exit) is typically used for stop-loss and can be computed for both long or short types.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/263 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Chandelier.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Chandelier/Chandelier.Series.cs)
- [Python wrapper]({{site.sourceurl}}/chandelier.py)
