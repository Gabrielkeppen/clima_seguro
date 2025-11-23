from weather import get_weather

def test_get_weather_returns_data():
    data = get_weather("Curitiba")
    assert "main" in data
