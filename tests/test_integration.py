import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from weather import get_weather
from weather import get_forecast_daily

def test_get_weather_real_api():
    response = get_weather("Curitiba")

    assert isinstance(response, dict)
    assert "cidade" in response
    assert "temperatura" in response
    assert response["cidade"].lower() == "curitiba"

def test_get_forecast_daily_real_api():
    forecast = get_forecast_daily("Curitiba")

    assert isinstance(forecast, list)
    assert len(forecast) > 0

    for day in forecast:
        assert "data" in day
        assert "temperatura" in day
        assert "descricao" in day