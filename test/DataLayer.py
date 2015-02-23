from lib.stratum.mysql.StaticDataLayer import StaticDataLayer


# ----------------------------------------------------------------------------------------------------------------------
class DataLayer(StaticDataLayer):

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_magic_constant01():
        return StaticDataLayer.execute_sp_singleton1("call tst_magic_constant01()")

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_magic_constant02():
        return StaticDataLayer.execute_sp_singleton1("call tst_magic_constant02()")

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_magic_constant03():
        return StaticDataLayer.execute_sp_singleton1("call tst_magic_constant03()")

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_magic_constant04():
        return StaticDataLayer.execute_sp_singleton1("call tst_magic_constant04()")

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test01(p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param26, p_param27):
        return StaticDataLayer.execute_sp_none("call tst_test01(%d, %d, %d, %d, %d, %d, %d, %d, %s, %s, %s, %s, %s, %d, %s, %s, %s, %s, %s, %s)" % (p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param26, p_param27))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test02(p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param18, p_param19, p_param20, p_param21, p_param22, p_param23, p_param24, p_param25, p_param26, p_param27):
        return StaticDataLayer.execute_sp_none("call tst_test02(%d, %d, %d, %d, %d, %d, %d, %d, %s, %s, %s, %s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (p_param00, p_param01, p_param02, p_param03, p_param04, p_param05, p_param06, p_param07, p_param08, p_param09, p_param10, p_param11, p_param12, p_param13, p_param14, p_param15, p_param16, p_param17, p_param18, p_param19, p_param20, p_param21, p_param22, p_param23, p_param24, p_param25, p_param26, p_param27))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_function(p_a, p_b):
        return StaticDataLayer.execute_singleton1("select tst_test_function(%d, %d)" % (p_a, p_b))

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_log():
        return StaticDataLayer.execute_sp_log("call tst_test_log()")

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_none(p_count):
        return StaticDataLayer.execute_sp_none("call tst_test_none(%d)" % p_count)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_row0a(p_count):
        return StaticDataLayer.execute_sp_row0("call tst_test_row0a(%d)" % p_count)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_row1a(p_count):
        return StaticDataLayer.execute_sp_row1("call tst_test_row1a(%d)" % p_count)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_rows1(p_count):
        return StaticDataLayer.execute_sp_rows("call tst_test_rows1(%d)" % p_count)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_rows_with_index1(p_count):
        rows = StaticDataLayer.execute_sp_rows("call tst_test_rows_with_index1(%d)" % p_count)
        if rows:
            return {rows[0]['tst_c01']: {rows[0]['tst_c02']: rows}}
        else:
            return {}

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_rows_with_key1(p_count):
        ret = {}
        rows = StaticDataLayer.execute_sp_rows("call tst_test_rows_with_key1(%d)" % p_count)
        for row in rows:
            if row['tst_c01'] in ret:
                if row['tst_c02'] in ret[row['tst_c01']]:
                    if row['tst_c03'] in ret[row['tst_c01']][row['tst_c02']]:
                        pass
                    else:
                        ret[row['tst_c01']][row['tst_c02']].update({row['tst_c03']: row})
                else:
                    ret[row['tst_c01']].update({row['tst_c02']: {row['tst_c03']: row}})
            else:
                ret.update({row['tst_c01']: {row['tst_c02']: {row['tst_c03']: row}}})

        return ret

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_singleton0a(p_count):
        return StaticDataLayer.execute_sp_singleton0("call tst_test_singleton0a(%d)" % p_count)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def tst_test_singleton1a(p_count):
        return StaticDataLayer.execute_sp_singleton1("call tst_test_singleton1a(%d)" % p_count)


# ----------------------------------------------------------------------------------------------------------------------