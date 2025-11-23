from weather import get_weather

def test_api_online():
    data = get_weather("São Paulo")
    assert data["name"] == "São Paulo"