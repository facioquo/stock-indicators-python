---
title: Simple Moving Average (SMA)
permalink: /indicators/Sma/
type: moving-average
layout: indicator
---

# {{ page.title }}
<hr>

## **get_sma**(*quotes, lookback_periods, candle_part=CandlePart.CLOSE*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Got in trouble with Pandas.dataframe?]({{site.baseurl}}/guide/#using-pandasdataframe) </span>
| `lookback_periods` | int | Number of periods (`N`) in the lookback window.  Must be greater than 0.
| `candle_part` | CandlePart, *default CandlePart.CLOSE* | Specify candle part to evaluate.  See [CandlePart options](#candlepart-options) below.


### Historical quotes requirements

You must have at least `N` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

{% include candlepart-options.md %}

## Returns

```python
SMAResults[SMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `SMAResults` is just a list of `SMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### SMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sma` | Decimal, Optional | Simple moving average

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import CandlePart     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate 20-period SMA
results = indicators.get_sma(quotes, 20, CandlePart.CLOSE)
```


<hr>
# Extended analysis

An extended variant of this indicator includes additional analysis.

## **get_sma_extended**(*quotes, lookback_periods*)

## Returns

```python
SMAExtendedResults[SMAExtendedResult]
```

### SMAExtendedResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sma` | Decimal, Optional | Simple moving average
| `mad` | float, Optional | Mean absolute deviation
| `mse` | float, Optional | Mean square error
| `mape` | float, Optional | Mean absolute percentage error

## Example

```python
# usage
results = indicators.get_sma_extended(quotes, lookback_periods)
```


## About: {{ page.title }}

[Simple Moving Average](https://en.wikipedia.org/wiki/Moving_average#Simple_moving_average) is the average price over a lookback window.  An [extended analysis](#extended-analysis) option includes mean absolute deviation (MAD), mean square error (MSE), and mean absolute percentage error (MAPE).
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/240 "Community discussion about this indicator")

![image]({{site.charturl}}/Sma.png)

### Sources

- [C# core]({{site.base_sourceurl}}/s-z/Sma/Sma.cs)
- [Python wrapper]({{site.sourceurl}}/sma.py)
