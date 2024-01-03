import os
import csv
from datetime import datetime
from decimal import Decimal, DecimalException
import pytest
from stock_indicators.indicators.common import Quote


dir = os.path.dirname(__file__)


def get_data_from_csv(filename):
    """Read from CSV file."""

    data_path = os.path.join(dir, f"../samples/quotes/{filename}.csv")
    with open(data_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data[1:]  # skips the first row, those are headers


def parse_decimal(value):
    """Parse decimal value."""

    try:
        return '{:f}'.format(Decimal(value))
    except DecimalException:
        return None


def parse_date(date_str):
    """Parse date value. Input format must be '%Y-%m-%d' """

    try:
        if len(date_str) <= 10:
            return datetime.strptime(date_str, '%Y-%m-%d')
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return datetime.now()


@pytest.fixture(scope='session')
def quotes(days: int = 502):
    rows = get_data_from_csv('Default')

    h = []
    for row in rows:
        h.append(Quote(
            parse_date(row[1]),
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
    rows = get_data_from_csv('Compare')

    h = []
    for row in rows:
        h.append(Quote(
            parse_date(row[2]),
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        ))

    h.reverse()
    return h[:days]


@pytest.fixture(scope='session')
def longish_quotes(days: int = 5285):
    rows = get_data_from_csv('Longish')

    h = []
    for row in rows:
        h.append(Quote(
            parse_date(row[2]),
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
        ))

    h.reverse()
    return h[:days]
