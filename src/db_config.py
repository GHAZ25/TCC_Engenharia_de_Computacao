from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import results as pmr
from pymongo import errors as pme
from .config import CONNECTION_STRING, DB_NAME

def get_database() -> MongoClient:
    """
    Obtém uma instância do banco de dados MongoDB.\n
    Returns:
        MongoClient: Instância do cliente MongoDB conectado ao banco de dados especificado.
    Exceptions:
        pymongo.errors.ConnectionError: Se não for possível conectar ao banco de dados.
    """
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi("1"))
 
    return client[DB_NAME]

def insert_data(table_name: str, data: dict) -> pmr.InsertOneResult:
    """
    Insere dados em uma tabela do banco de dados MongoDB.\n
    Args:
        table_name (str): Nome da tabela onde os dados serão inseridos.
        data (dict): Dados a serem inseridos na tabela.
    Returns:
        pymongo.results.InsertOneResult: Resultado da inserção, contendo o ID do documento inserido.
    Exceptions:
        pymongo.errors.PyMongoError: Se ocorrer um erro ao acessar o banco de dados ou inserir os dados.
    """
    database = get_database()
    collection = database[table_name]
    result = collection.insert_one(data)

    return result.inserted_id

def get_data(table_name: str) -> list:
    """
    Obtém todos os documentos de uma tabela do banco de dados MongoDB.\n
    Args:
        table_name (str): Nome da tabela de onde os dados serão recuperados.
    Returns:
        list: Lista de documentos encontrados na tabela.
    Exceptions:
        pymongo.errors.PyMongoError: Se ocorrer um erro ao acessar o banco de dados.
    """
    database = get_database()
    collection = database[table_name]

    return list(collection.find())