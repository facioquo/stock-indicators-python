import os
from datetime import datetime
from decimal import Decimal as PyDecimal
import pytest 
from stock_indicators.indicators.common import Quote

dir = os.path.dirname(__file__)

def load_data_from_csv(sheet):
    data_path = os.path.join(dir, f"../samples/quotes/{sheet}.csv")
    with open(data_path ,"r") as f:
        data = f.readlines()
        data = [d.replace("\n","").split(",") for d in data] # parse csv
    return data[1:] # skips the first row, those are headers

@pytest.fixture(scope='session')
def quotes(days: int = 502):
    rows = load_data_from_csv('Default')

    h = []
    for row in rows:
        h.append(Quote(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def bad_quotes(days: int = 502):
    rows = load_data_from_csv('Bad')

    h = []
    for row in rows:
        h.append(Quote(
            # Quoto.date cannot be null.
            row[1] or datetime.now(),
            # Keep micro values.
            '{:f}'.format(PyDecimal(row[2])) if row[2] is not None else None,
            '{:f}'.format(PyDecimal(row[3])) if row[3] is not None else None,
            '{:f}'.format(PyDecimal(row[4])) if row[4] is not None else None,
            '{:f}'.format(PyDecimal(row[5])) if row[5] is not None else None,
            '{:f}'.format(PyDecimal(row[6])) if row[6] is not None else None,
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def big_quotes(days: int = 1246):
    rows = load_data_from_csv('TooBig')

    h = []
    for row in rows:
        h.append(Quote(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def other_quotes(days: int = 502):
    rows = load_data_from_csv('Compare')

    h = []
    for row in rows:
        h.append(Quote(
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def bitcoin_quotes(days: int = 1246):
    rows = load_data_from_csv('Bitcoin')

    h = []
    for row in rows:
        h.append(Quote(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def mismatch_quotes(days: int = 502):
    rows = load_data_from_csv('Mismatch')

    h = []
    for row in rows:
        h.append(Quote(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def intraday_quotes(days: int = 1564):
    rows = load_data_from_csv('Intraday')

    h = []
    for row in rows:
        h.append(Quote(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def longish_quotes(days: int = 5285):
    rows = load_data_from_csv('Longish')

    h = []
    for row in rows:
        h.append(Quote(
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def longest_quotes():
    rows = load_data_from_csv('Longest')

    h = []
    for row in rows:
        h.append(Quote(
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        ))

    return h

@pytest.fixture(scope='session')
def penny_quotes():
    rows = load_data_from_csv('Penny')

    h = []
    for row in rows:
        h.append(Quote(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
        ))

    return h

@pytest.fixture(scope='session')
def zigzag_quotes(days: int = 342):
    rows = load_data_from_csv('ZigZag')

    h = []
    for row in rows:
        h.append(Quote(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def spx_quotes(days: int = 8111):
    rows = load_data_from_csv('SPX')

    h = []
    for row in rows:
        h.append(Quote(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def msft_quotes(days: int = 8111):
    rows = load_data_from_csv('MSFT')

    h = []
    for row in rows:
        h.append(Quote(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        ))

    h.reverse()
    return h[:days]

@pytest.fixture(scope='session')
def converge_quantities():
    return (5, 20, 30, 50, 75, 100, 120, 150, 200, 250, 350, 500, 600, 700, 800, 900, 1000)
