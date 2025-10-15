import Mlogging

UNITS = {
    "Масса": {
        "базовая_единица": "грамм",
        "единицы": {
            "грамм": 1.0, "г": 1.0, "килограмм": 1000.0, "кг": 1000.0,
            "миллиграмм": 0.001, "мг": 0.001, "тонна": 1_000_000.0, "т": 1_000_000.0,
            "центнер": 100_000.0, "ц": 100_000.0, "фунт": 453.592, "унция": 28.3495,
        }
    },
    "Длина": {
        "базовая_единица": "метр",
        "единицы": {
            "метр": 1.0, "м": 1.0, "километр": 1000.0, "км": 1000.0,
            "сантиметр": 0.01, "см": 0.01, "миллиметр": 0.001, "мм": 0.001,
            "миля": 1609.34, "ярд": 0.9144, "фут": 0.3048, "дюйм": 0.0254,
        }
    },
    "Объем данных": {
        "базовая_единица": "байт",
        "единицы": {
            "байт": 1.0, "б": 1.0, "килобайт": 1024.0, "кб": 1024.0,
            "мегабайт": 1024.0 ** 2, "мб": 1024.0 ** 2, "гигабайт": 1024.0 ** 3,
            "гб": 1024.0 ** 3, "терабайт": 1024.0 ** 4, "тб": 1024.0 ** 4,
        }
    },
    "Мощность": {
        "базовая_единица": "ватт",
        "единицы": {
            "ватт": 1.0, "вт": 1.0, "киловатт": 1000.0, "квт": 1000.0,
            "мегаватт": 1_000_000.0, "мвт": 1_000_000.0, "лошадиная сила": 735.5
        }
    },
    "Напряжение": {
        "базовая_единица": "вольт",
        "единицы": {
            "вольт": 1.0, "в": 1.0, "киловольт": 1000.0, "кв": 1000.0,
            "милливольт": 0.001, "мв": 0.001
        }
    }
}

# --- НОВАЯ ФУНКЦИЯ ---
def format_number(num):
    """
    Форматирует число для красивого и читаемого вывода.
    - Целые числа выводит с разделителями тысяч (1234567 -> 1,234,567).
    - Дробные числа выводит с 4 знаками после запятой и убирает лишние нули.
    """
    # Проверяем, является ли число целым (даже если оно float типа 123.0)
    if num.is_integer():
        # Форматируем как целое число с разделителями-запятыми
        return f"{int(num):,}"
    else:
        # Для дробных чисел используем 6 знаков после запятой для точности,
        # а затем убираем незначащие нули в конце.
        # Например, 2.500000 -> "2.5", 2.123456 -> "2.123456"
        return f"{num:,.6f}".rstrip('0').rstrip('.')

def main():
    Mlogging.logging('[ convertio ] Запуск конвертатора')
    """
    Главная функция, которая управляет всем взаимодействием с пользователем.
    """
    categories = list(UNITS.keys())

    while True:
        # --- ШАГ 1: ВЫБОР КАТЕГОРИИ ---
        print("\n" + "="*40)
        print("    Универсальный конвертер единиц")
        print("="*40)
        print("Выберите категорию для конвертации:")
        
        for i, category_name in enumerate(categories, 1):
            print(f"  {i}. {category_name}")
        
        print(f"  {len(categories) + 1}. Выход")
        
        try:
            choice = input("\nВведите номер категории: ")
            Mlogging.logging(f'[ convertio ] Ввод пользователя: {choice}')
            choice_num = int(choice)
            
            if choice_num == len(categories) + 1:
                print("До свидания!")
                Mlogging.logging('[ convertio ] Выход из конвертера')
                break
            
            if not 1 <= choice_num <= len(categories):
                print("! Ошибка: Такого номера нет в списке. Попробуйте еще раз.")
                Mlogging.logging('[ convertio ] Ошибка, не верный выбор')
                continue

            selected_category_name = categories[choice_num - 1]
            selected_category_data = UNITS[selected_category_name]
            units_for_choice = sorted([unit for unit in selected_category_data["единицы"].keys() if len(unit) > 2])
        except ValueError:
            print("! Ошибка: Пожалуйста, введите число.")
            Mlogging.logging('[ convertio ] Неверный ввод, ввод не число')
            continue

        # --- ШАГ 2: ВЫБОР ИСХОДНОЙ ЕДИНИЦЫ ---
        print(f"\n--- Категория: {selected_category_name} ---")
        Mlogging.logging(f'[ convertio ] Выбрана категория: {selected_category_name}')
        print("Выберите исходную единицу измерения:")
        for i, unit_name in enumerate(units_for_choice, 1):
            print(f"  {i}. {unit_name.capitalize()}")
        
        try:
            unit_choice_num = int(input("\nВведите номер единицы: "))
            Mlogging.logging(f'[ convertio ] Ввод пользователя: {unit_choice_num}')
            if not 1 <= unit_choice_num <= len(units_for_choice):
                print("! Ошибка: Неверный номер единицы.")
                Mlogging.logging('[ convertio ] Ошибка, не верный выбор')
                continue
            from_unit = units_for_choice[unit_choice_num - 1]
        except ValueError:
            print("! Ошибка: Пожалуйста, введите число.")
            Mlogging.logging('Ошибка, не верный выбор')
            continue

        # --- ШАГ 3: ВВОД ЗНАЧЕНИЯ ---
        try:
            value_str = input(f"Введите значение в '{from_unit}': ").replace(',', '.')
            Mlogging.logging(f'[ convertio ] Ввод пользователя: {value_str}')
            value = float(value_str)
        except ValueError:
            print("! Ошибка: Введенное значение не является числом.")
            Mlogging.logging('Ошибка, не корр. ввод')
            continue

        # --- ШАГ 4: РАСЧЕТ И ВЫВОД ВСЕХ РЕЗУЛЬТАТОВ ---
        all_units_map = selected_category_data["единицы"]
        value_in_base_unit = value * all_units_map[from_unit]
        
        print("-" * 40)
        # --- ИЗМЕНЕНИЕ 1 ---
        # Используем новую функцию для форматирования исходного числа
        print(f"Результаты для {format_number(value)} {from_unit}:")
        print("-" * 40)
        
        for unit_name, multiplier in all_units_map.items():
            if len(unit_name) <= 2:
                continue

            result = value_in_base_unit / multiplier
            marker = "-> " if unit_name == from_unit else "   "
            
            # --- ИЗМЕНЕНИЕ 2 ---
            # Используем новую функцию для форматирования каждого результата
            formatted_result = format_number(result)
            
            # --- ИЗМЕНЕНИЕ 3 ---
            # Выводим отформатированную строку
            print(f"{marker}{formatted_result} {unit_name}")
            Mlogging.logging(f'[ convertio ] Результат: {marker}{formatted_result} {unit_name}')

        print("-" * 40)
        input("Нажмите Enter, чтобы вернуться в главное меню...")