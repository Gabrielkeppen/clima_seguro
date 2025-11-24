import sys
import os
import weather
import requests

from _pytest.monkeypatch import MonkeyPatch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from weather import detect_weather_risks

def test_detect_weather_risks():
    fake_data = [
        {
            "data_hora": "2025-11-25 12:00:00",
            "descricao": "chuva forte",
            "vento": 55
        },
        {
            "data_hora": "2025-11-26 12:00:00",
            "descricao": "céu limpo",
            "vento": 10
        }
    ]

    riscos = detect_weather_risks(fake_data)

    assert len(riscos) > 0
    assert "Vento forte" in riscos[0][1] or "tempestade" in riscos[0][1].lower()

def test_get_weather_without_api_key(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(weather, "API_KEY", None)

    result = weather.get_weather("Curitiba")

    assert "error" in result
    assert "API_KEY" in result["error"]

def test_get_weather_connection_error(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.exceptions.RequestException("Erro fake de conexão")

    monkeypatch.setattr("requests.get", fake_get)

    result = weather.get_weather("QualquerCidade")

    assert "error" in result
    assert "conexão" in result["error"].lower()

def test_detect_weather_risks_no_risk():
    fake_data = [
        {
            "data_hora": "2025-11-27 12:00:00",
            "descricao": "céu limpo",
            "vento": 5
        }
    ]

    riscos = detect_weather_risks(fake_data)

    assert len(riscos) == 0
