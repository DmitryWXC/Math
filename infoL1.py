# -*- coding: utf-8 -*-
import math
import Mlogging

# --- Существующие вспомогательные функции (без изменений) ---
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def get_divisors(n):
    if n == 0: return ["Бесконечное количество"]
    if n < 0: n = abs(n)
    divs = {1, n}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

def check_perfect_abundant_deficient(n, divisors):
    if n <= 0: return "Неприменимо"
    sum_of_proper_divisors = sum(divisors[:-1])
    if sum_of_proper_divisors == n: return f"Совершенное (сумма делителей {sum_of_proper_divisors} = {n})"
    elif sum_of_proper_divisors > n: return f"Избыточное (сумма делителей {sum_of_proper_divisors} > {n})"
    else: return f"Недостаточное (сумма делителей {sum_of_proper_divisors} < {n})"

def is_happy(n):
    if n <= 0: return False
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

def is_narcissistic(n):
    if n < 0: return False
    s = str(n)
    num_digits = len(s)
    return n == sum(int(digit)**num_digits for digit in s)

def to_roman(n):
    if not (1 <= n <= 3999): return "Неконвертируемо (вне диапазона 1-3999)"
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman_num = ''
    for val, numeral in val_map:
        while n >= val:
            roman_num += numeral
            n -= val
    return roman_num

# --- НОВЫЕ ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

def get_prime_factorization(n):
    """Возвращает разложение числа на простые множители."""
    if n < 2:
        return "Неприменимо"
    factors = []
    d = 2
    temp_n = n
    while d * d <= temp_n:
        while temp_n % d == 0:
            factors.append(str(d))
            temp_n //= d
        d += 1
    if temp_n > 1:
        factors.append(str(temp_n))
    return ' × '.join(factors)

def is_perfect_square(n):
    """Эффективная проверка, является ли число полным квадратом."""
    if n < 0: return False
    if n == 0: return True
    x = int(math.sqrt(n))
    return x * x == n

def is_fibonacci(n):
    """Проверяет, является ли число числом Фибоначчи по формуле."""
    if n < 0: return False
    # Число n является числом Фибоначчи, если 5*n^2 + 4 или 5*n^2 - 4 является полным квадратом
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def is_triangular(n):
    """Проверяет, является ли число треугольным."""
    if n < 0: return False
    if n == 0: return True
    # Число n является треугольным, если 8*n + 1 является полным квадратом
    return is_perfect_square(8 * n + 1)

# --- Основная функция с пользовательским интерфейсом (обновленная) ---

