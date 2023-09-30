import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id INTEGER UNIQUE,
            user_id INTEGER NOT NULL UNIQUE,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def stat(self):
        return self.execute(f"SELECT COUNT(*) FROM Users;", fetchone=True)

    def add_user(self, user_id: int, name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, Name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(user_id, name), commit=True)

    def is_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
#-----------------------FILE-id-------------------------

    def create_table_files(self):
        sql = """
        CREATE TABLE files (
            id INTEGER UNIQUE,
            type TEXT,
            file_id TEXT,
            caption TEXT,
            user_id INTEGER,
            PRIMARY KEY (id AUTOINCREMENT)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_files(self, type: str=None, file_id: str=None, caption: str = None, user_id: str =None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO files(type, file_id, caption, user_id) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(type, file_id, caption, user_id), commit=True)

    def select_files(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = " SELECT * FROM files WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)


    def create_table_admins(self):
        sql = """
            CREATE TABLE Admins (
                id INTEGER UNIQUE,
                user_id INTEGER NOT NULL UNIQUE,
                full_name TEXT,
                PRIMARY KEY (id AUTOINCREMENT)
                );
    """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_admin(self, user_id: int, full_name: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO Admins( user_id, full_name ) VALUES(?, ?)
            """
        self.execute(sql, parameters=(user_id, full_name,), commit=True)

    def is_admin(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Admins WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_admins(self):
        sql = """
        SELECT * FROM Admins
        """
        return self.execute(sql, fetchall=True)


    def select_admins(self):
        return self.execute("SELECT * FROM Admins WHERE TRUE",fetchall=True)

    def stat_admins(self):
        return self.execute(f"SELECT COUNT(*) FROM Admins;", fetchone=True)

    def delete_admin(self,admin_id):
        self.execute(f"DELETE FROM Admins WHERE user_id={admin_id}", commit=True)

    def select_all_admin(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Admins WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def create_table_channel(self):
        sql = """
            CREATE TABLE Channels (
                id INTEGER UNIQUE,
                channel TEXT,
                PRIMARY KEY (id AUTOINCREMENT)
                );
    """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_channel(self, channel: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
            INSERT INTO Channels(channel) VALUES(?)
            """
        self.execute(sql, parameters=(channel,), commit=True)

    def check_channel(self, channel):
        return self.execute("SELECT channel FROM Channels WHERE channel=?", (channel,), fetchone=True)

    def select_channels(self):
        return self.execute("SELECT * FROM Channels WHERE TRUE",fetchall=True)

    def select_all_channels(self):
        sql = """
        SELECT * FROM Channels WHERE TRUE
        """
        return self.execute(sql, fetchall=True)

    def select_all_channel(self):
        sql = """
        SELECT * FROM Channels
        """
        return self.execute(sql, fetchall=True)




    def delete_channel(self, channel):
        return self.execute("DELETE FROM Channels WHERE channel=?", (channel,), commit=True)
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")