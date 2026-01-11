# Database connection factory using Abstract Factory pattern

from abc import ABC, abstractmethod


# Database Connection
class DBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDBConnection(DBConnection):
    def connect(self):
        print(f"MySQL connection.... connected!!")


class PostgresSQLDBConnection(DBConnection):
    def connect(self):
        print(f"PostgresSQL connection.... connected!!")


# Database Cursor
class Cursor(ABC):
    @abstractmethod
    def execute(self, query: str):
        pass


class MySQLCursor(Cursor):
    def execute(self, query: str):
        print(f"MySQL Cursor Executing {query}")


class PostgresSQLCursor(Cursor):
    def execute(self, query: str):
        print(f"PostresSQL Cursor Executing {query}")


# Abstract Factory
class AbstractDBFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_cursor(self):
        pass


class MySQLDBFactory(AbstractDBFactory):
    def create_connection(self):
        return MySQLDBConnection()

    def create_cursor(self):
        return MySQLCursor()


class PostgresSQLDBFactory(AbstractDBFactory):
    def create_connection(self):
        return PostgresSQLDBConnection()

    def create_cursor(self):
        return PostgresSQLCursor()


# client code
def client(db_name: str):
    db_factory = dict(my_sql=MySQLDBFactory, postgres_sql=PostgresSQLDBFactory)

    if db_name in db_factory:
        return db_factory.get(db_name)()


if __name__ == "__main__":
    my_sql_factory = client("my_sql")

    my_sql_connection = my_sql_factory.create_connection()
    my_sql_cursor = my_sql_factory.create_cursor()

    my_sql_connection.connect()
    my_sql_cursor.execute("SELECT * FROM CUST")

    print()

    pg_sql_factory = client("postgres_sql")

    pg_sql_connection = pg_sql_factory.create_connection()
    pg_sql_cursor = pg_sql_factory.create_cursor()

    pg_sql_connection.connect()
    pg_sql_cursor.execute("SELECT * FROM CUST")