def main():
    Mlogging.logging('[ info ] Вход в анализатор чисел')
    print("="*50); print("     Универсальный анализатор чисел "); print("="*50)
    
    while True:
        user_input = input("\nВведите число для анализа (или 'выход' для завершения): ").strip().lower().replace(',', '.')
        Mlogging.logging(f'[ info ] Ввод пользователя: {user_input}')
        if user_input in ['выход', 'exit', 'q']: print("До свидания!"); Mlogging.logging('[ info ] Выход из анализатора'); break
        try:
            num = float(user_input)
        except ValueError:
            print("! Ошибка: Ввод не распознан как число. Пожалуйста, попробуйте еще раз.")
            Mlogging.logging('[ info ] Ошибка, не верный ввод')
            continue
        
        print("\n" + "-"*50); print(f"     Отчет по числу: {user_input} "); print("-"*50)

        # --- ОБЩАЯ ИНФОРМАЦИЯ ---
        print("\n--- ОБЩАЯ ИНФОРМАЦИЯ ---")
        is_integer = num.is_integer()
        print(f"Тип: {'Целое' if is_integer else 'Дробное'}")
        Mlogging.logging(f"[ info ] Тип: {'Целое' if is_integer else 'Дробное'}")
        print(f"Знак: {'Положительное' if num > 0 else ('Отрицательное' if num < 0 else 'Ноль')}")
        Mlogging.logging(f"[ info ] Знак: {'Положительное' if num > 0 else ('Отрицательное' if num < 0 else 'Ноль')}")
        if num >= 0: print(f"Квадратный корень: {math.sqrt(num)}"); Mlogging.logging(f"[ info ] Квадратный корень: {math.sqrt(num)}")
        else: print(f"Квадратный корень: Не существует (для действительных чисел)"); Mloggig.logging('[ info ] Нету кв. корня')
        print(f"Научная нотация: {num:e}")
        Mlogging.logging(f"[ info ] Научная нотация: {num:e}")

        if is_integer:
            int_num = int(num)
            print("\n--- СВОЙСТВА ЦЕЛОГО ЧИСЛА ---")
            
            # Базовые свойства
            print(f"Чётность: {'Чётное' if int_num % 2 == 0 else 'Нечётное'}")
            Mlogging.logging(f"[ info ] Чётность: {'Чётное' if int_num % 2 == 0 else 'Нечётное'}")
            s_num = str(abs(int_num))
            print(f"Является палиндромом: {'Да' if s_num == s_num[::-1] else 'Нет'}")
            Mlogging.logging(f"[ info ] Является палиндромом: {'Да' if s_num == s_num[::-1] else 'Нет'}")
            
            # Свойства цифр
            print(f"Количество цифр: {len(s_num)}")
            print(f"Сумма цифр: {sum(int(digit) for digit in s_num)}")
            Mlogging.logging(f"[ info ] Количество цифр: {len(s_num)}")
            Mlogging.logging(f"[ info ] Сумма цифр: {sum(int(digit) for digit in s_num)}")

            # Свойства делимости
            if int_num < 2: print("Простота: Ни простое, ни составное"); Mlogging.logging('[ info ] Простота: Ни простоеЮ ни составное')
            elif is_prime(int_num): print("Простота: Простое число"); Mlogging.logging('[ info ] Простота: Простое число')
            else:
                print("Простота: Составное число"); Mlogging.logging('[ info ] Простота: Составное число')
                print(f"Разложение на множители: {get_prime_factorization(int_num)}"); Mlogging.logging(f"[ info ] Разложение на множители: {get_prime_factorization(int_num)}")
            
            divs = get_divisors(int_num)
            print(f"Делители ({len(divs)} шт.): {', '.join(map(str, divs))}")
            Mlogging.logging(f'[ info ] Делители ({len(divs)} шт.): {', '.join(map(str, divs))}')
            if isinstance(divs[0], int):
                print(f"Классификация: {check_perfect_abundant_deficient(int_num, divs)}"); Mlogging.logging(f"[ info ] Классификация: {check_perfect_abundant_deficient(int_num, divs)}")

            # Степенные свойства
            if int_num >= 0:
                print(f"Является полным квадратом: {'Да' if is_perfect_square(int_num) else 'Нет'}"); Mlogging.logging(f"[ info ] Является полным квадратом: {'Да' if is_perfect_square(int_num) else 'Нет'}")
                cbrt = round(int_num**(1/3.0), 10)
                print(f"Является полным кубом: {'Да' if cbrt.is_integer() else 'Нет'}"); Mlogging.logging(f"[ info ] Является полным кубом: {'Да' if cbrt.is_integer() else 'Нет'}")

            # Последовательности
            print("\n--- ТЕОРИЯ ЧИСЕЛ И ПОСЛЕДОВАТЕЛЬНОСТИ ---")
            print(f"Является числом Фибоначчи: {'Да' if is_fibonacci(int_num) else 'Нет'}"); Mlogging.logging(f"[ info ] Является числом Фибоначчи: {'Да' if is_fibonacci(int_num) else 'Нет'}")
            print(f"Является треугольным числом: {'Да' if is_triangular(int_num) else 'Нет'}"); Mlogging.logging(f"[ info ] Является треугольным числом: {'Да' if is_triangular(int_num) else 'Нет'}")
            print(f"Счастливое число: {'Да' if is_happy(int_num) else 'Нет'}"); Mlogging.logging(f"[ info ] частливое число: {'Да' if is_happy(int_num) else 'Нет'}")
            print(f"Нарциссическое число: {'Да' if is_narcissistic(int_num) else 'Нет'}"); Mlogging.logging(f"[ info ] Нарциссическое число: {'Да' if is_narcissistic(int_num) else 'Нет'}")

            # Представления
            print("\n--- ДРУГИЕ ФОРМЫ ЗАПИСИ ---")
            if 0 <= int_num <= 20: # Факториал вычисляем только для небольших чисел
                print(f"Факториал ({int_num}!): {math.factorial(int_num):,}"); Mlogging.loggin(f" [ info ] Факториал ({int_num}!): {math.factorial(int_num):,}")
            else:
                print(f"Факториал ({int_num}!): Слишком большое число для отображения"); Mlogging.logging(f"[ info ] Факториал ({int_num}!): Слишком большое число для отображения")
            
            print(f"Двоичная: {bin(int_num)}"); Mlogging.logging(f"[ info ] Двоичная: {bin(int_num)}")
            print(f"Восьмеричная: {oct(int_num)}"); Mlogging.logging(f"[ info ] Восьмеричная: {oct(int_num)}")
            print(f"Шестнадцатеричная: {hex(int_num)}"); Mlogging.logging(f"[ info ] Шестнадцатеричная: {hex(int_num)}")
            print(f"Римская: {to_roman(int_num)}"); Mlogging.logging(f"[ info ] Римская: {to_roman(int_num)}")

        print("\n" + "-"*50)
        input("Нажмите Enter для анализа следующего числа...")