try:
    num = int(input())
    num1 = int(input())
except ZeroDivisionError:
    print("Друге число не може бути 0")
except ValueError:
    print("Введіть тільки ціле число")
except:
    print("Помилка")



print("Програма працює")

try:
    celsius = float(input("Введіть температуру в градусах Цельсія: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Температура у Фаренгейтах: {fahrenheit}")
except ValueError:
    print("Помилка: будь ласка, введіть числове значення!")