---
title: Stock Indicators for Python
description: >-
  Transform financial market prices into technical analysis insights with this Python library.
permalink: /
layout: base
lazy-images: true
---

<p style="text-align:center;">
<a href="https://pypi.org/project/stock-indicators" aria-label="Get the PyPI package." class="not-mobile">
  <img src="https://img.shields.io/pypi/v/stock-indicators?color=blue&label=PyPI&cacheSeconds=259200" alt="" />
</a>
<a href="https://dev.azure.com/skender/Stock.Indicators/_build/latest?definitionId=26&branchName=main&view=codecoverage-tab" aria-label="Read more about our code coverage." class="not-mobile">
  <img src="https://img.shields.io/azure-devops/coverage/skender/stock.indicators/26/main?logo=AzureDevOps&label=Test%20Coverage&cacheSeconds=259200" alt="" />
</a>
<a href="https://pypistats.org/packages/stock-indicators" aria-label="See PyPi download stats." class="not-mobile">
  <img src="https://img.shields.io/pypi/dm/stock-indicators?style=flat&logo=Python&logoColor=white&label=Downloads&color=indigo&link=https%3A%2F%2Fpypistats.org%2Fpackages%2Fstock-indicators" alt="" />
</a>
</p>

<h1 style="display:none;">{{ page.title }}</h1>

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

## Python versions supported

- Python 3.8+

## Licensed for everyone

<a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square&cacheSeconds=259200" alt="Apache 2.0 license badge" width="124" height="20" class="lazyload" /></a>

This repository uses the standard Apache 2.0 open-source license.  Please review the [license](https://opensource.org/licenses/Apache-2.0) before using or contributing to the software.

## Share your ideas with the community

**Need help?**  Have ideas?  [Start a new discussion, ask a question &#128172;]({{site.dotnet.repo}}/discussions), or [submit an issue]({{site.github.repository_url}}/issues) if it is publicly relevant.  You can also direct message [@daveskender](https://twitter.com/messages/compose?recipient_id=27475431).

## Give back with patronage

Thank you for your support!  This software is crafted with care by unpaid enthusiasts who &#128150; all forms of encouragement.  If you or your organization use this library or like what we're doing, add a &#11088; on the [GitHub Repo]({{site.github.repository_url}}) as a token of appreciation.

If you want to buy us a beer or are interested in ongoing support as a patron, [become a sponsor](https://github.com/sponsors/LeeDongGeon1996).  Patronage motivates continued maintenance and evolution of open-source projects, and to inspire new ones.

## Contribute to help others

This PyPI package is an open-source project.  If you want to report bugs or contribute fixes, new indicators, or new features, please review our [contributing guidelines]({{site.baseurl}}/contributing/#content) and [the backlog](https://github.com/users/DaveSkender/projects/2).

Special thanks to all of our community code contributors!

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block">
     <a href="{{ contributor.html_url }}" width="75" height="75"><img data-src="{{ contributor.avatar_url }}&s=75" width="75" height="75" class="circle lazyload" alt="{{ contributor.login }} avatar" /></a>
  </li>
{% endfor %}
</ul>

&#187; see our [full list of indicators and overlays]({{site.baseurl}}/indicators/#content)
