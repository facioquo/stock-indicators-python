[![image](https://raw.githubusercontent.com/facioquo/stock-indicators-python/main/docs/assets/social-banner.png)](https://python.stockindicators.dev/)

[![PyPI](https://img.shields.io/pypi/v/stock-indicators?color=blue&label=PyPI)](https://badge.fury.io/py/stock-indicators)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/stock-indicators?style=flat&logo=Python&logoColor=white&label=Downloads&color=indigo)](https://pypistats.org/packages/stock-indicators)

# Stock Indicators for Python

**Stock Indicators for Python** is a PyPI library package that produces financial market technical indicators.  Send in historical price quotes and get back desired indicators such as moving averages, Relative Strength Index, Stochastic Oscillator, Parabolic SAR, etc.  Nothing more.

It can be used in any market analysis software using standard OHLCV price quotes for equities, commodities, forex, cryptocurrencies, and others.  We had trading algorithms, machine learning, and charting systems in mind when originally creating this community library.  [Stock Indicators for .NET](https://dotnet.stockindicators.dev/) is also available.

Visit our project site for more information:

- [Overview](https://python.stockindicators.dev/)
- [Indicators and overlays](https://python.stockindicators.dev/indicators/)
- [Guide and Pro tips](https://python.stockindicators.dev/guide/)
- [Release notes](https://github.com/facioquo/stock-indicators-python/releases)
- [Discussions](https://github.com/DaveSkender/Stock.Indicators/discussions)
- [Contributing](https://github.com/facioquo/stock-indicators-python/blob/main/docs/contributing.md#readme)

## Getting started

### Windows

1. Install .NET SDK (8.0 or newer):
    - Download from [Microsoft .NET Downloads](https://dotnet.microsoft.com/download)
    - Or using winget: `winget install Microsoft.DotNet.SDK.8`
    - Verify: `dotnet --info`

2. Install the package:

    ```bash
    pip install stock-indicators
    ```

### macOS

1. Install .NET SDK (8.0 or newer):

    ```bash
    brew install dotnet-sdk
    dotnet --info  # Verify installation
    ```

2. Install the package:

    ```bash
    pip install stock-indicators
    ```

## Example usage

```python
from stock_indicators import indicators

# fetch your data
quotes = get_history("MSFT")

# calculate 20-period SMA
results = indicators.get_sma(quotes, 20)
```

> **Note:** This is a simple example. For a step-by-step guide, see the [QuickStart Guide](https://github.com/facioquo/stock-indicators-python-quickstart#readme) or our [documentation](https://python.stockindicators.dev/) site.
