---
title: Doji (Preview)
permalink: /indicators/Doji/
layout: indicator
type: candlestick-pattern
---

# {{ page.title }}

<hr>

## **get_doji**(*quotes, max_price_change_percent=0.1*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `max_price_change_percent` | float, *default 0.1* | Optional.  Maximum absolute percent difference in open and close price.  Example: 0.3% would be entered as 0.3 (not 0.003).  Must be between 0 and 0.5 percent, if specified.

### Historical quotes requirements

You must have at least one historical quote; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
CandleResults[CandleResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `CandleResults` is just a list of `CandleResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The candlestick pattern is indicated on dates where `match` is `Match.NEUTRAL`.
- `price` is `close` price; however, all OHLC elements are included in the `candle` properties.
- There is no intrinsic basis or confirmation Match provided for this pattern.

{% include candle-result.md %}

### Utilities

- [.condense()]({{site.baseurl}}/utilities#condense)
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate
results = indicators.get_doji(quotes);
```

## About {{ page.title }}

[Doji](https://en.wikipedia.org/wiki/Doji) is a single candlestick pattern where open and close price are virtually identical, representing market indecision.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/734 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Doji.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Doji/Doji.Series.cs)
- [Python wrapper]({{site.sourceurl}}/doji.py)
