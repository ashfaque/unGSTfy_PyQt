
import os
import sys

from PyQt6 import QtCore, QtSql

from config.ui_element_names import APP_NAME
from config.constants import INI_SETTINGS_FILE_NAME, DB_FILE_NAME
from config.app_logging import trigger_manual_exception_and_log_it, get_app_data_dir


DEBUG_MODE = True    # ! IMPORTANT: Set to `False` before building the executable and revert it back to `True` before commit. This is used to disable some features like changing the Windows OS registry, etc. which is not required in development environment.


class AppSettingsManager:
    def __init__(self):
        self.app_name = APP_NAME
        # self.settings_dir = os.path.join(os.getenv("APPDATA"), app_name)

        self.settings_dir = get_app_data_dir()    # ? Get the writable location for application data, platform independent.

        # ? Create the directory if it doesn't exist.
        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir)

        # ? Define the settings file path.
        self.settings_file_path = f"{self.settings_dir}/{INI_SETTINGS_FILE_NAME}.ini"

        # Initialize QSettings with the custom location
        self.settings = QtCore.QSettings(self.settings_file_path, QtCore.QSettings.Format.IniFormat)


    def save_data_in_settings(self, key:str , value):    # ? 'key' is a string, 'value' is of any Python3 data type.
        self.settings.setValue(key, value)
        # with open(os.path.join(self.settings_dir, "settings.json"), "w") as json_file:    # open in 'a' mode to append.
        #     json.dump(data, json_file)


    def load_data_from_settings(self, key: str):
        return self.settings.value(key, defaultValue=None)
        # settings_file = os.path.join(self.settings_dir, "settings.json")
        # if os.path.exists(settings_file):
        #     with open(settings_file, "r") as json_file:
        #         return json.load(json_file)
        # return {}


    def remove_data_from_settings(self, key: str):
        self.settings.remove(key)


### * Usage:-
# from config.settings import AppSettingsManager
# settings_manager = AppSettingsManager()
# settings_manager.save_data_in_settings('key1', 'value1')
# loaded_settings = settings_manager.load_data_from_settings()
# print('loaded_settings---> ', loaded_settings)



# ? https://realpython.com/python-pyqt-database/

class LocalDatabaseManager:
    _db = None    # Class-level attribute to store the database connection

    @classmethod
    def open_db_connection(cls):
        # app_name = APP_NAME
        # local_db_dir = os.path.join(os.getenv("APPDATA"), app_name)

        local_db_dir = get_app_data_dir()    # ? Get the writable location for application data, platform independent.

        # ? Create the directory if it doesn't exist.
        if not os.path.exists(local_db_dir):
            os.makedirs(local_db_dir)

        # ? Define the settings file path.
        db_file_path = f"{local_db_dir}/{DB_FILE_NAME}.db"


        if cls._db is None:
            # Initialize QtSql.QSqlDatabase with the custom location
            cls._db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            cls._db.setDatabaseName(db_file_path)

            if not cls._db.open():
                # print("Error: Could not connect to the database: ", cls._db.lastError().text())
                trigger_manual_exception_and_log_it("Error: Could not connect to the database: " + cls._db.lastError().text())
                sys.exit(1)    # ? Closing the application.
        return cls._db


    @classmethod
    def close_connection(cls):
        if cls._db is not None:
            cls._db.close()





