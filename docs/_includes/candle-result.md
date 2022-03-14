### CandleResult

| name | type | notes
| -- |-- |--
| `date` | datetime | Date
| `price` | decimal, Optional | Price of the most relevant OHLC candle element when a signal is present
| `signal` | [Signal]({{site.baseurl}}/guide/#signal) | Generated signal type
| `candle` | [CandleProperties]({{site.baseurl}}/guide/#candle) | Candle properties
