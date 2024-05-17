import re
from datetime import datetime, timedelta

# Função para extrair UUID, horário e URL de cada linha do log
def extract_info(line):
    # Regex para extrair timestamp e UUID
    uuid_match = re.search(r'\[(\d{2}:\d{2}:\d{2}\.\d{3})\].*messageId=([0-9a-fA-F-]+)', line)
    # Regex para extrair a URL
    url_match = re.search(r'Chamando a url (http[^\s]+)', line)
    if uuid_match:
        timestamp_str = uuid_match.group(1)
        uuid = uuid_match.group(2)
        timestamp = datetime.strptime(timestamp_str, '%H:%M:%S.%f')
        return uuid, timestamp, url_match.group(1) if url_match else None
    return None, None, None

# Caminho para o arquivo de log
log_file_path = 'log_test.log'

# Definir tempo limite (por exemplo, 10 segundos)
time_limit = timedelta(seconds=10)

# Dicionário para armazenar UUIDs e seus horários e URLs
uuid_info = {}

# Ler o arquivo de log
with open(log_file_path, 'r') as file:
    for line in file:
        uuid, timestamp, url = extract_info(line)
        if uuid and timestamp:
            if uuid not in uuid_info:
                uuid_info[uuid] = {'timestamps': [], 'urls': set()}
            uuid_info[uuid]['timestamps'].append(timestamp)
            if url:
                uuid_info[uuid]['urls'].add(url)

# Calcular e exibir o tempo para cada UUID que excede o tempo limite
for uuid, info in uuid_info.items():
    timestamps = info['timestamps']
    urls = info['urls']
    if len(timestamps) > 1:
        start_time = timestamps[0]
        end_time = timestamps[-1]
        time_difference = end_time - start_time
        if time_difference > time_limit:
            url_list = ", ".join(urls) if urls else "Nenhuma URL registrada"
            print(f"O tempo entre o primeiro e o último log para o UUID {uuid} é: {time_difference}. URLs: {url_list}")
    else:
        print(f"UUID {uuid} tem apenas um registro de log.")

