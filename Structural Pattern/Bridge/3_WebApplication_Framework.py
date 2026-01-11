# WebApplication Framework
from abc import ABC, abstractmethod


class WebApplicationFramework(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def route(self, path):
        pass

    @abstractmethod
    def render(self, filename):
        pass

    def execute(self, query):
        self.driver.connect()
        self.driver.execute(query)
        self.driver.disconnect()


class Flask(WebApplicationFramework):
    def route(self, path):
        print(f"routing to {path}")

    def render(self, filename):
        print(f"rendering page {filename}")


class Django(WebApplicationFramework):
    def route(self, path):
        print(f"routing to {path}")

    def render(self, filename):
        print(f"rendering page {filename}")


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connecting to Database using MYSQL Driver")

    def execute(self, query):
        print(f"Executing {query} using MYSQL Driver")

    def disconnect(self):
        print(f"Disconnecting from Database using MYSQL Driver")


class PostgreSQL(Database):
    def connect(self):
        print("Connecting to Database using PostgreSQL Driver")

    def execute(self, query):
        print(f"Executing {query} using PostgreSQL Driver")

    def disconnect(self):
        print(f"Disconnecting from Database using PostgreSQL Driver")


if __name__ == "__main__":
    my_sql = MySQL()
    postgre_sql = PostgreSQL()

    flask = Flask(my_sql)
    flask.route("/flask")
    flask.render("index.html")
    flask.execute("SELECT * FROM CUST")

    print()

    django = Django(postgre_sql)
    django.route("/flask")
    django.render("index.html")
    django.execute("SELECT * FROM CUST")
