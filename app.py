from weather import get_weather

def main():
    city = input("Digite a cidade: ")

    data = get_weather(city)

    if "error" in data:
        print("Erro:", data["error"])
        return

    print(f"\nClima em {data['name']}")
    print("Temperatura:", data["main"]["temp"], "°C")
    print("Clima:", data["weather"][0]["description"])
    print("Vento:", data["wind"]["speed"], "km/h")

if __name__ == "__main__":
    main()
