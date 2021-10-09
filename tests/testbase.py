import unittest
from tests.test_data import HistoryTestData

class TestBase(unittest.TestCase):
    """Base class for testing"""
    
    @classmethod
    def setUpClass(cls):
        cls.data_reader = HistoryTestData()
        cls.quotes = cls.data_reader.get()
        cls.other_quotes = cls.data_reader.get_compare()
        cls.bad_quotes = cls.data_reader.get_bad()

        cls.converge_quantities = (5, 20, 30, 50, 75, 100, 120, 150, 200, 250, 350, 500, 600, 700, 800, 900, 1000)

    @classmethod
    def tearDownClass(cls):
        cls.data_reader = None
        cls.quotes = None
        cls.other_quotes = None
        cls.bad_quotes = None