class LocalDatabaseModel:
    def __init__(self, table_name: str = None, columns: dict = None):

        self.db = self.open_db_connection()    # ? Initialize the database connection object.

        self.TABLE_NAME = table_name
        self.COLUMNS = columns

        # Create the table if it doesn't exist
        self.create_table_if_not_exists(self.TABLE_NAME, self.COLUMNS)
        # self.update_table_if_changes_detected(self.TABLE_NAME, self.COLUMNS)    # * BE CAREFUL: This will drop the table and create new table with changed columns. So, use it only when you want to change the columns of the table.


    def __enter__(self):
        # self.db = LocalDatabaseManager.open_db_connection()
        self.db = self.open_db_connection()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        pass    # ? Keep the connection open for other classes to use the same connection. It will be closed in the main.py when application is closed.
        # self.db.close()
        # self.close_db_connection()


    def __del__(self):
        pass    # ? Keep the connection open for other classes to use the same connection. It will be closed in the main.py when application is closed.
        # self.close_db_connection()


    def __str__(self):
        return f"Database connection object: {self.db}"


    def __repr__(self):
        return f"Database connection object: {self.db}"


    def open_db_connection(self):
        return LocalDatabaseManager.open_db_connection()


    # def close_db_connection(self):
    #     if self.db is not None:
    #         self.db.close()
    #         self.db = None


    # * ------------------------------ Database operations ------------------------------ * #


    def create_table_if_not_exists(self, table_name: str, columns: dict):    # ? eg., columns = {'date': ['TEXT', 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP'], 'json_data': ['TEXT', 'NOT NULL', 'DEFAULT {}']}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
        ''' + ', '.join([f"{column_name} {' '.join(column_attributes)}" for column_name, column_attributes in columns.items()]) + ')'

        if not query.exec(query_to_execute):
            # print("Error: Failed to create table", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to create table" + query.lastError().text(), close_app=True)
        else:   # If table created successfully.
            self.db.commit()

        query.finish()
        query.clear()
        # self.db.close()

    def update_table_if_changes_detected(self, table_name: str, columns: dict):    # ? eg., columns = {'date': ['TEXT', 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP'], 'json_data': ['TEXT', 'NOT NULL', 'DEFAULT {}']}
        # # print("Error: Failed to create table", query.lastError().text())
        # trigger_manual_exception_and_log_it("Error: Failed to create table" + query.lastError().text(), close_app=True)
        # ...
        query = QtSql.QSqlQuery()
        query_to_execute = f'PRAGMA table_info({table_name});'
        if not query.exec(query_to_execute):
            # print("Error: Failed to fetch table info", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to fetch table info" + query.lastError().text(), close_app=True)
            return None

        existing_columns = {}
        while query.next():
            column_name = query.value("name")
            column_type = query.value("type")
            existing_columns[column_name] = column_type
            # TODO: Future Scope: Add support for column attributes like 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP', etc.

        query.finish()
        query.clear()

        if not existing_columns:
            return

        existing_columns.pop('id', None)    # ? Remove 'id' column from existing_columns dict.
        # Check for differences between existing and desired columns
        differences = set(columns.keys()) - set(existing_columns.keys())
        if not differences:    # Checking Vice Versa.
            differences = set(existing_columns.keys()) - set(columns.keys())
        if differences:
            # Perform DROP TABLE query if differences exist.
            query_to_execute = f"DROP TABLE {table_name};"
            if not query.exec(query_to_execute):
                # print("Error: Failed to drop table", query.lastError().text())
                trigger_manual_exception_and_log_it("Error: Failed to drop table" + query.lastError().text(), close_app=True)
            else:
                self.db.commit()
            query.finish()
            query.clear()

            # Perform CREATE TABLE query if differences exist.
            self.create_table_if_not_exists(table_name, columns)

            # # Perform ALTER TABLE query if differences exist
            # for column_name in differences:
            #     column_attributes = ' '.join(columns[column_name])
            #     query_to_execute = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_attributes};"

            #     query = QtSql.QSqlQuery()
            #     if not query.exec(query_to_execute):
            #         print("Error: Failed to alter table", query.lastError().text())
            #     else:
            #         self.db.commit()

            #     query.finish()
            #     query.clear()


    def insert_data(self, table_name: str, data: dict):    # ? eg., data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                INSERT INTO {table_name} (
                    {', '.join(data.keys())}
                ) VALUES (
                    {', '.join([f":{key}" for key in data.keys()])}
                )
        '''
        query.prepare(query_to_execute)

        for key, value in data.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            # print("Error: Failed to insert data: ", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to insert data: ", query.lastError().text(), close_app=True)
        query.finish()
        query.clear()


    def update_data(self, table_name: str, data: dict, where: dict):    # ? eg., data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}, where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                UPDATE {table_name} SET
                    {', '.join([f"{key} = :{key}" for key in data.keys()])}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''
        query.prepare(query_to_execute)
        for key, value in data.items():
            query.bindValue(f":{key}", str(value))
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            # print("Error: Failed to update data: ", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to update data: ", query.lastError().text(), close_app=True)
        query.finish()
        query.clear()


    def delete_data(self, table_name: str, where: dict):    # ? eg., where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                DELETE FROM {table_name}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''
        query.prepare(query_to_execute)
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            # print("Error: Failed to delete data: ", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to delete data: ", query.lastError().text(), close_app=True)
        query.finish()
        query.clear()


    def select_data(self, table_name: str, columns: list, where: dict, raw: str=None):    # ? eg., columns = ['id', 'date', 'json_data'], where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                SELECT
                    {', '.join(columns)}
                FROM
                    {table_name}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''
        if raw:
            query_to_execute += f" {raw}"    # ? eg., raw = "ORDER BY id DESC LIMIT 1" or "AND id = 1" or "date(date_column) > date('now', '-1 day')", etc.

        query.prepare(query_to_execute)
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        # print('query.exec()---> ', query.lastQuery())

        result = []
        if query.exec():
            while query.next():
                row = {}
                for column in columns:
                    row[column] = query.value(column)
                result.append(row)    # [{column1: value1, column2: value2}, {column1: value1, column2: value2}, ...]
                # result.append([query.value(i) for i in range(len(columns))])    # [query.value(0), query.value(1), query.value(2)]
            self.db.commit()
        else:
            # print("Error: Failed to fetch data: ", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to fetch data: ", query.lastError().text(), close_app=True)
        query.finish()
        query.clear()
        return result


    def select_all_data(self, table_name: str, columns: list):
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                SELECT
                    {', '.join(columns)}
                FROM
                    {table_name}
        '''
        query.prepare(query_to_execute)

        result = []
        if query.exec():
            while query.next():
                row = {}
                for column in columns:
                    row[column] = query.value(column)
                result.append(row)    # [{column1: value1, column2: value2}, {column1: value1, column2: value2}, ...]
            self.db.commit()
        else:
            # print("Error: Failed to fetch data: ", query.lastError().text())
            trigger_manual_exception_and_log_it("Error: Failed to fetch data: ", query.lastError().text(), close_app=True)
        query.finish()
        query.clear()
        return result


    # * ------------------------------ Utility methods ------------------------------ * #


    def create(self, data: dict):    # ? data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}
        # Use the insert_data method from the parent class
        return self.insert_data(self.TABLE_NAME, data)


    def update(self, data: dict, where: dict):    # ? data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}, where = {'id': 1}
        # Use the update_data method from the parent class
        return self.update_data(self.TABLE_NAME, data, where)


    def delete(self, where: dict):    # ? where = {'id': 1}
        # Use the delete_data method from the parent class
        return self.delete_data(self.TABLE_NAME, where)


    # * operator should be present after the column name in `where` dict.
    def get(self, where: dict, columns: list = None):    # ? where = {'id =': 1}, columns = ['id', 'date', 'json_data']
        if not columns:
            columns = list(self.COLUMNS.keys())
        # Use the select_data method from the parent class
        return self.select_data(self.TABLE_NAME, columns, where)


    def get_all(self, columns: list = None):    # ? columns = ['id', 'date', 'json_data']
        if not columns:
            columns = list(self.COLUMNS.keys())
        # Use the select_all_data method from the parent class
        return self.select_all_data(self.TABLE_NAME, columns)



### * Usage:-
# class CurrencyConverterCurrenciesListModel inherits class LocalDatabaseModel.
# currency_converter_currency_list_obj = CurrencyConverterCurrenciesListModel()
# currencies_list_of_dicts = currency_converter_currency_list_obj.get_all()
# or,
# with CurrencyConverterCurrenciesListModel() as currency_converter_currency_list_obj:
#     currencies_list_of_dicts = currency_converter_currency_list_obj.get_all()



# * SQLITE_OPERATORS : list = ['=', '>', '<', '>=', '<=', '!=', '<>', 'LIKE', 'NOT LIKE', 'IN', 'NOT IN', 'BETWEEN', 'NOT BETWEEN', 'IS', 'IS NOT', 'IS NULL', 'IS NOT NULL', 'REGEXP', 'NOT REGEXP', 'MATCH', 'NOT MATCH', 'GLOB', 'NOT GLOB', 'MATCH', 'NOT MATCH', 'REGEXP', 'NOT REGEXP', 'GLOB', 'NOT GLOB', 'IS', 'IS NOT', 'IS NULL']





"""    # ? IN this class we are facing the issue :
# ? ► QSqlDatabasePrivate::removeDatabase: connection 'qt_sql_default_connection' is still in use, all queries will cease to work.
# ? ► QSqlDatabasePrivate::addDatabase: duplicate connection name 'qt_sql_default_connection', old connection removed.
class LocalDatabaseModel:
    def __init__(self):
        self.app_name = APP_NAME
        # self.local_db_dir = os.path.join(os.getenv("APPDATA"), app_name)

        # ? Get the writable location for application data, platform independent.
        if is_frozen_executable():
            self.local_db_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
        else:    # If development environment.
            self.local_db_dir = os.getcwd() + "/_temp"    # Pending: Global variable defined in config/constants.py

        # ? Create the directory if it doesn't exist.
        if not os.path.exists(self.local_db_dir):
            os.makedirs(self.local_db_dir)

        # ? Define the settings file path.
        self.db_file_path = f"{self.local_db_dir}/unGSTfy_db.db"    # Pending: Global variable defined in config/constants.py or .sqlite3

        self.db = None    # ? Initialize the database connection object as None.

        # self.connect_to_database()
        self.open_db_connection()


    def __enter__(self):
        self.open_db_connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_db_connection()

    # def __del__(self):
    #     self.close_db_connection()

    # def __call__(self):
    #     self.open_db_connection()
    #     return self

    def __str__(self):
        return f"Database connection object: {self.db}"

    def __repr__(self):
        return f"Database connection object: {self.db}"


    # def connect_to_database(self):
    def open_db_connection(self):
        # Initialize QtSql.QSqlDatabase with the custom location
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_file_path)

        if not self.db.open():
            print("Error: Could not connect to the database: ", self.db.lastError().text())    # Pending: To show this to user.
            # self.label.setText("Failed to connect database")
            sys.exit(1)


    def close_db_connection(self):
        if self.db is not None:
            self.db.close()
            self.db = None


    def create_table_if_not_exists(self, table_name: str, columns: dict):    # ? eg., columns = {'date': ['TEXT', 'NOT NULL', 'DEFAULT CURRENT_TIMESTAMP'], 'json_data': ['TEXT', 'NOT NULL', 'DEFAULT {}']}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
        ''' + ', '.join([f"{column_name} {' '.join(column_attributes)}" for column_name, column_attributes in columns.items()]) + ')'

        if not query.exec(query_to_execute):
            print("Error: Failed to create table", query.lastError().text())    # Pending: To show this to user.
        else:   # If table created successfully.
            self.db.commit()

        query.finish()
        query.clear()
        # self.db.close()


    # Pending: Implement alter table method, if anything in column names or attributes changes.

    def insert_data(self, table_name: str, data: dict):    # ? eg., data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                INSERT INTO {table_name} (
                    {', '.join(data.keys())}
                ) VALUES (
                    {', '.join([f":{key}" for key in data.keys()])}
                )
        '''
        query.prepare(query_to_execute)

        for key, value in data.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            print("Error: Failed to insert data: ", query.lastError().text())    # Pending: To show this to user.
        query.finish()
        query.clear()


    def update_data(self, table_name: str, data: dict, where: dict):    # ? eg., data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}, where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                UPDATE {table_name} SET
                    {', '.join([f"{key} = :{key}" for key in data.keys()])}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''
        query.prepare(query_to_execute)
        for key, value in data.items():
            query.bindValue(f":{key}", str(value))
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            print("Error: Failed to update data: ", query.lastError().text())    # Pending: To show this to user.
        query.finish()
        query.clear()


    def delete_data(self, table_name: str, where: dict):    # ? eg., where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                DELETE FROM {table_name}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''
        query.prepare(query_to_execute)
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        if query.exec():
            self.db.commit()
        else:
            print("Error: Failed to delete data: ", query.lastError().text())    # Pending: To show this to user.
        query.finish()
        query.clear()


    def select_data(self, table_name: str, columns: list, where: dict):    # ? eg., columns = ['id', 'date', 'json_data'], where = {'id': 1}
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                SELECT
                    {', '.join(columns)}
                FROM
                    {table_name}
                WHERE
                    {', '.join([f"{key} = :{key}" for key in where.keys()])}
        '''    # Pending: Conditional operators needs to be implemented. along with date(data_date) etc.

        query.prepare(query_to_execute)
        for key, value in where.items():
            query.bindValue(f":{key}", str(value))

        # print('query.exec()---> ', query.lastQuery())

        result = []
        if query.exec():
            while query.next():
                row = {}
                for column in columns:
                    row[column] = query.value(column)
                result.append(row)    # [{column1: value1, column2: value2}, {column1: value1, column2: value2}, ...]
                # result.append([query.value(i) for i in range(len(columns))])    # [query.value(0), query.value(1), query.value(2)]
            self.db.commit()
        else:
            print("Error: Failed to fetch data: ", query.lastError().text())    # Pending: To show this to user.
        query.finish()
        query.clear()
        return result


    def select_all_data(self, table_name: str, columns: list):
        query = QtSql.QSqlQuery()
        query_to_execute = f'''
                SELECT
                    {', '.join(columns)}
                FROM
                    {table_name}
        '''
        query.prepare(query_to_execute)

        result = []
        if query.exec():
            while query.next():
                row = {}
                for column in columns:
                    row[column] = query.value(column)
                result.append(row)    # [{column1: value1, column2: value2}, {column1: value1, column2: value2}, ...]
            self.db.commit()
        else:
            print("Error: Failed to fetch data: ", query.lastError().text())    # Pending: To show this to user.
        query.finish()
        query.clear()
        return result


