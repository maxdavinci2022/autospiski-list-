from inputimeout import inputimeout, TimeoutOccurred

data = []

print("Введите данные (числа, строки, символы). У вас есть 3 секунды на каждый ввод.")

while True:
    try:
        user_input = inputimeout(prompt="Введите данные: ", timeout=3)
        
        # Пытаемся преобразовать введённые данные в число
        try:
            if "." in user_input:  # Если есть точка, пробуем преобразовать в float
                number = float(user_input)
            else:  # Иначе пробуем преобразовать в int
                number = int(user_input)
            data.append(number)  # Добавляем число в список
            print(f"Число {number} добавлено в список.")
        except ValueError:
            # Если преобразование в число не удалось, добавляем как строку
            data.append(user_input)
            print(f"Строка '{user_input}' добавлена в список.")
    
    except TimeoutOccurred:
        print("\nВремя истекло! Программа завершена.")
        break

print(f"Ваш список: l = {data}")
