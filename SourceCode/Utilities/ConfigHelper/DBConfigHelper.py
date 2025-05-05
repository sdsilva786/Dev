import UtilModule.ConfigHelper.ReadDBConfiguration as ConHP


def GetconfigDB_ParametersList():
    ConfigDB_data = ConHP.get_config_data()

    hostname = ConfigDB_data["host"]
    port = ConfigDB_data["port"]
    dbname = ConfigDB_data["dbname"]
    uname = ConfigDB_data["username"]
    pwd = ConfigDB_data["password"]
    db_config = {'hostname': hostname, 'port': port, 'dbname': dbname, 'username': uname, 'password': pwd}
    return db_config
