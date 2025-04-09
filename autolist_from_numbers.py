from inputimeout import inputimeout, TimeoutOccurred  # Импортируем необходимые функции

numbers = []  # Создаём пустой список для чисел

print("Введите целые числа. У вас есть 3 секунды на каждый ввод.")

while True:  # Бесконечный цикл
    try:
        # Запрашиваем ввод с таймером 3 секунды
        user_input = inputimeout(prompt="Введите число: ", timeout=3)
        
        # Проверяем, является ли введённое значение числом
        number = int(user_input)
        numbers.append(number)  # Добавляем число в список
        print(f"Число {number} добавлено в список.")
    
    except ValueError:
        # Если введено не число
        print("Ошибка! Введите целое число.")
    
    except TimeoutOccurred:
        # Если время на ввод истекло
        print("\nВремя истекло! Программа завершена.")
        break

# Выводим получившийся список в формате "l = [...]"
print(f"Ваш список: l = {numbers}")