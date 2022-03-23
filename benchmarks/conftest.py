import os
from datetime import datetime
from decimal import Decimal as PyDecimal
import pytest
from openpyxl import load_workbook
from stock_indicators.indicators.common import Quote

dir = os.path.dirname(__file__)
data_path = os.path.join(dir, "../samples/quotes/History.xlsx")
wb = load_workbook(data_path, data_only=True)

@pytest.fixture(scope='session')
def quotes(days: int = 502):
    rows = list(wb['Default'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def other_quotes(days: int = 502):
    rows = list(wb['Compare'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
            row[7].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def bad_quotes(days: int = 502):
    rows = list(wb['Bad'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            # Quoto.date cannot be null.
            row[1].value or datetime.now(),
            # Keep micro values.
            '{:f}'.format(PyDecimal(row[2].value)) if row[2].value is not None else None,
            '{:f}'.format(PyDecimal(row[3].value)) if row[3].value is not None else None,
            '{:f}'.format(PyDecimal(row[4].value)) if row[4].value is not None else None,
            '{:f}'.format(PyDecimal(row[5].value)) if row[5].value is not None else None,
            '{:f}'.format(PyDecimal(row[6].value)) if row[6].value is not None else None,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def bitcoin_quotes(days: int = 1246):
    rows = list(wb['Bitcoin'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def intraday_quotes(days: int = 1564):
    rows = list(wb['Intraday'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def longish_quotes(days: int = 5285):
    rows = list(wb['Longish'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
            row[7].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def longest_quotes():
    rows = list(wb['Longest'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
            row[7].value,
        ))

    return h

@pytest.fixture(scope='session')
def penny_quotes():
    rows = list(wb['Penny'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
        ))

    return h

@pytest.fixture(scope='session')
def zigzag_quotes(days: int = 342):
    rows = list(wb['ZigZag'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[0].value,
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def spx_quotes(days: int = 8111):
    rows = list(wb['SPX'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[0].value,
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def msft_quotes(days: int = 8111):
    rows = list(wb['MSFT'])[1:]

    h = []
    for row in rows:
        h.append(Quote(
            row[0].value,
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
        ))

    h.reverse()
    return h[:days]
