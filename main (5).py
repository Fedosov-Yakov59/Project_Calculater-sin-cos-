import flet as ft
import math

def main(page: ft.Page):
    page.title = "Калькулятор"

    # Поля для ввода чисел
    num1 = ft.TextField(label="Число 1", width=150)
    num2 = ft.TextField(label="Число 2", width=150)

    # Поле для вывода результата
    result_text = ft.Text("Результат: ")

    # Функция обработки нажатия кнопок
    def calculate(e):
        try:
            n1 = float(num1.value)  # Получаем первое число
            operation = e.control.text  # Узнаем, какую кнопку нажали

            # Вычисляем результат
            if operation == "+":
                n2 = float(num2.value)
                result = n1 + n2
            elif operation == "-":
                n2 = float(num2.value)
                result = n1 - n2
            elif operation == "*":
                n2 = float(num2.value)
                result = n1 * n2
            elif operation == "/":
                n2 = float(num2.value)
                if n2 != 0:
                    result = n1 / n2
                else:
                    result = "Ошибка: деление на 0"
            elif operation == "sqrt":
                result = math.sqrt(n1)
            elif operation == "^":
                n2 = float(num2.value)
                result = n1 ** n2
            elif operation == "sin":
                result = math.sin(math.radians(n1))  # Преобразуем в радианы
            elif operation == "cos":
                result = math.cos(math.radians(n1))  # Преобразуем в радианы
            elif operation == "tan":
                result = math.tan(math.radians(n1))  # Преобразуем в радианы
            elif operation == "sinh":
                result = math.sinh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "cosh":
                result = math.cosh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "tanh":
                result = math.tanh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "asinh":
                result = math.asinh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "acosh":
                result = math.acosh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "atanh":
                result = math.atanh(math.radians(n1))  # Преобразуем в радианы
            elif operation == "fabs":
                result = math.fabs(math.radians(n1))  # Преобразуем в радианы
            elif operation == "pi":
                result = math.pi
            else:
                result = "Ошибка: неизвестная операция"

            result_text.value = f"Результат: {result}"  # Обновляем результат
        except ValueError:
            result_text.value = "Ошибка: введите числа!"

        page.update()  # Обновляем интерфейс

    # Кнопки операций
    buttons = [
        ft.ElevatedButton(op, on_click=calculate) for op in ["+", "-", "*", "/", "sqrt", "^", "sin", "cos", "tan", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "fabs", "pi"]
    ]

    # Добавляем все элементы в окно
    page.add(
        num1, num2,
        ft.Row(buttons, alignment=ft.MainAxisAlignment.CENTER),
        result_text
    )

ft.app(target=main)
