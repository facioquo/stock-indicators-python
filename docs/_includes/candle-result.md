### CandleResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `price` | decimal, Optional | Price of the most relevant OHLC candle element when a Match is present
| `match` | [Match]({{site.baseurl}}/guide/#Match) | Generated Match type
| `candle` | [CandleProperties]({{site.baseurl}}/guide/#candle) | Candle properties
