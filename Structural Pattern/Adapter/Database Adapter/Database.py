from MySQL import MySQLDatabase
from PostgreSQL import PostgreSQLDatabase


class DB:
    def insert(self, record):
        pass

    def delete(self, record):
        pass

    def update(self, record):
        pass

    def select(self, record):
        pass


class MySQLAdapter(DB):
    def __init__(self, adaptee):
        self.my_sql_adaptee = adaptee

    def insert(self, record):
        self.my_sql_adaptee.insert(record)

    def delete(self, record):
        self.my_sql_adaptee.delete(record)

    def update(self, record):
        self.my_sql_adaptee.update(record)

    def select(self, record):
        self.my_sql_adaptee.select(record)


class PostgreSQLAdapter(DB):
    def __init__(self, adaptee):
        self.postgresql_adaptee = adaptee

    def insert(self, record):
        self.postgresql_adaptee.insert(record)

    def delete(self, record):
        self.postgresql_adaptee.delete(record)

    def update(self, record):
        self.postgresql_adaptee.update(record)

    def select(self, record):
        self.postgresql_adaptee.select(record)


if __name__ == "__main__":
    my_sql_adapter = MySQLAdapter(MySQLDatabase())
    my_sql_adapter.insert("record-1")
    my_sql_adapter.delete("record-1")
    my_sql_adapter.update("record-1")
    my_sql_adapter.select("record-1")
    print()
    posgresql_adapter = PostgreSQLAdapter(PostgreSQLDatabase())
    posgresql_adapter.insert("record-1")
    posgresql_adapter.delete("record-1")
    posgresql_adapter.update("record-1")
    posgresql_adapter.select("record-1")