# ? This used to work with older commented above LocalDatabaseModel class.
class LocalDatabaseManager(LocalDatabaseModel):
    def __init__(self, table_name: str = None, columns: dict = None):
        # Initialize the parent class (LocalDatabaseModel)
        super().__init__()

        self.TABLE_NAME = table_name
        self.COLUMNS = columns

        # Create the table if it doesn't exist
        self.create_table_if_not_exists(self.TABLE_NAME, self.COLUMNS)

    def create(self, data: dict):    # ? data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}
        # Use the insert_data method from the parent class
        return self.insert_data(self.TABLE_NAME, data)

    def update(self, data: dict, where: dict):    # ? data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}, where = {'id': 1}
        # Use the update_data method from the parent class
        return self.update_data(self.TABLE_NAME, data, where)

    def delete(self, where: dict):    # ? where = {'id': 1}
        # Use the delete_data method from the parent class
        return self.delete_data(self.TABLE_NAME, where)

    # * operator should be present after the column name in `where` dict.
    def get(self, where: dict, columns: list = None):    # ? where = {'id =': 1}, columns = ['id', 'date', 'json_data']
        if not columns:
            columns = list(self.COLUMNS.keys())
        # Use the select_data method from the parent class
        return self.select_data(self.TABLE_NAME, columns, where)

    def get_all(self, columns: list = None):    # ? columns = ['id', 'date', 'json_data']
        if not columns:
            columns = list(self.COLUMNS.keys())
        # Use the select_all_data method from the parent class
        return self.select_all_data(self.TABLE_NAME, columns)


