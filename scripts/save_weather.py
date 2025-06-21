import os
import sys
import json

# Adiciona o caminho do módulo ao sys.path para permitir a importação do módulo src
module_path = os.path.abspath(os.path.dirname(__file__) + "/..")
sys.path.append(module_path)

from datetime import datetime
from src import get_weather, insert_data, BASE_DIR, DB_TABLE_WEATHER, BACKUP_DB, BACKUP_DIR

cidades = [429100, 862592, 1521894, 2430300, 15015372]
"""
Lista de WOEIDs das cidades para buscar os dados meteorológicos:
Fonte: HG Weather (https://console.hgbrasil.com/documentation/weather/tools)

429100 - Caxias do Sul, Rio Grande do Sul (Brasil)
862592 - Oslo (Noruega)
1521894 - Cairo (Egito)
2430300 - Juneau, Alaska (Estados Unidos)
15015372 - Kyoto (Japão)
"""

try:
    for woeid in cidades:
        # Obtém os dados meteorológicos para o WOEID atual
        dados = get_weather(woeid)

        # Verifica se os dados foram encontrados
        if dados["results"]["city"] == "" or dados["results"]["city"] == None:
            raise Exception(f"Dados meteorológicos não encontrados para o WOEID {woeid}.")

        # Adiciona o resultado dos dados metereológicos encontrados no MongoDB
        id = insert_data(DB_TABLE_WEATHER, dados)

        # Se o backup do banco de dados estiver ativado, salva os dados em um arquivo JSON
        if BACKUP_DB and os.path.exists(f"{BACKUP_DIR}"):
            del dados["_id"]

            with open(f"{BACKUP_DIR}/{id}.json", "w") as arquivo:
                json.dump(dados, arquivo)
except Exception as e:
    # Cria o diretório de erros se não existir
    if not os.path.exists(f"{BASE_DIR}/error"):
        os.makedirs(f"{BASE_DIR}/error")

    # Registra o erro em um arquivo de log
    with open(f"{BASE_DIR}/error/{datetime.now().strftime("%Y-%m-%d")}.txt", "a") as arquivo:
        arquivo.write(f"Erro: {e}.\n")