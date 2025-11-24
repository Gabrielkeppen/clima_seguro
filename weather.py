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

def get_forecast_daily(city: str):
    if not API_KEY:
        return {"error": "API_KEY não encontrada."}

    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        daily_forecast = []

        for item in data["list"]:
            # Pegamos só os registros do meio-dia
            if "12:00:00" in item["dt_txt"]:
                daily_forecast.append({
                    "data": item["dt_txt"].split(" ")[0],
                    "temperatura": item["main"]["temp"],
                    "descricao": item["weather"][0]["description"],
                    "vento": item["wind"]["speed"]
                })

        return daily_forecast

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def detect_weather_risks(forecast_data):
    """
    Analisa os dados de previsão e identifica riscos climáticos.
    """

    riscos = []

    for item in forecast_data:
        descricao = item["descricao"].lower()
        vento = item["vento"]

        if "trovoada" in descricao or "tempestade" in descricao:
            riscos.append((item["data_hora"], "Possível tempestade"))

        if vento > 50:
            riscos.append((item["data_hora"], "Vento forte"))

        if "chuva" in descricao and vento > 40:
            riscos.append((item["data_hora"], "Risco de tempestade severa"))

    return riscos