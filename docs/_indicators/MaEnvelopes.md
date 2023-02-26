---
title: Moving Average Envelopes
permalink: /indicators/MaEnvelopes/
type: price-channel
layout: indicator
---

# {{ page.title }}

<hr>

## **get_ma_envelopes**(*quotes, lookback_periods, percent_offset=2.5, ma_type=MAType.SMA*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes). <br><span class='qna-dataframe'> • [Need help with pandas.DataFrame?]({{site.baseurl}}/guide/#using-pandasdataframe)</span>
| `lookback_periods` | int | Number of periods (`N`) in the moving average.  Must be greater than 1.
| `percent_offset` | float, *default 2.5* | Percent offset for envelope width.  Example: 3.5% would be entered as 3.5 (not 0.035).  Must be greater than 0.  Typical values range from 2 to 10.
| `ma_type` | MAType, *default MAType.SMA* | Type of moving average (e.g. SMA, EMA, HMA).  See [MAType options](#matype-options) below.

### Historical quotes requirements

See links in the supported [MAType options](#matype-options) section below for details on the inherited requirements for `quotes` and `lookback_periods`.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### MAType options

```python
from stock_indicators.indicators.common.enums import MAType
```

| type | description
|-- |--
| `MAType.ALMA` | [Arnaud Legoux Moving Average](../Alma#content)
| `MAType.DEMA` | [Double Exponential Moving Average](../Dema#content)
| `MAType.EPMA` | [Endpoint Moving Average](../Epma#content)
| `MAType.EMA` | [Exponential Moving Average](../Ema#content)
| `MAType.HMA` | [Hull Moving Average](../Hma#content)
| `MAType.SMA` | [Simple Moving Average](../Sma#content) (default)
| `MAType.SMMA` | [Smoothed Moving Average](../Smma#content)
| `MAType.TEMA` | [Triple Exponential Moving Average](../Tema#content)
| `MAType.WMA` | [Weighted Moving Average](../Wma#content)

> :warning:  **Warning**: For ALMA, default values are used for `offset` and `sigma`.

## Return

```python
MAEnvelopeResults[MAEnvelopeResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `MAEnvelopeResults` is just a list of `MAEnvelopeResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.
- The first periods will have `None` values since there's not enough data to calculate; the quantity will vary based on the `ma_type` specified.

> :hourglass: **Convergence Warning**: Some moving average variants have decreasing magnitude, convergence-related precision errors that can be as high as ~5% deviation in indicator values for earlier periods.  See links in the supported [MAType options](#matype-options) section above for more information.

### MaEnvelopeResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `center_line` | float, Optional | Moving average
| `upper_envelope` | float, Optional | Upper envelope band
| `lower_envelope` | float, Optional | Lower envelope band

The moving average `center_line` is based on the `ma_type` type specified.

### Utilities

- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators
from stock_indicators import MAType     # Short path, version >= 0.8.1

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate 20-period SMA envelopes with 2.5% offset
results = indicators.get_ma_envelopes(quotes, 20, 2.5, MAType.SMA);
```

## About {{ page.title }}

[Moving Average Envelopes](https://en.wikipedia.org/wiki/Moving_average_envelope) is a price band overlay that is offset from the moving average of Close price over a lookback window.
[[Discuss] :speech_balloon:]({{site.dotnet.repo}}/discussions/288 "Community discussion about this indicator")

![image]({{site.dotnet.charts}}/MaEnvelopes.png)

### Sources

- [C# core]({{site.dotnet.src}}/m-r/MaEnvelopes/MaEnvelopes.Series.cs)
- [Python wrapper]({{site.sourceurl}}/ma_envelopes.py)
