import random


"""Функція для генерації набору унікальних випадкових чисел
   В разі виклику без аргументів використовую ключові параметри"""
    
def get_numbers_ticket(min=1, max=1000 , quantity=10):

    #Множина для ініціалізації циклу
    lucky_list = set()

    try:
        #Перевірка чи значення в заданому діапазоні.Якщо ні повертає пустий список
        if min < 1 or max > 1000 or quantity > max + min:
            print("Невірно заданий діапазон чисел")
            return list(lucky_list)

        '''Цикл для заповнення унікальними випадковими числами 
            до поки кількість чисел не буде = quantity '''
        while len(lucky_list) != quantity:

            #Якщо число унікальне додає до множини
            lucky_list.add(random.randint(min, max))

    except TypeError:
        print("Невірний тип даних")

    # Повертає відстортований список
    return sorted(lucky_list)





print(get_numbers_ticket([], '100', 10))





# raise ValueError("Введіть коректні значення для Min не меньше 1,\n" 
#        "для Max не більше 1000. Кількість номерів не може перевищувати\n"
#        "загальної кількості чисел")