import requests

from .config import API_WEATHER, API_WEATHER_KEY

def get_weather(woeid: int) -> dict:
    """
    Obtém dados meteorológicos para um determinado WOEID (Where On Earth IDentifier).\n
    Fonte: HG Brasil (https://hgbrasil.com/).

    Args:
        woeid (int): O WOEID para buscar os dados meteorológicos.
    Returns:
        dict: Um dicionário contendo os dados meteorológicos para o WOEID especificado.
    Exceptions:
        requests.exceptions.RequestException: Se ocorrer um erro ao fazer a requisição HTTP.
    """
    URL = f"{API_WEATHER}?{API_WEATHER_KEY}woeid={woeid}"

    response = requests.get(URL)

    return response.json()