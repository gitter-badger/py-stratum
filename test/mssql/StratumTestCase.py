import unittest
from test.mssql.DataLayer import DataLayer


# ----------------------------------------------------------------------------------------------------------------------
class StratumTestCase(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------------
    def setUp(self):
        DataLayer.connect('192.168.137.7', 'test', 'test', 'test')

    # ------------------------------------------------------------------------------------------------------------------
    def tearDown(self):
        DataLayer.disconnect()

# ----------------------------------------------------------------------------------------------------------------------
