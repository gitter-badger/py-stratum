from pystratum.pgsql.StaticDataLayer import StaticDataLayer
from pystratum import Connection


# ----------------------------------------------------------------------------------------------------------------------
class PgSqlConnection(Connection.Connection):
    """
    Class for connecting to PostgreSQL instances and reading PostgreSQL specific connection parameters from 
    configuration files.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self._host = None
        """
        The hostname of the PostgreSQL instance.

        :type: string
        """

        self._port = None
        """
        The port of the PostgreSQL instance.

        :type: string
        """

        self._user = None
        """
        User name.

        :type: string
        """

        self._password = None
        """
        Password required for logging in on to the PostgreSQL instance.

        :type: string
        """

        self._database = None
        """
        The database name.

        :type: string
        """

        self._schema = None
        """
        The schema name.

        :type: string
        """

    # ------------------------------------------------------------------------------------------------------------------
    def connect(self):
        """
        Connects to the PostgreSQL instance.
        """
        StaticDataLayer.connect(self._host,
                                self._database,
                                self._schema,
                                self._user,
                                self._password,
                                self._port)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def disconnect():
        """
        Disconnects from the PostgreSQL instance.
        """
        StaticDataLayer.disconnect()

    # ------------------------------------------------------------------------------------------------------------------
    def _read_configuration_file(self, filename):
        """
        Reads connections parameters from the configuration file.

        :param str filename: The path to the configuration file.
        """
        config, config_supplement = self._read_configuration(filename)

        self._host = self._get_option(config, config_supplement, 'database', 'host', fallback='localhost')
        self._user = self._get_option(config, config_supplement, 'database', 'user')
        self._password = self._get_option(config, config_supplement, 'database', 'password')
        self._database = self._get_option(config, config_supplement, 'database', 'database')
        self._schema = self._get_option(config, config_supplement, 'database', 'schema')
        self._port = int(self._get_option(config, config_supplement, 'database', 'port', fallback='5432'))

# ----------------------------------------------------------------------------------------------------------------------
