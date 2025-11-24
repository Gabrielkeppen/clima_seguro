# Clima Seguro - Monitoramento de Riscos Climáticos

Sistema desenvolvido em Python com integração à **OpenWeather API** para auxiliar no monitoramento climático da cidade de **Rio Bonito do Iguaçu**, contribuindo com a prevenção de riscos durante o processo de reconstrução após o desastre natural.

O projeto foi desenvolvido como parte da atividade **A3 – Gestão e Qualidade de Software**.

---

## Objetivo

Fornecer uma ferramenta simples e acessível para:
- Consultar o **clima atual**;
- Obter a **previsão para os próximos dias**;
- Detectar **possíveis riscos meteorológicos**, como chuvas intensas, ventos fortes e tempestades.

---

## Tecnologias utilizadas

- **Python 3.12**
- **OpenWeather API**
- **Requests** (requisições HTTP)
- **Pytest** (testes automatizados)
- **Coverage.py** (cobertura de testes)
- **python-dotenv** (variáveis de ambiente)
- **Git e GitHub** (controle de versão)

---

## Estrutura do projeto

clima_seguro/
│
├── weather.py # Lógica principal da aplicação
├── app.py # Interface
├── tests/
│ ├── test_unit.py # Testes unitários
│ └── test_integration.py # Testes de integração
├── .env # Chave da API
├── .gitignore
├── requirements.txt
└── README.md

---

## Configuração da OpenWeather API

Crie um arquivo `.env` na raiz do projeto e adicione:
API_KEY=SUA_CHAVE_AQUI


> Esse arquivo está no `.gitignore` e **não é enviado ao GitHub**.

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Gabrielkeppen/clima_seguro.git
cd clima_seguro

2. Crie e ative o ambiente virtual:

python -m venv venv
venv\Scripts\activate  # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o sistema:

python app.py

---

## Testes automatizados

O projeto possui testes unitários e de integração.
Rodar os testes:

pytest

---

## Cobertura de Testes

Foi utilizado o Coverage.py para garantir a qualidade do código.
Gerar relatório de cobertura:

coverage run -m pytest
coverage report
coverage html

---

## Funcionalidades

  - Consulta de clima atual
  -Previsão dos próximos dias
  -Detecção de riscos meteorológicos
  -Tratamento de erros de conexão e API
  -Testes automatizados com mais de 80% de cobertura

---

## Autor

Desenvolvido por Gabriel Keppen
Curso: Ciência da Computação
Disciplina: Gestão e Qualidade de Software
Universidade: Unicuritiba
