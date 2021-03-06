from pystratum.mysql.wrapper.MySqlWrapper import MySqlWrapper
from pystratum.wrapper.RowsWithIndexWrapper import RowsWithIndexWrapper as BaseRowsWithIndexWrapper


# ----------------------------------------------------------------------------------------------------------------------
class RowsWithIndexWrapper(BaseRowsWithIndexWrapper, MySqlWrapper):
    # ------------------------------------------------------------------------------------------------------------------
    def _write_execute_rows(self, routine):
        self._write_line('rows = StaticDataLayer.execute_sp_rows(%s)' % self._generate_command(routine))

# ----------------------------------------------------------------------------------------------------------------------
