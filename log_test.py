import re
from datetime import datetime, timedelta

# Função para extrair UUID e horário de cada linha do log
def extract_uuid_and_time(line):
    # Regex para extrair timestamp e UUID
    match = re.search(r'\[(\d{2}:\d{2}:\d{2}\.\d{3})\].*messageId=([0-9a-fA-F-]+)', line)
    if match:
        timestamp_str = match.group(1)
        uuid = match.group(2)
        timestamp = datetime.strptime(timestamp_str, '%H:%M:%S.%f')
        return uuid, timestamp
    return None, None

# Caminho para o arquivo de log
log_file_path = 'log_test.log'

# Definir tempo limite (por exemplo, 10 segundos)
time_limit = timedelta(seconds=25)

# Dicionário para armazenar UUIDs e seus horários
uuid_timestamps = {}

# Ler o arquivo de log
with open(log_file_path, 'r') as file:
    for line in file:
        uuid, timestamp = extract_uuid_and_time(line)
        if uuid and timestamp:
            if uuid not in uuid_timestamps:
                uuid_timestamps[uuid] = []
            uuid_timestamps[uuid].append(timestamp)

# Calcular e exibir o tempo para cada UUID que excede o tempo limite
for uuid, timestamps in uuid_timestamps.items():
    if len(timestamps) > 1:
        start_time = timestamps[0]
        end_time = timestamps[-1]
        time_difference = end_time - start_time
        if time_difference > time_limit:
            print(f"O tempo entre o primeiro e o último log para o UUID {uuid} é: {time_difference}")
    else:
        print(f"UUID {uuid} tem apenas um registro de log.")
