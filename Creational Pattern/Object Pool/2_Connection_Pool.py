# Example Connection Pool Manager
import random
import uuid
import time


class Connection:
    def __init__(self):
        self.id = uuid.uuid4()
        self.is_connected = False

    def __str__(self):
        return f"Connection ID = {self.id}"

    def connect(self):
        print(f"Connecting to Server........ Connection ID = {self.id}")
        time.sleep(random.randint(1, 10))
        self.is_connected = True
        print(f"Connection ID = {self.id} Connected!!!!")

    def disconnect(self):
        print(f"Disconnecting to Server........ Connection ID = {self.id}")
        time.sleep(random.randint(1, 10))
        self.is_connected = False
        print(f"Connection ID = {self.id} Disconnected!!!!")


class ConnectionPoolManager:
    def __init__(self, max_connections: int):
        self.max_connections = max_connections
        self.available_connections = []
        self.in_use_connection = []

        for i in range(max_connections):
            self.available_connections.append(Connection())

    def acquire_connection(self):
        if self.acquire_connection:
            conn = self.available_connections.pop()
            self.in_use_connection.append(conn)
            conn.connect()
            return conn
        else:
            print("No Connections available...")

    def release_connection(self, conn: Connection):
        conn.disconnect()
        self.in_use_connection.remove(conn)
        self.available_connections.append(conn)

    def __str__(self):
        return f"Available Connections = {len(self.available_connections)} && Acquired Connections = {len(self.in_use_connection)}"


if __name__ == "__main__":
    pool = ConnectionPoolManager(5)

    conn1 = pool.acquire_connection()
    print(pool)
    print("*" * 50)
    conn2 = pool.acquire_connection()
    print(pool)
    print("*" * 50)
    conn3 = pool.acquire_connection()
    print(pool)
    print("*" * 50)
    conn4 = pool.acquire_connection()
    print(pool)
    print("*" * 50)
    conn5 = pool.acquire_connection()
    print(pool)
    print("*" * 50)
