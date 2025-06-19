from .config import BASE_DIR, BACKUP_DB, BACKUP_DIR, DB_TABLE_WEATHER
from .db_config import get_database, insert_data, get_data
from .weather import get_weather

# Definir a variável __all__ para controlar o que é importado ao usar "from src import *"
__all__ = [
    "BASE_DIR",
    "BACKUP_DB",
    "BACKUP_DIR",
    "DB_TABLE_WEATHER",
    "get_database",
    "insert_data",
    "get_data",
    "get_weather"
]