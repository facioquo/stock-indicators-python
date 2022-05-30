---
title: Renko Chart
permalink: /indicators/Renko/
type: price-transform
layout: indicator
---

# {{ page.title }}
<hr>

## **get_renko**(*quotes, brick_size, end_type=EndType.CLOSE*)

## Parameters

| name | type | notes
| -- |-- |--
| `quotes` | Iterable[Quote] | Iterable(such as list or an object having `__iter__()`) of the [Quote class]({{site.baseurl}}/guide/#historical-quotes) or [its sub-class]({{site.baseurl}}/guide/#using-custom-quote-classes).
| `brick_size` | float | Brick size.  Must be greater than 0.
| `end_type` | EndType, *default EndType.CLOSE* | See [EndType options](#endtype-options) below.

### Historical quotes requirements

You must have at least two periods of `quotes` to cover the warmup periods; however, more is typically provided since this is a chartable candlestick pattern.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

### EndType options

| type | description
|-- |--
| `CLOSE` | Brick change threshold measured from `close` price (default)
| `HIGH_LOW` | Brick change threshold measured from `high` and `low` price

## Return

```python
RenkoResults[RenkoResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `RenkoResults` is just a list of `RenkoResult`.
- It does not return a single incremental indicator value.

<!-- - `RenkoResult` is based on `IQuote`, so it can be used as a direct replacement for `quotes`.  In other words, you can use it as base quotes for other indicators. Example:

  ```csharp
  var renkoQuotes = quotes.GetRenko(..);
  var renkoRsi = renkoQuotes.GetRsi(..);
  ``` -->

:warning: WARNING!  Unlike most indicators in this library, this indicator DOES NOT return the same number of elements as there are in the historical quotes.  Renko bricks are added to the results once the `brick_size` change is achieved.  For example, if it takes 3 days for a $2.50 price change to occur an entry is made on the third day while the first two are skipped.  If a period change occurs at multiples of `brick_size`, multiple bricks are drawn with the same `date`.  See [online documentation](https://www.investopedia.com/terms/r/renkochart.asp) for more information.

### RenkoResult

Each result record represents one Renko brick.

| name | type | notes
| -- |-- |--
| `date` | datetime | Formation date of brick(s)
| `open` | Decimal | Brick open price
| `high` | Decimal | Highest high during elapsed quotes periods
| `low` | Decimal | Lowest low during elapsed quotes periods
| `close` | Decimal | Brick close price
| `volume` | Decimal | Sum of Volume over elapsed quotes periods
| `is_up` | bool | Direction of brick (true=up,false=down)

:warning: WARNING! When multiple bricks are drawn from a single `quote` period, the extra information about `high` and `low` wicks and `volume` is potentially confusing to interpret.  `high` and `low` wicks will be the same across the multiple bricks; and `volume` is portioning evenly across the number of bricks.  For example, if within one `quote` period 3 bricks are drawn, the `volume` for each brick will be `(sum of quotes Volume since last brick) / 3`.

### Utilities

- ~~[.to_quotes()]({{site.baseurl}}/utilities#convert-to-quotes)~~ <code style='color: #f32faf; important'>[deprecated]</code>
- [.find(lookup_date)]({{site.baseurl}}/utilities#find-indicator-result-by-date)
- [.remove_warmup_periods(qty)]({{site.baseurl}}/utilities#remove-warmup-periods)

See [Utilities and Helpers]({{site.baseurl}}/utilities#utilities-for-indicator-results) for more information.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate
results = indicators.get_renko(quotes, 2.5);
```

## ATR Variant

## **get_renko_atr**(*quotes, atr_periods, end_type=EndType.CLOSE*)

### Parameters for ATR

| name | type | notes
| -- |-- |--
| `atr_periods` | int | Number of lookback periods (`A`) for ATR evaluation.  Must be greater than 0.
| `end_type` | EndType, *default EndType.CLOSE* | See [EndType options](#endtype-options).

#### Historical quotes requirements for ATR

You must have at least `A+100` periods of `quotes`.

`quotes` is an `Iterable[Quote]` collection of historical price quotes.  It should have a consistent frequency (day, hour, minute, etc).  See [the Guide]({{site.baseurl}}/guide/#historical-quotes) for more information.

## Return for ATR

```python
RenkoResults[RenkoResult]
```

- This method returns a time series of all available indicator values for the `quotes` provided.
- `RenkoResults` is just a list of `RenkoResult`.
- It always returns the same number of elements as there are in the historical quotes.
- It does not return a single incremental indicator value.

:paintbrush: **Repaint Warning**: When using the `get_renko_atr()` variant, the last [Average True Range (ATR)](../Atr/#content) value is used to set `brick_size`.  Since the ATR changes over time, historical bricks will be repainted as new periods are added or updated in `quotes`.

## Example

```python
from stock_indicators import indicators

# This method is NOT a part of the library.
quotes = get_history_from_feed("SPY")

# Calculate
results = indicators.get_renko_atr(quotes, atr_periods);
```

## About: {{ page.title }}

The [Renko Chart](https://en.m.wikipedia.org/wiki/Renko_chart) is a Japanese price transformed candlestick pattern that uses "bricks" to show a defined increment of change over a non-linear time series.  Transitions can use either `close` or `high/low` price values.  An [ATR variant](#atr-variant) is also provided where brick size is determined by Average True Range values.
[[Discuss] :speech_balloon:]({{site.github.base_repository_url}}/discussions/478 "Community discussion about this indicator")

![image]({{site.charturl}}/Renko.png)

### Sources

- [C# core]({{site.base_sourceurl}}/m-r/Renko/Renko.cs)
- [Python wrapper]({{site.sourceurl}}/renko.py)
