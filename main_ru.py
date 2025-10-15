print('\n\n   Загрузка...')
import Mlogging
import calculateL1
import convertioL1
import infoL1
import os
import json
import subprocess
import rules
print('\n\n   Загрузка завершена!')


APP_DIR = 'C:\\Program Files\\CalculateL1'
log_file_path = f'{APP_DIR}\\logging.log'
SETTINGS_FILE_PATH = os.path.join(APP_DIR, 'settings.json')

# Создаем директорию, если ее нет
if not os.path.exists(APP_DIR):
    os.makedirs(APP_DIR)

# Глобальная переменная для хранения статуса в памяти
status = True 

# Проверяем и читаем файл настроек при запуске
try:
    with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        status = data.get('status', True) # Загружаем статус из файла
except (FileNotFoundError, json.JSONDecodeError):
    # Если файл не найден или испорчен, создаем его со значением по умолчанию
    with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump({'status': True}, f) # Записываем словарь {'status': True} в формате JSON
    status = True

def cls(): os.system('cls' if os.name == 'nt' else 'clear'); print("\n")

cls()

def change_color():
	print('Доступные цвета:')
	print('Код	Цвет')
	print('========================')
	print('0	Черный')
	print('1	Синий')
	print('2    Зеленый')
	print('3    Голубой')
	print('4    Красный')
	print('6    Желтый')
	print('7    Светло-серый')
	print('8    Темно-серый')
	print('9    Светло-синий')
	print('A    Светло-зеленый')
	print('B    Светло-голубой')
	print('C    Светло-красный')
	print('D    Светло-пурпурный')
	print('E    Светло-желтый')
	print('F    Белый')
	print('=========================')
	print('Введите "exit" Чтобы выйти')
	color = input('Укажите цвет в формате [ФонЦвет] (например) 0A >>> ')
	if color.lower() != 'exit':
		os.system(f'color {color}')
		Mlogging.logging('Попытка сменить цвет на {color}')
	Mlogging.logging('Выход из меню смены цвета')

def logginning():
    global status # Указываем, что будем менять глобальную переменную
    cls()
    print(f'Состояние логирования: {status}')
    print(f'[1] Сменить состояние')
    print(f'[2] Удалить логи')
    print(f'[3] Просмотреть логи')
    print(f'[4] Выйти')
    
    # ИСПРАВЛЕНО: было `==` вместо `=`
    logging_input = input('Выбор >>> ')
    Mlogging.logging(f'Ввод пользователя в меню логгирования: {logging_input}')
    
    if logging_input == '1':
        # Переключаем статус (True -> False, False -> True)
        status = not status
        
        # ИСПРАВЛЕНО: Правильно записываем JSON в файл
        Mlogging.logging(f'Статус логирования изменен на {status}')
        with open(SETTINGS_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump({'status': status}, f) # Сохраняем новый статус
            
        print(f"Статус логирования изменен на: {status}")
        input("Нажмите Enter для продолжения...")
    elif logging_input == '2':
    	yn = input('Вы уверены? (да/нет) >> ')
    	if yn.lower() == 'да':
    		with open(log_file_path, 'w', encoding='utf-8') as f:
    			f.write('')
    			Mlogging.logging('Логи были очищены')
    		print('Очищено!')
    	else:
    		print("Отменено")
    elif logging_input == '3':
    	subprocess.Popen(['start', '', log_file_path], shell=True)

def settings():
	Mlogging.logging('Открыто меню настроек')
	while True:
		cls()
		print(f'{'='*40}\n   Меню настроек\n{'='*40}')
		print('[0] Выход')
		print('[1] Сменить цвета')
		print('[2] Логирование')
		settings_choice = input('Выбор >>> ')
		Mlogging.logging(f'Выбор в меню настроек: {settings_choice}')
		if settings_choice == '0':
			break
		elif settings_choice == '1':
			change_color()
		elif settings_choice == '2':
			logginning()

def main():
	while True:
		cls()
		print(f'\n   Главное меню')
		print(' [0] Выход')
		print(' [1] Калькулятор (Дроби, степени, уравнения)')
		print(' [2] Конвертация числа')
		print(' [3] Вывод информации о числе')
		print(' [4] Правила математики')
		print('     [99] Настройки')
		choice = input('Выбор >>> ')
		Mlogging.logging(f'Выбор в главном меню: {choice}')
		if choice == '1':
			Mlogging.logging('Запуск калькулятора')
			calculateL1.main()
		elif choice == '2':
			convertioL1.main()
		elif choice == '3':
			infoL1.main()
		elif choice == '4':
			rules.main()
		elif choice == '99':
			settings()
		elif choice == '0':
			print('До свидания!')
			break

if __name__ == "__main__":
    Mlogging.logging('Запуск программы')
    main()
    Mlogging.logging('Выход из программы')