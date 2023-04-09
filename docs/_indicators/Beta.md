---
title: Beta Coefficient
description: Beta Coefficient with Beta+/Beta-
permalink: /indicators/Beta/
type: numerical-analysis
layout: indicator
---

# {{ page.title }}

<hr>

## **get_beta**(*eval_history, market_quotes, lookback_periods, beta_type=BetaType.STANDARD*)

## Parameters

| name | type | notes
| -- |-- |--
| `eval_history` | Iterable[Quote] | Historical [evaluation stock] Quotes data should be at any consistent frequency (day, hour, minute, etc). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `market_history` | Iterable[Quote] | Historical [market] Quotes data should be at any consistent frequency (day, hour, minute, etc).  This `market` quotes will be used to establish the baseline.
| `lookback_periods` | int | Number of periods (`N`) in the lookback period.  Must be greater than 0 to calculate; however we suggest a larger period for statistically appropriate sample size and especially when using Beta +/-.
| `beta_type` | BetaType, *default BetaType.STANDARD* | Type of Beta to calculate.  See [BetaType options](#betatype-options) below.

### Historical quotes requirements

You must have at least `N` periods of quotes to cover the warmup periods.  You must have at least the same matching date elements of `market_history`.  Exception will be thrown if not matched.  Historical price quotes should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

#### BetaType options

```python
from stock_indicators.indicators.common.enums import BetaType
```

| type | description
|-- |--
| `STANDARD` | Standard Beta only.  Uses all historical quotes.
| `UP` | Upside Beta only.  Uses historical quotes from market up bars only.
| `DOWN` | Downside Beta only.  Uses historical quotes from market down bars only.
| `ALL` | Returns all of the above.  Use this option if you want `ratio` and `convexity` values returned.  Note: 3× slower to calculate.

## Returns

```python
BetaResults[BetaResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `BetaResults` is just a list of `BetaResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### BetaResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `beta` | float, Optional | Beta coefficient based on `N` lookback periods
| `beta_up` | float, Optional | Beta+ (Up Beta)
| `beta_down` | float, Optional | Beta- (Down Beta)
| `ratio` | float, Optional | Beta ratio is `beta_up/beta_down`
| `convexity` | float, Optional | Beta convexity is <code>(beta_up-beta_down)<sup>2</sup></code>
| `returns_eval` | float, Optional | Returns of evaluated quotes (`R`)
| `returns_mrkt` | float, Optional | Returns of market quotes (`Rm`)

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import BetaType      # Short path, version >= 0.8.1

# This method is NOT a part of the library.
history_SPX = get_history_from_feed("SPX")
history_TSLA = get_history_from_feed("TSLA")

# calculate 20-period Beta coefficient
results = indicators.get_beta(history_SPX, history_TSLA, 20, BetaType.STANDARD)
```

## About {{ page.title }}

[Beta](https://en.wikipedia.org/wiki/Beta_(finance)) shows how strongly one stock responds to systemic volatility of the entire market.  [Upside Beta](https://en.wikipedia.org/wiki/Upside_beta) (Beta+) and [Downside Beta](https://en.wikipedia.org/wiki/Downside_beta) (Beta-), [popularized by Harry M. Markowitz](https://www.jstor.org/stable/j.ctt1bh4c8h), are also included.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/268 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/Beta.png)

### Sources

- [C# core]({{site.dotnet.src}}/a-d/Beta/Beta.Series.cs)
- [Python wrapper]({{site.sourceurl}}/beta.py)
