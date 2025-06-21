import os
from dotenv import load_dotenv

# Define o caminho absoluto do arquivo .env
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
ENV_FILE = os.path.join(BASE_DIR, ".env")

# Carrega o arquivo .env
load_dotenv(ENV_FILE)

# Definição das variáveis globais
API_WEATHER = os.getenv("API_WEATHER", default="https://api.hgbrasil.com/weather")
API_WEATHER_KEY = f"key={os.getenv("API_WEATHER_KEY")}&" if os.getenv("API_WEATHER_KEY") != None and os.getenv("API_WEATHER_KEY") != "" else ""
BACKUP_DB = os.getenv("BACKUP_DB", default="False").lower() in ("true", "1", "yes")
BACKUP_DIR = os.getenv("BACKUP_DIR", default="")
CONNECTION_STRING = os.getenv("CONNECTION_STRING", default="mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", default="db_weather")
DB_TABLE_WEATHER = os.getenv("DB_TABLE_WEATHER", default="table_weather")