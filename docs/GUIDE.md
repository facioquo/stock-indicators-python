---
title: Guide and Pro tips
permalink: /guide/
layout: default
redirect_from:
 - /docs/GUIDE.html
---

# {{ page.title }}

- [Installation and setup](#installation-and-setup)
- [Prerequisite data](#prerequisite-data)
- [Example usage](#example-usage)
- [Historical quotes](#historical-quotes)
- [Using custom quote classes](#using-custom-quote-classes)
- [Using derived results classes](#using-derived-results-classes)
- [Generating indicator of indicators](#generating-indicator-of-indicators)
- [Utilities and Helper functions]({{site.baseurl}}/utilities/#content)
- [Contributing guidelines]({{site.baseurl}}/contributing/#content)

## Getting started

### Installation and setup

Find and install the [stock-indicators](#LINK-TO-PYPI) Python package into your environment. See [more help](https://packaging.python.org/tutorials/installing-packages/) for installing packages.

```powershell
# pip example
pip install stock-indicators

# conda example (No plan yet.)
# conda install stock-indicators
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

- [Example usage code]({{site.baseurl}}/examples/#content) in a simple working console application
- [Demo site](https://stock-charts.azurewebsites.net) (a stock chart)

## Historical quotes

You must provide historical price quotes to the library in the standard [OHLCV](https://acronyms.thefreedictionary.com/OHLCV) `Iterable[Quote]`(such as a list of `Quote`) format.  It should have a consistent period frequency (day, hour, minute, etc).

| name | type | notes
| -- |-- |--
| date | [`datetime.datetime`](https://docs.python.org/3.8/library/datetime.html#datetime.datetime) | Date
| open | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal) | Open price
| high | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal) | High price
| low | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal) | Low price
| close | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal) | Close price
| volume | [`decimal.Decimal`](https://docs.python.org/3.8/library/decimal.html?highlight=decimal#decimal.Decimal) | Volume

### Where can I get historical quote data?

There are many places to get stock market data.  Check with your brokerage or other commercial sites.  If you're looking for a free developer API, see our ongoing [discussion on market data](https://github.com/DaveSkender/Stock.Indicators/discussions/579) for ideas.

### How much historical quote data do I need?

Each indicator will need different amounts of price `quotes` to calculate.  You can find guidance on the individual indicator documentation pages for minimum requirements; however, **most use cases will require that you provide more than the minimum**.  As a general rule of thumb, you will be safe if you provide 750 points of historical quote data (e.g. 3 years of daily data).  A `BadQuotesException` will be thrown if you do not provide sufficient historical quotes to produce any results.

:warning: IMPORTANT! Some indicators use a smoothing technique that converges to better precision over time.  While you can calculate these with the minimum amount of quote data, the precision to two decimal points often requires 250 or more preceding historical records.

For example, if you are using daily data and want one year of precise EMA(250) data, you need to provide 3 years of historical quotes (1 extra year for the lookback period and 1 extra year for convergence); thereafter, you would discard or not use the first two years of results.  Occassionally, even more is required for optimal precision.


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

If you have a model that has different properties names, but the same meaning, you only need to map them. There are already mapper methods for each OHLCV properties. These mappers are in `stock_indicators.indicators.common.quote`

| **OHLCV** | **Mapper Methods** |
| -- |getter |setter
| date | `_get_date` | `_set_date`
| open | `_get_open` | `_set_open`
| high | `_get_high` | `_set_high`
| low | `_get_low` | `_set_low`
| close | `_get_close` | `_set_close`
| volume | `_get_volume` | `_set_volume`


Suppose your class has a property called `close_date` instead of `date`, it could be represented like this:

```python
from stock_indicators.indicators.common.quote import Quote, _get_date, _set_date

class MyCustomQuote(Quote):
    close_date = property(_get_date, _set_date)

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

Here's an example of SMA of RSI:

```python
from stock_indicators import indicators

# fetch historical quotes from your feed (your method)
quotes = get_history_from_feed("MSFT")

# calculate SMA of RSI
results = indicators.get_rsi(quotes)
quotes_from_rsi = results.to_quotes()
sma_of_rsi = indicators.get_sma(quotes_from_rsi, 20)

```

See [.to_quotes()]({{site.baseurl}}/utilities/#convert-to-quotes) for more information.

When `.to_quotes()` is not available for an indicator, a workaround is to convert yourself.

```python
# calculate EMA
results = indicators.get_ema(quotes, 20)

# convert to synthetic quotes
quotes_from_ema = [ Quote(date=r.date, close=r.ema) for r in results ]

# calculate SMA of EMA
sma_of_ema = indicators.get_sma(quotes_from_ema, 20)

```

## Utilities

See [Utilities and Helper functions]({{site.baseurl}}/utilities/#content) for additional tools.
