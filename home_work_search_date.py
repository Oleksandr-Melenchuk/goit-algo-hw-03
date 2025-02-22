from datetime import datetime, timedelta


""" Функція яка розраховує кількість днів
 між заданою датою і поточною датою """

def get_days_from_today(date):
    
    # Поточна дата
    today = datetime.today().date()

    try:

        #Заміна при наявності "-" на валідний символ 
        fixed_date = date.replace('-', '.')
        
        # Перетворення об'єкта з str в datatime
        input_date = datetime.strptime(fixed_date,'%Y.%m.%d').date()
    
        # Розрахунок кількості днів між поточною та заданою датою
        out_date = today.toordinal() - input_date.toordinal()
    
        # Повернення різниці у формати цілого числа
        return out_date

        #Обробка винятків таких як невірний тип, значення
    except ValueError: 
        print(" Введено невірний формат дати.\n Введіть дату у форматі 'РРРР-ММ-ДД' ")
    except (AttributeError, TypeError):
        print(" Неправильний тип даних. Дата повинна бути у вигляді рядка('str').")

dic = {21: 12, 12: 2, }
print(get_days_from_today(dic))


