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

    ghgfhjfjjhj
    
from operator import index
from tkinter.font import names

try:
    num = int(input())
    num1 = int(input())
except ZeroDivisionError:
    print("Друге число не може бути 0")
except ValueError:
    print("Введіть тільки ціле число")
except:
    print("Помилка")



names = ["Олексія", "Марія", "Іван", "Анна", "Дмитро"]

try:
    index = int(input("Введіть номер елемента (індекс): "))
    print(f"Ім'я під індексом {index}: {names[index]}")
except ValueError:
    print("Помилка: індекс має бути цілим числом!")
except IndexError:
    print(f"Помилка: такого індексу не існує! Допустимі індекси: від 0 до {len(names) - 1}")