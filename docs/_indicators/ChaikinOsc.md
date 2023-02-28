---
title: Chaikin Oscillator
permalink: /indicators/ChaikinOsc/
type: volume-based
layout: indicator
---

# {{ page.title }}

<hr>

## **get_chaikin_osc**(*quotes, fast_periods=3, slow_periods=10*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `fast_periods` | int, *default 3* | Number of periods (`F`) in the ADL fast EMA.  Must be greater than 0 and smaller than `S`.
| `slow_periods` | int, *default 10* | Number of periods (`S`) in the ADL slow EMA.  Must be greater `F`.

### Historical quotes requirements

You must have at least `2×S` or `S+100` periods of `quotes`, whichever is more, to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `S+250` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
ChaikinOscResults[ChaikinOscResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ChaikinOscResults` is just a list of `ChaikinOscResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `S-1` periods will have `None` values for `Oscillator` since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `S+100` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ChaikinOscResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `money_flow_multiplier` | float, Optional | Money Flow Multiplier
| `money_flow_volume` | float, Optional | Money Flow Volume
| `adl` | float, Optional | Accumulation Distribution Line (ADL)
| `oscillator` | float, Optional | Chaikin Oscillator

> :warning: **Warning**: absolute values in MFV, ADL, and Oscillator are somewhat meaningless.  Use with caution.

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

# Calculate 20-period Chaikin Oscillator
results = indicators.get_chaikin_osc(quotes, 20)
```

## About {{ page.title }}

Created by Marc Chaikin, the [Chaikin Oscillator](https://en.wikipedia.org/wiki/Chaikin_Analytics#Chaikin_Oscillator) is the difference between fast and slow Exponential Moving Averages (EMA) of the [Accumulation/Distribution Line](../Adl#content) (ADL).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/264 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ChaikinOsc.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/ChaikinOsc/ChaikinOsc.Series.cs)
- [Python wrapper]({{site.sourceurl}}/chaikin_oscillator.py)
