from weather import get_weather

def main():
    print("=== Sistema de Monitoramento Climático ===")
    city = input("Digite o nome da cidade: ")

    resultado = get_weather(city)

    if "error" in resultado:
        print("Erro:", resultado["error"])
    else:
        print("\nClima em:", resultado["cidade"])
        print("Temperatura:", resultado["temperatura"], "°C")
        print("Descrição:", resultado["descricao"])
        print("Vento:", resultado["vento"], "km/h")

if __name__ == "__main__":
    main()
