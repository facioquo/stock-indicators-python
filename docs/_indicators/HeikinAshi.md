---
title: Heikin-Ashi
permalink: /indicators/HeikinAshi/
type: price-transform
layout: indicator
---

# {{ page.title }}

<hr>

## **get_heikin_ashi**(*quotes*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>

### Historical quotes requirements

You must have at least two periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
HeikinAshiResults[HeikinAshiResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `HeikinAshiResults` is just a list of `HeikinAshiResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first period will have `None` values since there's not enough data to calculate.

### HeikinAshiResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `open` | Decimal | Modified open price
| `high` | Decimal | Modified high price
| `low` | Decimal | Modified low price
| `close` | Decimal | Modified close price
| `volume` | Decimal | Volume (same as `quotes`)

### Utilities

- ~~[.to_quotes()]({{site.baseurl}}/utilities#convert-to-quotes)~~ <code style='color: #d32f2f; important'>[deprecated]</code>
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# calculate
results = indicators.get_heikin_ashi(quotes)
```

## About {{ page.title }}

Created by Munehisa Homma, [Heikin-Ashi](https://en.wikipedia.org/wiki/Candlestick_chart#Heikin-Ashi_candlesticks) is a modified candlestick pattern that uses prior day for smoothing.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/254 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/HeikinAshi.png)

### Sources

- [C# core]({{site.dotnet.src}}/e-k/HeikinAshi/HeikinAshi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/heikin_ashi.py)
