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
- [Date and time compatibility](#date-and-time-compatibility)
- [Utilities and Helper functions]({{site.baseurl}}/utilities/#content)
- [Contributing guidelines]({{site.baseurl}}/contributing/#content)

## Getting started

### Installation and setup

1. Install prerequisite framework dependencies

    Stock Indicators for Python has dependency on on the [Common Language Runtime (CLR)](https://learn.microsoft.com/dotnet/standard/clr).  You'll need to install the .NET SDK in your environment to get required CLR capability. Check that you've installed the following prerequisite software:

    > Install **Python** and the **.NET SDK**.  Use the latest versions for better performance.

    | Installer | Min | Latest | Download |
    | --- | :---: | :---: | --- |
    | Python | 3.8 | 3.13 | [@python.org](https://www.python.org/downloads/) |
    | .NET SDK | 8.0 | 10.0 | [@microsoft.com](https://dotnet.microsoft.com/en-us/download) |

    Note: we do not support the open source [Mono .NET Framework](https://www.mono-project.com). Python 3.14+ is not yet supported due to `pythonnet` compatibility.

2. Install the **stock-indicators** Python package into your environment.

    ```bash
    # bash CLI command
    pip install stock-indicators
    ```

    > See [Python documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/) for more help with installing packages.

### Troubleshooting

#### Windows

- Ensure PATH includes .NET SDK location
- Run PowerShell as administrator if needed
- Visual Studio Build Tools may be required

#### macOS

- If you see `DOTNET_ROOT not set`:

    ```bash
    export DOTNET_ROOT="/usr/local/share/dotnet"
    ```

- For M1/M2 Macs:
  - Use ARM64 .NET SDK if available
  - Or install Rosetta 2 for x64 SDK

### Prerequisite data

Most indicators require that you provide historical quote data and additional configuration parameters.

You must get historical quotes from your own market data provider.  For clarification, the `get_historical_quotes()` method shown in the example below and throughout our documentation **is not part of this library**, but rather an example to represent your own acquisition of historical quotes.

Historical price data can be provided as an `Iterable`(such as `List` or an object having `__iter__()`) of the `Quote` class or its sub-class ([see below](#historical-quotes)); be aware that you **have to** inherit `Quote` class when you [make custom quote class](#using-custom-quote-classes).

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

> **More help**: if you're having trouble getting started, see our
> **[QuickStart guide](https://github.com/facioquo/stock-indicators-python-quickstart#readme)**
> for step-by-step instructions to setup up your environment,
> and for calculating your first indicator using this library.
>
> We also have a [demo site](https://charts.stockindicators.dev) (a stock chart) where you can visualize and experiment with different indicator settings.

## Historical quotes

You must provide historical price quotes to the library in the standard [OHLCV](https://acronyms.thefreedictionary.com/OHLCV) `Iterable[Quote]`(such as a list of `Quote`) format.  It should have a consistent period frequency (day, hour, minute, etc).

<!-- ### stock_indicators.indicators.common.quote.**Quote** -->
```python
from stock_indicators.indicators.common.quote import Quote
```

**class Quote(date, open=None, high=None, low=None, close=None, volume=None)**
[[source]](https://github.com/facioquo/stock-indicators-python/blob/main/stock_indicators/indicators/common/quote.py)

| name | type | notes |
| ---- | ---- | ----- |
| date | [`datetime.datetime`](https://docs.python.org/3.8/library/datetime.html#datetime.datetime) | Date |
| open | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Open price |
| high | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | High price |
| low | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Low price |
| close | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Close price |
| volume | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal), Optional | Volume |

Note that:

1. `date` is always required, while each ohlcv values are optional.
2. ohlcv can be provided by `float`, `Decimal` and `str` representing number, but these are always stored as `Decimal`.

### Where can I get historical quote data?

There are many places to get stock market data.  Check with your brokerage or other commercial sites.  If you're looking for a free developer API, see our ongoing [discussion on market data]({{site.dotnet.repo}}/discussions/579) for ideas.

### How much historical quote data do I need?

Each indicator will need different amounts of price `quotes` to calculate.  You can find guidance on the individual indicator documentation pages for minimum requirements; however, **most use cases will require that you provide more than the minimum**.  As a general rule of thumb, you will be safe if you provide 750 points of historical quote data (e.g. 3 years of daily data).

> &#128681; **IMPORTANT! Applying the _minimum_ amount of quote history as possible is NOT a good way to optimize your system.**  Some indicators use a smoothing technique that converges to better precision over time.  While you can calculate these with the minimum amount of quote data, the precision to two decimal points often requires 250 or more preceding historical records.
>
> For example, if you are using daily data and want one year of precise EMA(250) data, you need to provide 3 years of historical quotes (1 extra year for the lookback period and 1 extra year for convergence); thereafter, you would discard or not use the first two years of results.  Occasionally, even more is required for optimal precision.

### Using pandas.DataFrame

If you are using `pandas.DataFrame` to hold quote data, you have to convert it into an iterable `Quote` list. Here's [an efficient way](https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01) to iterate `DataFrame` using _list comprehension_.

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

> For a quickstart that uses **pandas.DataFrame**, see our online _ReplIt_ code example for the [Williams Fractal indicator](https://replit.com/@daveskender/Stock-Indicators-for-Python-Williams-Fractal).
>
> _For more help_, see our GitHub community discussion on
> [Converting pandas.DataFrame to iterable Quotes]({{site.dotnet.repo}}/discussions/1165).

### Using custom quote classes

If you would like to use your own custom `MyCustomQuote` _quote_ class, you **have to** inherit `Quote` class. The `Quote` class is a special class which converts OHLCV properties existing as Python objects to C# objects and which is concrete class of `IQuote` of C# implementation. It enables Python.Net to work with our C# implementation using generics.

```python
from stock_indicators.indicators.common import Quote

class MyCustomQuote(Quote):
    def foo(self): ...
    ... add your own attributes.

```

```python
from stock_indicators import indicators

# fetch historical quotes from your favorite feed
quotes: Iterable[MyCustomQuote] = get_historical_quotes("MSFT");

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
quotes = get_historical_quotes("MSFT")
results = indicators.get_ema(quotes, 20)

# 1. list[ExtendedEMA]
extended_results = [ ExtendedEMA(r._csdata) for r in results ]
for r in extended_results:
    print(r)
```

**Be aware that** if you want to use [helper functions]({{site.baseurl}}/utilities/#utilities-for-indicator-results), use the wrapper class (such as `EMAResults`).

```python
# 2. use wrapper for helper function
from stock_indicators.indicators.ema import EMAResults

extended_results = EMAResults[ExtendedEMA](results._csdata, ExtendedEMA)
pruned_results = extended_results.remove_warmup_periods()
for r in pruned_results:
    print(r)
```

## Generating indicator of indicators

If you want to compute an indicator of indicators, such as an SMA of an ADX or an [RSI of an OBV](https://medium.com/@robswc/this-is-what-happens-when-you-combine-the-obv-and-rsi-indicators-6616d991773d), all you need to do is to take the results of one, reformat into a synthetic historical quotes, and send it through to another indicator.

```python
from stock_indicators import indicators

# fetch historical quotes from your feed (your method)
quotes = get_historical_quotes("MSFT")

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

| type | description |
| ---- | :---------- |
| `Match.BULL_CONFIRMED` | Confirmation of a prior bull Match |
| `Match.BULL_SIGNAL` | Matching bullish pattern |
| `Match.BULL_BASIS` | Bars supporting a bullish Match |
| `Match.NEUTRAL` | Matching for non-directional patterns |
| `Match.NONE` | No match |
| `Match.BEAR_BASIS` | Bars supporting a bearish Match |
| `Match.BEAR_SIGNAL` | Matching bearish pattern |
| `Match.BEAR_CONFIRMED` | Confirmation of a prior bear Match |

### Candle

The `CandleProperties` class is an extended version of `Quote`, and contains additional calculated properties.

| name             | type              | notes                    |
| ---------------- | ----------------- | ------------------------ |
| `date`           | datetime          | Date                     |
| `open`           | Decimal           | Open price               |
| `high`           | Decimal           | High price               |
| `low`            | Decimal           | Low price                |
| `close`          | Decimal           | Close price              |
| `volume`         | Decimal           | Volume                   |
| `size`           | Decimal, Optional | `high-low`               |
| `body`           | Decimal, Optional | `&#124;open-close&#124;` |
| `upper_wick`     | Decimal, Optional | Upper wick size          |
| `lower_wick`     | Decimal, Optional | Lower wick size          |
| `body_pct`       | float, Optional   | `body/size`              |
| `upper_wick_pct` | float, Optional   | `upper_wick/size`        |
| `lower_wick_pct` | float, Optional   | `lower_wick/size`        |
| `is_bullish`     | bool              | `close>open` direction   |
| `is_bearish`     | bool              | `close<open` direction   |

## Utilities

See [Utilities and helper functions]({{site.baseurl}}/utilities/#content) for additional tools.

## Date and time compatibility

Keep date handling simple and predictable:

- Inputs are Python datetime.datetime objects. Provide either tz-aware or naive.
- Tz-aware inputs are normalized to UTC internally; outputs remain tz-aware in UTC.
- Naive inputs stay naive; outputs keep no tzinfo.
- Mixed series are supported. Results align 1:1 with input dates. Sorting is chronological regardless of tz awareness.
- Use valid ISO 8601 when constructing datetimes via parsing. Python's datetime.fromisoformat requires seconds and a colon in offsets, e.g. `2000-03-26T23:00:00+00:00`.
- Examples of accepted creation patterns:
  - Offset-aware: `datetime.fromisoformat('2022-06-02T10:29:00-04:00')`
  - Zulu/UTC: `datetime.fromisoformat('2022-06-02T14:29:00+00:00')`
  - Naive date-time: `datetime.strptime('2022-06-02 14:29:00', '%Y-%m-%d %H:%M:%S')`
  - Date-only (naive midnight): `datetime.strptime('2022-06-02', '%Y-%m-%d')`
- Do not pass raw strings to indicators; always pass datetimes through Quote(date=...).

Behavior summary:

- The instant-in-time is preserved for tz-aware inputs (converted to UTC).
- Naive inputs are treated as unspecified local context and kept as-is.
- Indicator results echo input dates unchanged in both value and tz awareness.
