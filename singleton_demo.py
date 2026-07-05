import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def get_connection(self):
        return self._connection

def test_singleton():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(db1 is db2)  # Should print True

if __name__ == "__main__":
    test_singleton()
