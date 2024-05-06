---
title: Stochastic Oscillator
description: Stochastic Oscillator and KDJ Index
permalink: /indicators/Stoch/
type: oscillator
layout: indicator
---

# {{ page.title }}

><span class="indicator-syntax">**get_stoch**(*quotes, lookback_periods=14, signal_periods=3, smooth_periods=3, k_factor=3, d_factor=2, ma_type=MAType.SMA*)</span>

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [See here]({{site.baseurl}}/guide/#using-pandasdataframe) for usage with pandas.DataFrame</span>
| `lookback_periods` | int, *default 14* | Lookback period (`N`) for the oscillator (%K).  Must be greater than 0.
| `signal_periods` | int, *default 3* | Smoothing period for the signal (%D).  Must be greater than 0.
| `smooth_periods` | int, *default 3* | Smoothing period (`S`) for the Oscillator (%K).  "Slow" stochastic uses 3, "Fast" stochastic uses 1.  Must be greater than 0.
| `k_factor` | int, *default 3* | Weight of %K in the %J calculation.  Must be greater than 0.
| `d_factor` | int, *default 2* | Weight of %D in the %J calculation.  Must be greater than 0.
| `ma_type` | MAType, *default MAType.SMA* | Type of moving average (SMA or SMMA) used for smoothing.  See [MAType options](#matype-options) below.

### Historical quotes requirements

You must have at least `N+S` periods of `quotes` to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### MAType options

```python
from stock_indicators.indicators.common.enums import MAType
```

| type | description
|-- |--
| `MAType.SMA` | [Simple Moving Average]({{site.baseurl}}/indicators/Sma#content) (default)
| `MAType.SMMA` | [Smoothed Moving Average]({{site.baseurl}}/indicators/Smma#content)

## Returns

```python
StochResults[StochResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `StochResults` is just a list of `StochResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N+S-2` periods will have `None` Oscillator values since there's not enough data to calculate.

>&#9886; **Convergence warning**: The first `N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods when using `MAType.SMMA`.  Standard use of `MAType.SMA` does not have convergence-related precision errors.

### StochResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `oscillator` or `k` | float, Optional | %K Oscillator over prior `N` lookback periods
| `signal` or `d` | float, Optional | %D Simple moving average of Oscillator
| `percent_j` or `j` | float, Optional | %J is the weighted divergence of %K and %D: `%J=kFactor×%K-dFactor×%D`

Note: aliases of `k`, `d`, and `j` are also provided.  They can be used interchangeably with the standard outputs.

### Utilities

- [.condense()]({{site.baseurl}}/utilities#condense)
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_historical_quotes("SPY")

# calculate STO %K(14),%D(3) (slow)
results = indicators.get_stoch(quotes, 14, 3, 3)
```

## About {{ page.title }}

Created by George Lane, the [Stochastic Oscillator](https://en.wikipedia.org/wiki/Stochastic_oscillator) is a momentum indicator that looks back `N` periods to produce a scale of 0 to 100.  %J is also included for the KDJ Index extension.
[[Discuss] &#128172;]({{site.dotnet.repo}}/discussions/237 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Stoch.png)

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Stoch/Stoch.Series.cs)
- [Python wrapper]({{site.python.src}}/stoch.py)
