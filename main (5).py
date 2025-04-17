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
            else:
                result = "Ошибка: неизвестная операция"

            result_text.value = f"Результат: {result}"  # Обновляем результат
        except ValueError:
            result_text.value = "Ошибка: введите числа!"

        page.update()  # Обновляем интерфейс

    # Кнопки операций
    buttons = [
        ft.ElevatedButton(op, on_click=calculate) for op in ["+", "-", "*", "/", "sqrt", "^", "sin", "cos"]
    ]

    # Добавляем все элементы в окно
    page.add(
        num1, num2,
        ft.Row(buttons, alignment=ft.MainAxisAlignment.CENTER),
        result_text
    )

ft.app(target=main)