### * Usage:-
# from config.settings import LocalDatabaseManager
# with LocalDatabaseManager() as db_manager:
    ## Perform database operations here
    ## db_manager.create(data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})})
    ## db_manager.update(data = {'date': '2021-08-01', 'json_data': json.dumps({'key1': 'value1', 'key2': 'value2'})}, where = {'id': 1})
    ## db_manager.delete(where = {'id': 1})
    ## db_manager.get(where = {'id =': 1}, columns = ['id', 'date', 'json_data'])
    ## db_manager.get_all(columns = ['id', 'date', 'json_data'])
## Connection is automatically closed when you exit the 'with' block
"""





'''
import os
import json

from PyQt6 import QtCore

from config.ui_element_names import APP_NAME
from utils.global_functions import is_frozen_executable

class SettingsManager:
    def __init__(self):
        self.app_name = APP_NAME
        # self.settings_dir = os.path.join(os.getenv("APPDATA"), app_name)
        if is_frozen_executable():
            self.settings_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppDataLocation)
        else:
            self.settings_dir = os.getcwd() + "/_temp"

    def save_settings(self, data):
        if not os.path.exists(self.settings_dir):
            os.makedirs(self.settings_dir)

        with open(os.path.join(self.settings_dir, "settings.json"), "w") as json_file:    # open in 'a' mode to append.
            json.dump(data, json_file)

    def load_settings(self):
        settings_file = os.path.join(self.settings_dir, "settings.json")
        if os.path.exists(settings_file):
            with open(settings_file, "r") as json_file:
                return json.load(json_file)
        return {}

if __name__ == "__main__":
    settings_manager = SettingsManager()

    # Save settings
    settings_manager.save_settings({"key1": "value1", "key2": "value2"})

    # Load settings
    loaded_settings = settings_manager.load_settings()
    # print(loaded_settings)
'''

