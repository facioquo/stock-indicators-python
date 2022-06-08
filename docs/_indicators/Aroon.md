---
title: Aroon
permalink: /indicators/Aroon/
type: price-trend
layout: indicator
---

# {{ page.title }}
<hr>

## **get_aroon**(*quotes, lookback_periods=25*)

## Parameters

| name | type | notes
| -- | -- | --
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Got in trouble with Pandas.dataframe?]({{site.baseurl}}/guide/#using-pandasdataframe) </span>
| `lookback_periods` | int, *default 25* | Number of periods (`N`) for the lookback evaluation.  Must be greater than 0.

<!-- 
## Usage
```python
from stock_indicators import indicators

results = indicators.get_aroon(quotes, lookback_periods)
``` -->


### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
AroonResult[AroonResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values for `Aroon` since there's not enough data to calculate.

### AroonResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `aroon_up` | Decimal, Optional | Based on last High price
| `aroon_down` | Decimal, Optional | Based on last Low price
| `oscillator` | Decimal, Optional | AroonUp - AroonDown

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

results = indicators.get_aroon(quotes, lookback_periods)
```

## About: {{ page.title }}

Created by Tushar Chande, [Aroon](https://school.stockcharts.com/doku.php?id=technical_indicators:aroon) is a oscillator view of how long ago the new high or low price occured over a lookback window.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/266 "Community discussion about this indicator")

![image]({{site.charturl}}/Aroon.png)

### Sources

- [C# core]({{site.base_sourceurl}}/a-d/Aroon/Aroon.cs)
- [Python wrapper]({{site.sourceurl}}/aroon.py)
