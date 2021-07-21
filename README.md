# Stock.Indicators for Python

**Stock.Indicators for Python** is a library that produces financial market technical indicators.  Send in historical price quotes and get back desired indicators such as moving averages, Relative Strength Index, Stochastic Oscillator, Parabolic SAR, etc.  Nothing more.

It can be used in any market analysis software using standard OHLCV price quotes for equities, commodities, forex, cryptocurrencies, and others.  We had private trading algorithms, machine learning, and charting systems in mind when originally creating this community library.  A [Stock.Indicators for .NET](https://daveskender.github.io/Stock.Indicators) is also available.

Explore more information:

- [Indicators and overlays](docs/INDICATORS.md)
- [Guide and Pro tips](docs/GUIDE.md)
- [Contributing guidelines](docs/CONTRIBUTING.md)
- [Discussions](https://github.com/DaveSkender/Stock.Indicators.Python/discussions)
- [Release notes](https://github.com/DaveSkender/Stock.Indicators.Python/releases)
- [Contact us](#contact-us)

## Samples

![image](https://raw.githubusercontent.com/DaveSkender/Stock.Indicators/main/docs/examples.png)

### Example usage

```csharp
using Skender.Stock.Indicators;

[..]  // prerequisite: get historical quotes from your own source

// example: get 20-period simple moving average
IEnumerable<SmaResult> results = quotes.GetSma(20);
```

See the [guide](docs/GUIDE.md) and the [full list of indicators and overlays](docs/INDICATORS.md) for more information.

## Frameworks targeted

- Python 3.8
- Python 3.9

## Contributing

This library is an open-source community project.  If you want to report bugs or contribute fixes, new indicators, or new features, please review our [contributing guidelines](docs/CONTRIBUTING.md#content) and [the backlog](https://github.com/DaveSkender/Stock.Indicators.Python/projects/1).

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository uses the standard Apache 2.0 open-source license.  Please review the [license](https://opensource.org/licenses/Apache-2.0) before using or contributing to the software.

## :heart: Patronage

If you or your organization use any of my projects or like what I’m doing, please add a :star: on the [GitHub Repo](https://github.com/DaveSkender/Stock.Indicators.Python) as a token of appreciation.
Thank you for your support!

## :phone: Contact us

[Start a new feature discussion, ask a question](https://github.com/DaveSkender/Stock.Indicators.Python/discussions), or [submit an issue](https://github.com/DaveSkender/Stock.Indicators.Python/issues) if it is publicly relevant.
