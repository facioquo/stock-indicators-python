---
title: Stock Indicators for Python
description: >-
  Transform financial market prices into technical analysis insights with this Python library.
permalink: /
layout: base
lazy-images: true
---

<h1 style="display:none;">{{ page.title }}</h1>

[![PyPI](https://img.shields.io/pypi/v/stock-indicators?color=blue&label=PyPI)](https://badge.fury.io/py/stock-indicators)
[![code coverage](https://img.shields.io/azure-devops/coverage/skender/stock.indicators/26/main?logo=AzureDevOps&label=Test%20Coverage)](https://dev.azure.com/skender/Stock.Indicators/_build/latest?definitionId=26&branchName=main&view=codecoverage-tab)

**Stock Indicators for Python** is a library that produces financial market technical indicators.  Send in historical price quotes and get back desired indicators such as moving averages, Relative Strength Index, Stochastic Oscillator, Parabolic SAR, etc.  Nothing more.

It can be used in any market analysis software using standard OHLCV price quotes for equities, commodities, forex, cryptocurrencies, and others.  We had private trading algorithms, machine learning, and charting systems in mind when originally creating this community library.  [Stock Indicators for .NET](https://dotnet.stockindicators.dev) is also available.

Explore more information:

- [Guide and Pro tips]({{site.baseurl}}/guide/#content)
- [Indicators and overlays]({{site.baseurl}}/indicators/#content)
- [Utilities and Helpers]({{site.baseurl}}/utilities/#content)
- [Demo site](https://stock-charts.azurewebsites.net) (a stock chart)
- [Release notes]({{site.github.repository_url}}/releases)
- [Discussions]({{site.dotnet.repo}}/discussions)
- [Contributing guidelines]({{site.baseurl}}/contributing/#content)

## Samples

![image](https://raw.githubusercontent.com/DaveSkender/Stock.Indicators/main/docs/examples.webp)

### Example usage

```python
from stock_indicators import indicators

# prerequisite: get historical quotes from your own source
quotes = get_historical_quotes()

# example: get 20-period simple moving average
results = indicators.get_sma(quotes, 20)
```

See the [guide]({{site.baseurl}}/guide/#content) and the [full list of indicators and overlays]({{site.baseurl}}/indicators/#content) for more information.

## Version supported

- Python 3.8+

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)

This repository uses the standard Apache 2.0 open-source license.  Please review the [license](https://opensource.org/licenses/Apache-2.0) before using or contributing to the software.

## :phone: Contact us

[Start a new discussion, ask a question]({{site.dotnet.repo}}/discussions), or [submit an issue]({{site.github.repository_url}}/issues) if it is publicly relevant.  You can also direct message [@daveskender](https://twitter.com/messages/compose?recipient_id=27475431).

## :heart: Patronage

If you or your organization use any of my projects or like what I’m doing, please add a :star: on the [GitHub Repo]({{site.github.repository_url}}) as a token of appreciation.
If you want to buy me a beer or are interest in ongoing support as a patron, [become a sponsor](https://github.com/sponsors/DaveSkender).
Patronage motivates continued maintenance and evolution of open-source projects, and to inspire new ones.
Thank you for your support!

## :octocat: Contributing

This NuGet package is an open-source project.  If you want to report bugs or contribute fixes, new indicators, or new features, please review our [contributing guidelines]({{site.baseurl}}/contributing/#content) and [the backlog]({{site.github.repository_url}}/projects/1).

Special thanks to all of our community code contributors!

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="75" height="75" class="circle" alt="{{ contributor.login }}" /></a>
  </li>
{% endfor %}
</ul>
