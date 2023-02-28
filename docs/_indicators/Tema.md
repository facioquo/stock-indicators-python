---
title: Triple Exponential Moving Average (TEMA)
permalink: /indicators/Tema/
type: moving-average
layout: indicator
---

# {{ page.title }}

<hr>

## **get_tema**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `4×N` or `3×N+100` periods of `quotes`, whichever is more, to cover the warmup periods.  Since this uses a smoothing technique, we recommend you use at least `3×N+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
TEMAResults[TEMAResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `TEMAResults` is just a list of `TEMAResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `3×N-2` periods will have `None` values since there's not enough data to calculate.  Also note that we are using the proper [weighted variant](https://en.wikipedia.org/wiki/Triple_exponential_moving_average) for TEMA.  If you prefer the unweighted raw 3 EMAs value, please use the `Ema3` output from the [TRIX](../Trix#content) oscillator instead.

> :hourglass: **Convergence warning**: The first `3×N+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### TEMAResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `tema` | float, Optional | Triple exponential moving average

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

# calculate 20-period TEMA
results = indicators.get_tema(quotes, 20)
```

## About {{ page.title }}

[Triple exponential moving average](https://en.wikipedia.org/wiki/Triple_exponential_moving_average) of the Close price over a lookback window.
Note: TEMA is often confused with the alternative [TRIX](../Trix#content) oscillator.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/256 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Tema.png)

See related [EMA](../Ema#content) and [Double EMA](../Dema#content).

### Sources

- [C# core]({{site.dotnet.src}}/s-z/Tema/Tema.Series.cs)
- [Python wrapper]({{site.sourceurl}}/tema.py)
