import random


"""Функція для генерації набору унікальних випадкових чисел
   В разі виклику без аргументів використовую ключові параметри"""
    
def get_numbers_ticket(min=1, max=1000 , quantity=10):

    #Множина для ініціалізації циклу
    lucky_list = set()

    #Список для перевірки вхідних даних
    variables = [min, max, quantity]

    try:
        # Перевірка чи вказаний тип відповідає int
        for x in variables:
                if not isinstance(x, int):
                    raise TypeError
                
        #Перевірка чи значення в заданому діапазоні
        if min < 1 or max > 1000 or quantity > (max - min + 1) or min > max:
            raise ValueError

        '''Цикл для заповнення унікальними випадковими числами 
            до поки кількість чисел не буде = quantity '''
        while len(lucky_list) != quantity:

            #Якщо число унікальне додає до множини
            lucky_list.add(random.randint(min, max))

    #Обробка винятків таких як невірний тип, значення
    except ValueError:
         print("Невірно вказане значення")
         return []
    except TypeError:
        print("Невірно вказаний тип")
        return []

    # Повертає відстортований список
    return sorted(lucky_list)
