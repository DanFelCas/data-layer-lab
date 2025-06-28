import threading
from src.db_config import POSTGRES_CREDENTIALS

class DatabaseCredentials:
    _credentials = POSTGRES_CREDENTIALS.copy()
    _lock = threading.Lock()

    @classmethod
    def set_database(cls, database: str) -> None:
        with cls._lock:
            cls._credentials['dbname'] = database

    @classmethod
    def set_user(cls, username: str) -> None:
        with cls._lock:
            cls._credentials['user'] = username

    @classmethod
    def set_password(cls, password: str) -> None:
        with cls._lock:
            cls._credentials['password'] = password

    @classmethod
    def set_host(cls, host: str) -> None:
        with cls._lock:
            cls._credentials['host'] = host

    @classmethod
    def set_port(cls, port: str | int) -> None:
        with cls._lock:
            cls._credentials['port'] = port

    @classmethod
    def get_credentials(cls) -> dict[str, str]:
        with cls._lock:
            return cls._credentials.copy()
