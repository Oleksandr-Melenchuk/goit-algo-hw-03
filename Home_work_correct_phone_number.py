import re


"""Функція для нормалізації телефоних номерів
     до стандартного формату """
def normalize_phone(phone_number):
    # Регулярний вираз для сортування номера
    pattern = r'\+*\d+'

    # Відокремлення зайвих символів
    check = re.findall(pattern, phone_number)

    # Поєднання в одну строку
    result = ''.join(check)

    # Перевірка на наявність регіонального коду
    if result.find('38') == -1:
            result = '38' + result

    # Перевірка на наявність префіксу
    if result.find('+') == -1:
            result = '+' + result
        
    return result
