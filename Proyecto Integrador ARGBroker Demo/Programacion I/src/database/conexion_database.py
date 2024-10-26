import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib

class DatabaseConnection:
    def __init__(self,configuration_file="config.ini"):
        self.configuration_file=configuration_file
        if (self.configuration_file != ""):
            config=configparser.ConfigParser()
            config_path= pathlib.Path(__file__).parent.parent/ self.configuration_file
            config.read(config_path)
            self.db_config=config["database"]

    def connection_database(self):
        try:
            connection = mysql.connector.connect(
                host=self.db_config.get("host"),
                database=self.db_config.get("database"),
                user=self.db_config.get("user"),
                password=self.db_config.get("password")
            )
            return connection
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise "Usuario o Password  no válido"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise "La base de datos no existe"
            else:
                raise err
        return None