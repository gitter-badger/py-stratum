import sys
from test.mysql.StratumTestCase import StratumTestCase
from test.mysql.DataLayer import DataLayer


# ----------------------------------------------------------------------------------------------------------------------
class LogTest(StratumTestCase):

    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Stored routine with designation type none must return the number of rows affected.
        """
        n = DataLayer.tst_test_log()

        self.assertEqual(2, n)

        self.assertRegex(sys.stdout.getvalue(),
                         '^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\sHello, world\n){2}$')


# ----------------------------------------------------------------------------------------------------------------------
