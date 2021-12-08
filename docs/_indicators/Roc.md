---
title: Rate of Change (ROC)
description: Rate of Change (ROC), Momentum Oscillator, and ROC with Bands
permalink: /indicators/Roc/
type: price-characteristic
layout: indicator
---
# {{ page.title }}
<hr>

## **get_roc**(*quotes, lookback_periods, sma_periods=None*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `lookback_periods` | int | Number of periods (`N`) to go back.  Must be greater than 0.
| `sma_periods` | int, Optional | Number of periods in the moving average of ROC.  Must be greater than 0, if specified.

### Historical quotes requirements

You must have at least `N+1` periods of `quotes`.

`quotes` is an `Iterable[Type[Quote]]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Returns

```python
ROCResults[ROCResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N` periods will have `None` values for ROC since there's not enough data to calculate.

### ROCResult

| name | type | notes
| -- |-- |--
| `date` | datetime.datetime | Date
| `roc` | decimal.Decimal | Rate of Change over `N` lookback periods (%, not decimal)
| `roc_sma` | decimal.Decimal | Moving average (SMA) of ROC based on `sma_periods` periods, if specified

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

# calculate 20-period ROC
results = indicators.get_roc(quotes, 20)
```

# ROC with Bands
<hr>

## **get_roc_with_band**(*quotes, lookback_periods, ema_periods, std_dev_periods*)

## Parameters with Bands

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Type[Quote]] | Iterable(such as list or an object having `__iter__()`) of the Quote class or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `lookback_periods` | int | Number of periods (`N`) to go back.  Must be greater than 0.  Typical values range from 10-20.
| `ema_periods` | int | Number of periods for the ROC EMA line.  Must be greater than 0.  Standard is 3.
| `std_dev_periods` | int | Number of periods the standard deviation for upper/lower band lines.  Must be greater than 0 and not more than `lookback_periods`.  Standard is to use same value as `lookback_periods`.

## Returns

```python
ROCWBResults[ROCWBResult]
```

### ROCWBResult

| name | type | notes
| -- |-- |--
| `date` | datetime.datetime | Date
| `roc` | decimal.Decimal | Rate of Change over `N` lookback periods (%, not decimal)
| `roc_ema` | decimal.Decimal | Exponential moving average (EMA) of `roc`
| `upper_band` | decimal.Decimal | Upper band of ROC (overbought indicator)
| `lower_band` | decimal.Decimal | Lower band of ROC (oversold indicator)


## About {{ page.title }}

[Rate of Change](https://en.wikipedia.org/wiki/Momentum_(technical_analysis)), also known as Momentum Oscillator, is the percent change of Close price over a lookback window.  A [Rate of Change with Bands](#roc-with-bands) variant, created by Vitali Apirine, is also included.
[[Discuss] :speech_balloon:]({{site.github.repository_url}}/discussions/242 "Community discussion about this indicator")

![image]({{site.charturl}}/Roc.png)

### ROC with Bands

![image]({{site.charturl}}/RocWb.png)


### Sources

- [C# core]({{site.base_sourceurl}}/m-r/Roc/Roc.cs)
- [Python wrapper]({{site.sourceurl}}/roc.py)
