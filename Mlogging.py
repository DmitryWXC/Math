# Файл: logging.py

from datetime import datetime
import os
import json

# Пути лучше определять один раз
LOGGING_DIR = 'C:\\Program Files\\CalculateL1'
SETTINGS_FILE_PATH = os.path.join(LOGGING_DIR, 'settings.json')
LOG_FILE_PATH = os.path.join(LOGGING_DIR, 'logging.log')

def logging(text):
    """
    Записывает сообщение в лог, если это разрешено в settings.json.
    """
    try:
        # ИСПРАВЛЕНО: Правильно читаем файл настроек
        # Открываем в режиме 'r' (чтение). Если файла нет, будет ошибка FileNotFoundError.
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
            settings_data = json.load(f)  # Читаем и сразу преобразуем из JSON в словарь
            status = settings_data.get('status', True) # Безопасно получаем ключ, по умолчанию True
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не найден, пуст или содержит невалидный JSON, 
        # считаем по умолчанию, что логирование включено.
        status = True
    
    # Если статус False, просто выходим из функции
    if not status:
        return

    # Запись в лог-файл
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{current_time} | {text}"
    
    # Открываем лог-файл в режиме 'a' (добавление в конец)
    with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')