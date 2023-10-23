---
title: Detrended Price Oscillator (DPO)
permalink: /indicators/Dpo/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_dpo**(*quotes, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 0.

### Historical quotes requirements

You must have at least `N` historical quotes to cover the warmup periods.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
DPOResults[DPOResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `DPOResults` is just a list of `DPOResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N/2-2` and last `N/2+1` periods will be `None` since they cannot be calculated.

### DPOResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `sma` | float, Optional | Simple moving average offset by `N/2+1` periods
| `dpo` | float, Optional | Detrended Price Oscillator (DPO)

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

# Calculate
results = indicators.get_dpo(quotes, 14)
```

## About {{ page.title }}

[Detrended Price Oscillator](https://en.wikipedia.org/wiki/Detrended_price_oscillator) depicts the difference between price and an offset simple moving average.  It is used to identify trend cycles and duration.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/551 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Dpo.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Dpo/Dpo.Series.cs)
- [Python wrapper]({{site.sourceurl}}/dpo.py)
