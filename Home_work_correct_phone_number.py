import re
"""Функція для нормалізації телефоних номерів
     до стандартного формату """
def normalize_phone(phone_number):
     

     try:
          # Перевірка на відповідність типу
          if not isinstance(phone_number, str):
               raise TypeError('Введено невірний тип даних')
          
          
          # Регулярний вираз для сортування номера
          pattern = r'\+?\d+'

          # Відокремлення зайвих символів
          check = re.findall(pattern, phone_number)

          # Поєднання в одну строку
          result = ''.join(check)
          
          # Перевірка номера на мінімальну та максимальну кількість символів
          if len(result) < 9 or len(result) > 13:
               raise ValueError("Невірна довжина номера")

          # Перевірка на наявність регіонального коду та префіксу '+'
          if result.startswith('380'):
               result = '+' + result

          elif result.startswith('0'):
               result = '+38' + result
          
          elif result.startswith('80'):
               result = '+3' + result

     #Обробка винятків таких як невірний тип, значення
     except TypeError:
          print('Введено невірний тип даних')
          return None
     
     except ValueError:
          print(f"{result} Некоректний номер телефону")
          return None
     
     return result