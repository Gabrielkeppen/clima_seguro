from weather import get_weather, get_forecast_daily, detect_weather_risks

def main():
    print("\n=== Sistema de Monitoramento Climático ===")
    print("1 - Clima Atual")
    print("2 - Previsão para os próximos dias")
    print("3 - Análise de risco meteorológico")

    op = input("Escolha uma opção: ")
    cidade = input("Digite a cidade: ")

    if op == "1":
        dados = get_weather(cidade)

        if "error" in dados:
            print("Erro:", dados["error"])
        else:
            print("\nClima em:", dados["cidade"])
            print("Temperatura:", dados["temperatura"], "°C")
            print("Descrição:", dados["descricao"])
            print("Vento:", dados["vento"], "km/h")

    elif op == "2":
        previsoes = get_forecast_daily(cidade)

        if isinstance(previsoes, dict) and "error" in previsoes:
            print("Erro:", previsoes["error"])
        else:
            print("\n=== Previsão dos Próximos Dias ===")

            for p in previsoes:
                print(f"{p['data']} - {p['descricao']} - {p['temperatura']}°C - vento {p['vento']} km/h")

    elif op == "3":
        previsoes = get_forecast_daily(cidade)
        riscos = detect_weather_risks(previsoes)

        if riscos:
            print("\n ALERTAS METEOROLÓGICOS ")
            for horario, risco in riscos:
                print(f"{horario} -> {risco}")
        else:
            print("\n Nenhum risco detectado para os próximos dias.")

if __name__ == "__main__":
    main()
