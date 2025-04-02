import datetime
import os
import json
import requests
from config.settings import Config

LOG_FILE = "logs.json"

def log_api_request(endpoint, method="GET", data=None):
    url = f"{Config.BITRIX_URL_API}{endpoint}"
    start_time = datetime.datetime.utcnow()

    response = requests.request(
        method, url, json=data, auth=(Config.USERNAME_GENIAL, Config.PASSWORD_GENIAL)
    )

    end_time = datetime.datetime.utcnow()
    response_time = (end_time - start_time).total_seconds() * 1000  # Converte para ms
    data_size = len(response.content) / 1024  # Converte para KB

    log_entry = {
        "timestamp": start_time.isoformat(),
        "partner": "Genial",
        "endpoint": endpoint,
        "response_time": response_time,
        "data_size": round(data_size, 2),
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

    return response.json()


def generate_report(params):
    """Gera um relatório básico dos logs registrados"""
    if not os.path.exists(LOG_FILE):
        return {"error": "Nenhum log encontrado"}, 404

    with open(LOG_FILE, "r") as file:
        logs = json.load(file)

    # Retorna todos os logs por enquanto (pode ser melhorado com filtros via `params`)
    return {"logs": logs}, 200