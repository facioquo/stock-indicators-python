import json
import os
from datetime import datetime

from stock_indicators.indicators.common.quote import Quote


def load_quotes_from_json(json_path):
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, json_path)
    quotes = []
    with open(data_path, encoding="utf-8") as st_json:
        for j in json.load(st_json):
            quotes.append(
                Quote(
                    datetime.fromisoformat(j["Date"]),
                    j["Open"],
                    j["High"],
                    j["Low"],
                    j["Close"],
                    j["Volume"],
                )
            )

    return quotes
