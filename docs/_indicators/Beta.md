---
title: Beta Coefficient
description: Beta Coefficient with Beta+/Beta-
permalink: /indicators/Beta/
type: numerical-analysis
layout: indicator
---

# {{ page.title }}
<hr>

## **get_beta**(*market_history, eval_history, lookback_periods*)

## Parameters

| name | type | notes
| -- |-- |--
| `market_history` | Iterable[Type[Quote]] | Historical [market] Quotes data should be at any consistent frequency (day, hour, minute, etc).  This `market` quotes will be used to establish the baseline.
| `eval_history` | Iterable[Type[Quote]] | Historical [evaluation stock] Quotes data should be at any consistent frequency (day, hour, minute, etc).
| `lookback_periods` | int | Number of periods (`N`) in the lookback period.  Must be greater than 0 to calculate; however we suggest a larger period for statistically appropriate sample size and especially when using Beta +/-.

<!-- | `type` | BetaType | Type of Beta to calculate.  Default is `BetaType.Standard`. See [BetaType options](#betatype-options) below. -->

### Historical quotes requirements

You must have at least `N` periods of quotes.  You must have at least the same matching date elements of `market_history`.  Exception will be thrown if not matched.  Historical price quotes should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

<!-- #### BetaType options

| type | description
|-- |--
| `Standard` | Standard Beta only.  Uses all historical quotes.
| `Up` | Upside Beta only.  Uses historical quotes from market up bars only.
| `Down` | Downside Beta only.  Uses historical quotes from market down bars only.
| `All` | Returns all of the above.  Use this option if you want `Ratio` and `Convexity` values returned.  Note: 3× slower to calculate. -->

## Returns

```python
BetaResults[BetaResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first `N-1` periods will have `None` values since there's not enough data to calculate.

### BetaResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `beta` | float, Optional | Beta coefficient based on `N` lookback periods

<!-- | `BetaUp` | decimal | Beta+ (Up Beta)
| `BetaDown` | decimal | Beta- (Down Beta)
| `Ratio` | decimal | Beta ratio is `BetaUp/BetaDown`
| `Convexity` | decimal | Beta convexity is <code>(BetaUp-BetaDown)<sup>2</sup></code> -->

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods()]({{site.baseurl}}/utilities#remove-warmup-periods)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
history_SPX = get_history_from_feed("SPX")
history_TSLA = get_history_from_feed("TSLA")

# calculate 20-period Beta coefficient
results = indicators.get_beta(history_SPX, history_TSLA, 20)
```

## About: {{ page.title }}

[Beta](https://en.wikipedia.org/wiki/Beta_(finance)) shows how strongly one stock responds to systemic volatility of the entire market.  [Upside Beta](https://en.wikipedia.org/wiki/Upside_beta) (Beta+) and [Downside Beta](https://en.wikipedia.org/wiki/Downside_beta) (Beta-), [popularized by Harry M. Markowitz](https://www.jstor.org/stable/j.ctt1bh4c8h), are also included.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/268 "Community discussion about this indicator")

![image]({{site.charturl}}/Beta.png)

### Sources

- [C# core]({{site.base_sourceurl}}/a-d/Beta/Beta.cs)
- [Python wrapper]({{site.sourceurl}}/beta.py)
