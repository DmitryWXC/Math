import sympy as sp
from mpmath import mp
import os
import Mlogging

# Устанавливаем высокую точность для численных вычислений
mp.dps = 50 

def print_welcome_message():
    """Выводит финальное приветственное сообщение."""
    print("===================== ПРОДВИНУТЫЙ КАЛЬКУЛЯТОР v9.0 =====================")
    print("Поддерживает: +, -, *, /, ^, функции (sqrt, log), алгебру и уравнения.")
    print("Константы: 'pi' для числа Пи, 'e' для числа Эйлера.")
    print("Примеры: sin(pi/4)*2 | (x+y)**2 | x**2-16=0 | log(e)")
    print("Для выхода введите 'exit' или 'выход'.")
    print("========================================================================")

def process_expression(expression_str: str) -> sp.Expr:
    """
    Преобразует строку в символьное выражение SymPy.
    ИСПРАВЛЕНИЕ: Теперь 'e' автоматически распознается как число Эйлера.
    """
    safe_expr_str = expression_str.strip().replace('^', '**')
    if not safe_expr_str:
        raise ValueError("Ввод не может быть пустым.")
        Mlogging.logging('[ calculator ] Ошибка: Ввод не может быть пустым')
    
    # Добавляем 'e' в локальные переменные, чтобы sympy правильно его понял
    local_vars = {
        'e': sp.E, 
        'expand': sp.expand, 
        'simplify': sp.simplify
    }
    return sp.sympify(safe_expr_str, locals=local_vars)

def display_result(value, prefix="Результат"):
    """
    Интеллектуально форматирует и выводит результат.
    """
    s_val = sp.simplify(value)

    if s_val.is_integer:
        print(f"{prefix}: {s_val}")
        Mlogging.logging(f"[ calculator ] {prefix}: {s_val}")
        return

    if s_val.is_rational:
        p, q = s_val.as_numer_denom()
        print(f"{prefix} (дробь): {p}/{q}")
        Mlogging.logging(f"[ calculator ] {prefix} (дробь): {p}/{q}")
        print(f"  └─ Десятичная: {s_val.evalf()}")
        Mlogging.logging(f"[ calculator ]   └─ Десятичная: {s_val.evalf()}")
        if abs(p) > q:
            whole = int(abs(p) / q)
            rem = abs(p) % q
            sign = "- " if p < 0 else ""
            if rem != 0: print(f"  └─ Смешанная: {sign}{whole} и {rem}/{q}"); Mlogging.logging(f"[ calculator ]   └─ Смешанная: {sign}{whole} и {rem}/{q}")
        return

    print(f"{prefix} (приближенно): {s_val.evalf()}")
    Mlogging.logging(f"[ calculator ] {prefix} (приближенно): {s_val.evalf()}")
    print(f"  └─ Точное значение: {s_val}")
    Mlogging.logging(f"[ calculator ]   └─ Точное значение: {s_val}")


def main():
    Mlogging.logging('Вход в калькулятор')
    os.system("chcp 65001 > nul") 
    print_welcome_message()

    while True:
        user_input = input("\nВведите выражение (или 'exit' для выхода): ").strip()
        Mlogging.logging(f'[ calculator ] Пользователь вводит "{user_input}"')

        if not user_input:
            Mlogging.logging('[ calculator ] Неверный ввод пользователя')
            continue
        
        if user_input.lower() in ('exit', 'выход'):
            print("Выход из калькулятора. Спасибо за использование!")
            Mlogging.logging('[ calculator ] Выход из калькулятора ')
            break

        try:
            if '=' in user_input:
                lhs_str, rhs_str = user_input.split('=', 1)
                if not lhs_str or not rhs_str:
                    raise ValueError("Уравнение должно иметь левую и правую части.")
                    Mlogging.logging('[ calculator ] Ошибка решения уравнения: "Уравнение должно иметь левую и правую части."')
                
                lhs = process_expression(lhs_str)
                rhs = process_expression(rhs_str)
                
                equation = lhs - rhs
                variables = equation.free_symbols

                if not variables:
                    print(f"Числовое равенство {'верно' if equation.is_zero else 'неверно'}.")
                    Mlogging.logging("[ calculator ] Числовое равенство {'верно' if equation.is_zero else 'неверно'}.")
                    continue
                
                if sp.simplify(equation) == 0:
                    print("Это тождество, верное для любых значений переменных.")
                    Mlogging.logging('[ calculator ] Решение: Это тождество, верное для любых значений переменных.')
                    continue

                print(f"Решаем уравнение: {sp.Eq(lhs, rhs)}")
                Mlogging.logging(f"Решаем уравнение: {sp.Eq(lhs, rhs)}")
                
                # ИСПРАВЛЕНИЕ: Используем флаг dict=True для предсказуемого результата
                # sp.solve теперь ВСЕГДА возвращает список словарей.
                solution = sp.solve(equation, variables, dict=True)
                
                if not solution:
                    print("Решений не найдено.")
                    Mlogging.logging('[ calculator ] Решений не найдено')
                else:
                    print("Решение(я):")
                    Mlogging.logging('[ calculator ] Решение(я): ')
                    # Этот цикл теперь правильно обработает любой случай
                    for sol_dict in solution:
                        for var, val in sol_dict.items():
                            display_result(val, prefix=f"  {var}")

            else: # Логика для выражений
                expr = process_expression(user_input)
                if expr.free_symbols:
                    simplified_expr = sp.simplify(expr)
                    print("Упрощенное выражение:", simplified_expr)
                    Mlogging.logging(f'[ calculator ] Упрощенное выражение: {simplified_expr}')
                    
                    expanded_expr = sp.expand(expr)
                    if str(expanded_expr) != str(simplified_expr):
                         print("Раскрытое выражение:", expanded_expr)
                         Mlogging.logging(f'[ calculator ] Раскрытое выражение: {simplified_expr}')
                else:
                    display_result(expr)

        except Exception as e:
            print(f"Ошибка! Проверьте правильность ввода. ({e})")
            Mlogging.logging(f'[ calculator ] Ошибка: {e}')