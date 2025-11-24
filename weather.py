import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    """
    Consulta o clima atual de uma cidade usando a OpenWeather API.
    Retorna um dicionário com os dados ou erro.
    """

    if not API_KEY:
        return {"error": "API_KEY não encontrada. Verifique seu .env"}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "descricao": data["weather"][0]["description"],
            "vento": data["wind"]["speed"]
        }

    except requests.exceptions.HTTPError:
        return {"error": "Cidade não encontrada ou erro na API."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Erro de conexão: {str(e)}"}

