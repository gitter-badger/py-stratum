from pystratum.mysql.wrapper.MySqlWrapper import MySqlWrapper


# ----------------------------------------------------------------------------------------------------------------------
class LogWrapper(MySqlWrapper):
    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine):
        self._write_line('return StaticDataLayer.execute_sp_log(%s)' % self._generate_command(routine))


# ----------------------------------------------------------------------------------------------------------------------
