---
title: ConnorsRSI
permalink: /indicators/ConnorsRsi/
type: oscillator
layout: indicator
---

# {{ page.title }}

<hr>

## **get_connors_rsi**(*quotes, rsi_periods=3, streak_periods=2, rank_periods=100*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `rsi_periods` | int, *default 3* | Lookback period (`R`) for the close price RSI.  Must be greater than 1.
| `streak_periods` | int, *default 2* | Lookback period (`S`) for the streak RSI.  Must be greater than 1.
| `rank_periods` | int, *default 100* | Lookback period (`P`) for the Percentile Rank.  Must be greater than 1.

### Historical quotes requirements

`N` is the greater of `R+100`, `S`, and `P+2`.  You must have at least `N` periods of `quotes` to cover the convergence periods.  Since this uses a smoothing technique, we recommend you use at least `N+150` data points prior to the intended usage date for better precision.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return

```python
ConnorsRSIResults[ConnorsRSIResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `ConnorsRSIResults` is just a list of `ConnorsRSIResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `MAX(R,S,P)-1` periods will have `None` values since there's not enough data to calculate.

> :hourglass: **Convergence warning**: The first `N` periods will have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.

### ConnorsRSIResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `rsi_close` | float, Optional | RSI(`R`) of the Close price.
| `rsi_streak` | float, Optional | RSI(`S`) of the Streak.
| `percent_rank` | float, Optional | Percentile rank of the period gain value.
| `connors_rsi` | float, Optional | ConnorsRSI

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

# Calculate ConnorsRsi(3,2.100)
results = indicators.get_connors_rsi(quotes, 3, 2, 100)
```

## About {{ page.title }}

Created by Laurence Connors, the [ConnorsRSI](https://alvarezquanttrading.com/wp-content/uploads/2016/05/ConnorsRSIGuidebook.pdf) is a composite oscillator that incorporates RSI, winning/losing streaks, and percentile gain metrics on scale of 0 to 100.  See [analysis](https://alvarezquanttrading.com/blog/connorsrsi-analysis).
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/260 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/ConnorsRsi.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/ConnorsRsi/ConnorsRsi.Series.cs)
- [Python wrapper]({{site.sourceurl}}/connors_rsi.py)
