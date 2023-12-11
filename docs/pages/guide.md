---
title: Guide and Pro tips
description: Learn how to use the Stock Indicators for Python PyPI library in your own software tools and platforms.  Whether you're just getting started or an advanced professional, this guide explains how to get setup, example usage code, and instructions on how to use historical price quotes, make custom quote classes, chain indicators of indicators, and create custom technical indicators.
permalink: /guide/
relative_path: pages/guide.md
layout: page
---

# {{ page.title }}

- [Installation and setup](#installation-and-setup)
- [Prerequisite data](#prerequisite-data)
- [Example usage](#example-usage)
- [Historical quotes](#historical-quotes)
- [Using custom quote classes](#using-custom-quote-classes)
- [Using derived results classes](#using-derived-results-classes)
- [Generating indicator of indicators](#generating-indicator-of-indicators)
- [Candlestick patterns](#candlestick-patterns)
- [Utilities and Helper functions]({{site.baseurl}}/utilities/#content)
- [Contributing guidelines]({{site.baseurl}}/contributing/#content)

## Getting started

### Installation and setup

Stock Indicators for Python has dependency on [PythonNet](https://github.com/pythonnet/pythonnet), which uses [CLR(Common Language Runtime)](https://learn.microsoft.com/dotnet/standard/clr).
Check that you have CLR installed. It currently supports **.NET 6 or above**. Note that, the latest CLR has better performance on it.

- [download and install the latest .NET](https://dotnet.microsoft.com/download/dotnet)

Find and install the **stock-indicators** Python package into your environment. See [more help](https://packaging.python.org/en/latest/tutorials/installing-packages/) for installing packages.

```bash
# pip example
pip install stock-indicators
```

### Prerequisite data

Most indicators require that you provide historical quote data and additional configuration parameters.

You must get historical quotes from your own market data provider.  For clarification, the `get_history_from_feed()` method shown in the example below and throughout our documentation **is not part of this library**, but rather an example to represent your own acquisition of historical quotes.

Historical price data can be provided as an `Iterable`(such as `List` or an object having `__iter__()`) of the `Quote` class or its sub-class ([see below](#historical-quotes)); Be aware that you **have to** inherit `Quote` class when you [make custom quote class](#using-custom-quote-classes).

<!-- however, it can also be supplied as a generic [custom TQuote type](#using-custom-quote-classes) if you prefer to use your own quote model. -->

For additional configuration parameters, default values are provided when there is an industry standard.  You can, of course, override these and provide your own values.

### Example usage

All indicator methods will produce all possible results for the provided historical quotes as a time series dataset -- it is not just a single data point returned.  For example, if you provide 3 years worth of historical quotes for the SMA method, you'll get 3 years of SMA result values.

```python
from stock_indicators import indicators

# fetch historical quotes from your feed (your method)
quotes = get_historical_quotes("MSFT")

# calculate 20-period SMA
results = indicators.get_sma(quotes, 20)

# use results as needed for your use case (example only)
for r in results:
    print(f"SMA on {r.date.date()} was ${r.sma or 0:.4f}")

```

```console
SMA on 2018-04-19 was $255.0590
SMA on 2018-04-20 was $255.2015
SMA on 2018-04-23 was $255.6135
SMA on 2018-04-24 was $255.5105
SMA on 2018-04-25 was $255.6570
SMA on 2018-04-26 was $255.9705
..
```

See [individual indicator pages]({{site.baseurl}}/indicators/) for specific usage guidance.

More examples available:

- [Demo site](https://stock-charts.azurewebsites.net) (a stock chart)

## Historical quotes

You must provide historical price quotes to the library in the standard [OHLCV](https://acronyms.thefreedictionary.com/OHLCV) `Iterable[Quote]`(such as a list of `Quote`) format.  It should have a consistent period frequency (day, hour, minute, etc).

<!-- ### stock_indicators.indicators.common.quote.**Quote** -->
```python
from stock_indicators.indicators.common.quote import Quote
```

**class Quote(date, open=None, high=None, low=None, close=None, volume=None)**
[[source]](https://github.com/DaveSkender/Stock.Indicators.Python/blob/main/stock_indicators/indicators/common/quote.py)

| name | type | notes
| -- |-- |--
| date | [`datetime.datetime`](https://docs.python.org/3.8/library/datetime.html#datetime.datetime) | Date
| open | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Open price
| high | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | High price
| low | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Low price
| close | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Close price
| volume | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Volume

**Note that**

1. `date` is always required, while each ohlcv values are optional.
2. ohlcv can be provided by `float`, `Decimal` and `str` representing number, but these are always stored as `Decimal`.

### Where can I get historical quote data?

There are many places to get stock market data.  Check with your brokerage or other commercial sites.  If you're looking for a free developer API, see our ongoing [discussion on market data]({{site.dotnet.repo}}/discussions/579) for ideas.

### How much historical quote data do I need?

Each indicator will need different amounts of price `quotes` to calculate.  You can find guidance on the individual indicator documentation pages for minimum requirements; however, **most use cases will require that you provide more than the minimum**.  As a general rule of thumb, you will be safe if you provide 750 points of historical quote data (e.g. 3 years of daily data).  A `BadQuotesException` will be thrown if you do not provide sufficient historical quotes to produce any results.

> :warning: IMPORTANT! Some indicators use a smoothing technique that converges to better precision over time.  While you can calculate these with the minimum amount of quote data, the precision to two decimal points often requires 250 or more preceding historical records.

For example, if you are using daily data and want one year of precise EMA(250) data, you need to provide 3 years of historical quotes (1 extra year for the lookback period and 1 extra year for convergence); thereafter, you would discard or not use the first two years of results.  Occassionally, even more is required for optimal precision.

### Using Pandas.Dataframe

If you are using `Pandas.Dataframe` to hold quote data, you have to convert it into our `Quote` instance. That means you must iterate them row by row. There's [an awesome article](https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01) that introduces the best-efficiency way to iterate `Dataframe`.

Here's an example we'd like to suggest: **Use list comprehension**

```python
# Suppose that you have dataframe like the below.
#             date    open    high     low   close     volume
# 0     2018-12-31  244.92  245.54  242.87  245.28  147031456
# 1     2018-12-28  244.94  246.73  241.87  243.15  155998912
# 2     2018-12-27  238.06  243.68  234.52  243.46  189794032
# ...          ...     ...     ...     ...     ...        ...

from stock_indicators import Quote

quotes_list = [
    Quote(d,o,h,l,c,v) 
    for d,o,h,l,c,v 
    in zip(df['date'], df['open'], df['high'], df['low'], df['close'], df['volume'])
]
```

You can also use `numpy.vectorize()`, its gain is too slight and hard to apply in this case.

### Using custom quote classes

If you would like to use your own custom `MyCustomQuote` _quote_ class, you **have to** inherit `Quote` class. The `Quote` class is a special class which converts OHLCV properties existing as Python objects to C# objects and which is concrete class of `IQuote` of C# implementation. It enables Pythonnet to work with our C# implementation using generics.

```python
from stock_indicators.indicators.common import Quote

class MyCustomQuote(Quote):
    def foo(self): ...
    ... add your own attributes.

```

```python
from stock_indicators import indicators

# fetch historical quotes from your favorite feed
quotes: Iterable[MyCustomQuote] = get_history_from_feed("MSFT");

# example: get 20-period simple moving average
results = indicators.get_sma(quotes, 20);
```

#### Using custom quote property names

If you have a model that has different properties names, but the same meaning, you only need to map them. Each properties is `property` object, so you can just reference them.

Suppose your class has a property called `close_date` instead of `date`, it could be represented like this:

```python
from stock_indicators.indicators.common.quote import Quote

class MyCustomQuote(Quote):
    close_date = Quote.date

```

Note that the property `date` now can be accessed by both `close_date` and `date`.

## Using derived results classes

The indicator result (e.g. `EMAResult`) classes can be extended in your code.

Here's an example of how you'd set that up:

```python
from stock_indicators import indicators
from stock_indicators.indicators.ema import EMAResult

class ExtendedEMA(EMAResult):
    def __str__(self):
        return f"EMA on {self.date.date()} was ${self.ema or 0:.4f}"
    
# compute indicator
quotes = get_history_from_feed("MSFT")
results = indicators.get_ema(quotes, 20)

# 1. list[ExtendedEMA]
extended_results = [ ExtendedEMA(r._csdata) for r in results ]
for r in extended_results:
    print(r)
```

**Be aware that** If you want to use [helper functions]({{site.baseurl}}/utilities/#utilities-for-indicator-results), use wrapper class(e.g. `EMAResults`).<br>

```python
# 2. use wrapper for helper function
from stock_indicators.indicators.ema import EMAResults

extended_results = EMAResults[ExtendedEMA](results._csdata, ExtendedEMA)
pruned_results = extended_results.remove_warmup_periods()
for r in pruned_results:
    print(r)
```

<!-- ### Using nested results classes

If you prefer nested classes, here's an alternative method for customizing your results:<br>
(Wrapper class is not available for nested result class.)

```python
from stock_indicators import indicators

class NestedEMA:
    def __init__(self, ema_result):
        self.id = "123"
        self.result = ema_result
    
    def __str__(self):
        return f"EMA on {self.result.date.date()} was ${self.result.ema or 0:.4f}"

# compute indicator
quotes = get_history_from_feed("MSFT")
results = indicators.get_ema(quotes, 20)

nested_results = [ NestedEMA(r) for r in results ]
for r in nested_results:
    print(r)

``` -->

## Generating indicator of indicators

If you want to compute an indicator of indicators, such as an SMA of an ADX or an [RSI of an OBV](https://medium.com/@robswc/this-is-what-happens-when-you-combine-the-obv-and-rsi-indicators-6616d991773d), all you need to do is to take the results of one, reformat into a synthetic historical quotes, and send it through to another indicator.

<!-- MEMO: This example is for to_quotes(), deprecated. -->
<!-- Here's an example of SMA of RSI:

```python
from stock_indicators import indicators

# fetch historical quotes from your feed (your method)
quotes = get_history_from_feed("MSFT")

# calculate SMA of RSI
results = indicators.get_rsi(quotes)
quotes_from_rsi = results.to_quotes()
sma_of_rsi = indicators.get_sma(quotes_from_rsi, 20)

``` -->

~~See [.to_quotes()]({{site.baseurl}}/utilities/#convert-to-quotes) for more information.~~
The .to_quotes() method is deprecated. (since v0.8.0)

A workaround is to convert yourself.

```python
from stock_indicators import indicators

# fetch historical quotes from your feed (your method)
quotes = get_history_from_feed("MSFT")

# calculate EMA
results = indicators.get_ema(quotes, 20)

# convert to synthetic quotes
quotes_from_ema = [ Quote(date=r.date, close=r.ema) for r in results ]

# calculate SMA of EMA
sma_of_ema = indicators.get_sma(quotes_from_ema, 20)

```

## Candlestick patterns

[Candlestick Patterns]({{site.baseurl}}/indicators/#candlestick-pattern) are a unique form of indicator and have a common output model.

{% include candle-result.md %}

### Match

When a candlestick pattern is recognized, it produces a match.  In some cases, an intrinsic confirmation is also available.  In cases where previous bars were used to identify a pattern, they are indicated as the basis for the match. [Documentation for each candlestick pattern]({{site.baseurl}}/indicators/#candlestick-pattern) will indicate whether confirmation and/or basis information is produced.

```python
from stock_indicators.indicators.common.enums import Match
```

| type | description
|-- |:--
| `Match.BULL_CONFIRMED` | Confirmation of a prior bull Match
| `Match.BULL_SIGNAL` | Matching bullish pattern
| `Match.BULL_BASIS` | Bars supporting a bullish Match
| `Match.NEUTRAL` | Matching for non-directional patterns
| `Match.NONE` | No match
| `Match.BEAR_BASIS` | Bars supporting a bearish Match
| `Match.BEAR_SIGNAL` | Matching bearish pattern
| `Match.BEAR_CONFIRMED` | Confirmation of a prior bear Match

### Candle

The `CandleProperties` class is an extended version of `Quote`, and contains additional calculated properties.

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `open` | Decimal | Open price
| `high` | Decimal | High price
| `low` | Decimal | Low price
| `close` | Decimal | Close price
| `volume` | Decimal | Volume
| `size` | Decimal, Optional | `high-low`
| `body` | Decimal, Optional | `|open-close|`
| `upper_wick` | Decimal, Optional | Upper wick size
| `lower_wick` | Decimal, Optional | Lower wick size
| `body_pct` | float, Optional | `body/size`
| `upper_wick_pct` | float, Optional | `upper_wick/size`
| `lower_wick_pct` | float, Optional | `lower_wick/size`
| `is_bullish` | bool | `close>open` direction
| `is_bearish` | bool | `close<open` direction

## Utilities

See [Utilities and helper functions]({{site.baseurl}}/utilities/#content) for additional tools.
