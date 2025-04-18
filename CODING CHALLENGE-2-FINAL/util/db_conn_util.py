import pyodbc
from util.db_property_util import get_connection_string

def get_connection(filename="db.properties"):
    conn_str = get_connection_string()
    return pyodbc.connect(conn_str)
