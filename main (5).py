import flet as ft
import math

def main(page: ft.Page):
    page.title = "Калькулятор"
    page.bgcolor = ft.colors.GREY_100  # Устанавливаем фоновый цвет

    # Поля для ввода чисел
    num1 = ft.TextField(label="Число 1", width=150, bgcolor=ft.colors.WHITE)
    num2 = ft.TextField(label="Число 2", width=150, bgcolor=ft.colors.WHITE)

    # Поле для вывода результата
    result_text = ft.Text("Результат: ", color=ft.colors.BLACK)

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
            elif operation == "asin":
                result = math.asin(math.radians(n1))  # Преобразуем в радианы
            elif operation == "acos":
                result = math.acos(math.radians(n1))  # Преобразуем в радианы
            elif operation == "atan":
                result = math.atan(math.radians(n1))  # Преобразуем в радианы
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
        ft.ElevatedButton(op, on_click=calculate) for op in ["+", "-", "*", "/", "sqrt", "^", "sin", "cos", "tan",  "asin", "acos", "atan", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "fabs", "pi"]
    ]

    # Добавляем изображения коал
    koala_image = ft.Image(src="https://example.com/koala.png", width=100, height=100)  # Замените на реальный URL изображения коалы

    # Добавляем все элементы в окно
    page.add(
        koala_image,
        num1, num2,
        ft
